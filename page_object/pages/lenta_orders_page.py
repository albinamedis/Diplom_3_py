import pytest
import allure
from pages.base_page import BasePage
from locators.lenta_orders_locators import LentaOrdersLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class LentaOrdersPage(BasePage):

    @allure.step("Открыть информацию о заказе")
    def open_modal_about_orders(self):
        self.click_to_element(LentaOrdersLocators.CLICK_FOR_ORDER)
        element = self.find_element_with_wait(LentaOrdersLocators.FORM_ABOUT_ORDER)
        return element.is_displayed()
    
    @allure.step("Найти заказ пользователя в ленте")
    def find_order_user(self):
        elements = self.find_elements_with_wait(LentaOrdersLocators.LIST_ORDERS)
        order_numbers = [el.text.strip() for el in elements]
        return order_numbers

    @allure.step("Получить количество заказов за все время")
    def get_count_all_time_orders(self):
        value = self.find_element_with_wait(LentaOrdersLocators.ALL_TIME_ORDERS)
        return value

    @allure.step("Получить количество заказов за сегодня")
    def get_count_today_orders(self):
        value = self.find_element_with_wait(LentaOrdersLocators.ALL_TIME_ORDERS)
        return value
    
    @allure.step("Закрыть overlay")
    def close_overlay(self):
        # Нажимаем ESC на весь документ (активный элемент)
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        self.wait_for_modal_overlay_to_disappear(LentaOrdersLocators.OVERLAY)

    @allure.step("Получить заказ в статусе В работе")
    def get_order_in_work(self, order_number):
        self.find_element_with_text(LentaOrdersLocators.ORDER_IN_WORK, order_number)
        return self.driver.find_element(*LentaOrdersLocators.ORDER_IN_WORK).text
    