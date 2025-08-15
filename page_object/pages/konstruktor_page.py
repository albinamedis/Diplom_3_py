import pytest
import allure
from pages.base_page import BasePage
from locators.konstruktor_locators import KonstruktorLocators
from data import default_text_order


class KonstruktorPage(BasePage):

    @allure.step("Открыть информацию об ингредиенте")
    def open_modal_about_ingredient(self):
        self.click_to_element(KonstruktorLocators.CLICK_TO_INGREDIENTS)
        element = self.find_element_with_wait(KonstruktorLocators.TITLE_ABOUT_INGREDIENT)
        return element.is_displayed()
    
    @allure.step("Закрыть информацию об ингредиенте")
    def close_modal_about_ingredient(self):
        self.click_to_element(KonstruktorLocators.CLOSE_MODAL_ABOUT_INGREDIENT)
        modal = self.find_element_with_wait(KonstruktorLocators.MODAL_ABOUT_INGREDIENT)
        classes = modal.get_attribute("class")
        return ("Modal_modal_opened__3ISw4" not in classes)
    
    @allure.step("Добавить ингредиент")
    def add_ingredient(self):
        self.find_element_with_wait(KonstruktorLocators.TITLE_BUILD_BURGER)
        self.my_drag_and_drop(KonstruktorLocators.CLICK_TO_INGREDIENTS, KonstruktorLocators.KONSTRUKTOR_BURGER)
        self.find_element_with_wait(KonstruktorLocators.COUNT_INGREDIENTS)
        value = self.get_text_from_element(KonstruktorLocators.COUNT_INGREDIENTS)
        return value
    
    @allure.step("Оформить заказ")
    def create_order(self):
        self.click_to_element(KonstruktorLocators.BUTTON_CREATE_ORDER)
        self.wait_until_is_visibility(KonstruktorLocators.ID_ORDER, default_text_order)
        value = self.get_text_from_element(KonstruktorLocators.ID_ORDER)
        return value

    