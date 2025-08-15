import allure 
import pytest
from data import default_text_order, count_ingredients


class TestMainFunction:

    @allure.title('Проверка перехода в раздел Конструктор')
    def test_go_to_konstruktor(self, menu_page):
        assert menu_page.open_page_by_konstruktor() == True

    @allure.title('Проверка перехода в раздел Лента заказов')
    def test_go_to_lenta_orders(self, menu_page):
        assert menu_page.open_page_by_lenta_orders() == True

    @allure.title('Проверка открытия окна с информацией об ингредиенте')
    def test_open_info_about_ingredients(self, konstruktor_page):
        assert konstruktor_page.open_modal_about_ingredient() == True

    @allure.title('Проверка закрытия окна с информацией об ингредиенте')
    def test_close_info_about_ingredients(self, konstruktor_page):
        konstruktor_page.open_modal_about_ingredient()
        assert konstruktor_page.close_modal_about_ingredient() == True

    @allure.title('Проверка добавления ингредиента в заказ')
    def test_add_ingredients(self, konstruktor_page):
        konstruktor_page.add_ingredient()
        assert konstruktor_page.add_ingredient() == count_ingredients

    @allure.title('Проверка оформления заказа')
    def test_create_order(self, auth_user, konstruktor_page):
        menu_page = auth_user
        konstruktor_page.add_ingredient()
        value = konstruktor_page.create_order()
        assert int(value) > default_text_order
