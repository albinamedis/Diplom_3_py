import pytest
import allure
from pages.base_page import BasePage
from locators.account_locators import AccountLocators 


class AccountPage(BasePage):

    @allure.step("Выполнить авторизацию по логину и паролю")
    def sign_by_account(self, email, password):
        self.add_text_to_element(AccountLocators.EMAIL, email)
        self.add_text_to_element(AccountLocators.PASSWORD, password)
        self.click_to_element(AccountLocators.BUTTON_SIGN)
        element = self.find_element_with_wait(AccountLocators.BUTTON_CREATE_ORDER)
        return element.is_displayed()
    
    @allure.step("Открыть историю заказов")
    def open_page_by_history_orders(self):
        self.click_to_element(AccountLocators.HISTORY_ORDERS)
        return self.driver.current_url
    
    @allure.step("Выйти из аккаунта")
    def logout_account(self):
        self.click_to_element(AccountLocators.BUTTON_LOGOUT)
        element = self.find_element_with_wait(AccountLocators.FORM_SIGN)
        return element.is_displayed()
    
    @allure.step("Восстановаить пароль")
    def forgot_password(self):
        self.click_to_element(AccountLocators.FORGOT_PASSWORD)
        element = self.find_element_with_wait(AccountLocators.TITLE_FORGOT_PASSWORD)
        return element.is_displayed()
    
    @allure.step("Ввести логин")
    def email_for_forgot_password(self, email):
        self.add_text_to_element(AccountLocators.EMAIL, email)
        self.click_to_element(AccountLocators.BUTTON_FORGOT_PASSWORD)
        element = self.find_element_with_wait(AccountLocators.TITLE_FORGOT_PASSWORD)
        return element.is_displayed()

    @allure.step("Посмотреть пароль")
    def email_view_password(self):
        self.click_to_element(AccountLocators.PASSWORD)
        modal = self.find_element_with_wait(AccountLocators.ACTIVE_FORM_PASSWORD)
        classes = modal.get_attribute("class")
        return classes
