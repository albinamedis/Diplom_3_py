import pytest
import allure
from pages.base_page import BasePage
from locators.menu_locators import MenuLocators
from locators.konstruktor_locators import KonstruktorLocators
from locators.lenta_orders_locators import LentaOrdersLocators
from locators.account_locators import AccountLocators


class MenuPage(BasePage):

    @allure.step("Нажать на раздел Конструктор")
    def open_page_by_konstruktor(self):
        self.click_to_element(MenuLocators.CLICK_KONSTRUCTOR)
        element = self.find_element_with_wait(KonstruktorLocators.TITLE_BUILD_BURGER)
        return element.is_displayed()
    
    @allure.step("Нажать на раздел Лента заказов")
    def open_page_by_lenta_orders(self):
        self.click_to_element(MenuLocators.CLICK_LENTA_ORDERS)
        element = self.find_element_with_wait(LentaOrdersLocators.TITLE_LENTA_ORDERS)
        return element.is_displayed()
    
    @allure.step("Открыть страницу авторизации")
    def open_page_by_sign(self):
        self.click_to_element(MenuLocators.CLICK_ACCOUNT)
        element = self.find_element_with_wait(AccountLocators.FORM_SIGN)
        return element.is_displayed()
    
    @allure.step("Нажать на раздел Личный кабинет")
    def open_page_by_profile(self):
        self.click_to_element(MenuLocators.CLICK_ACCOUNT)
        element = self.find_element_with_wait(AccountLocators.PROFILE)
        return element.is_displayed()