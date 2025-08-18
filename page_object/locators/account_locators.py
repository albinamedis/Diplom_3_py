from selenium.webdriver.common.by import By

class AccountLocators:

    FORM_SIGN = [By.CLASS_NAME, "Auth_login__3hAey"]
    EMAIL = [By.XPATH, "//label[text()='Email']/../input"]
    PASSWORD = [By.XPATH, "//label[text()='Пароль']/../input"]
    BUTTON_SIGN = [By.XPATH, "//button[text()='Войти']"]
    PROFILE = [By.CLASS_NAME, "Account_text__fZAIn"]
    HISTORY_ORDERS = [By.XPATH, "//a[text()='История заказов']"]
    FORM_HISTORY_ORDERS = [By.CLASS_NAME,"OrderHistory_profileList__374GU"]
    BUTTON_LOGOUT = [By.XPATH, "//button[text()='Выход']"]
    FORGOT_PASSWORD = [By.XPATH, "//a[text()='Восстановить пароль']"]
    TITLE_FORGOT_PASSWORD = [By.XPATH, "//h2[text()='Восстановление пароля']"]
    BUTTON_FORGOT_PASSWORD = [By.XPATH, "//button[text()='Восстановить']"]
    ACTIVE_FORM_PASSWORD = [By.XPATH, "//label[text()='Пароль']/parent::div"]
    BUTTON_CREATE_ORDER = [By.XPATH, "//button[text()='Оформить заказ']"]

