import pytest
from selenium import webdriver
from methods.auth_methods import AuthMethods
from pages.menu_page import MenuPage
from pages.account_page import AccountPage
from pages.lenta_orders_page import LentaOrdersPage
from pages.konstruktor_page import KonstruktorPage
from data import BASE_URL, URL_LOGIN
from helpers import GenUser


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
    else:
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def auth_methods():
    return AuthMethods()

@pytest.fixture
def menu_page(driver):
    driver.get(BASE_URL)
    return MenuPage(driver)

@pytest.fixture
def account_page(driver):
    return AccountPage(driver)

@pytest.fixture
def lenta_orders_page(driver):
    return LentaOrdersPage(driver)

@pytest.fixture
def konstruktor_page(driver):
    driver.get(BASE_URL)
    return KonstruktorPage(driver)

# Генерация рандомного email, пароля и имени
@pytest.fixture
def gen_email_password_name():
    gen = GenUser()
    email = f"{gen.generate_random_string(10)}@yandex.ru"
    password = gen.generate_random_string(10)
    name = gen.generate_random_string(10)
    return email, password, name

# Создать нового пользователя
@pytest.fixture
def create_user(auth_methods, gen_email_password_name):
    email, password, name = gen_email_password_name
    payload = {"email": email, "password": password, "name": name}
    response = auth_methods.post_register(payload)
    token = response.json()['accessToken']
    yield token, email, password
    auth_methods.delete_user(token)

# Авторизованный пользователь (только для тестов, где нужна авторизация)
@pytest.fixture
def auth_user(driver, create_user):
    token, email, password = create_user
    driver.delete_all_cookies()
    driver.get(URL_LOGIN)
    account_page = AccountPage(driver)
    account_page.sign_by_account(email, password)
    yield MenuPage(driver)
