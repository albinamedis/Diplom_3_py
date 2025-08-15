import allure 
import pytest


class TestAccount:

    @allure.title('Проверка перехода в раздел Личный кабинет')
    def test_go_to_profile(self, auth_user, menu_page):
        menu_page = auth_user
        assert menu_page.open_page_by_profile() == True

    @allure.title('Открыть Историю заказов')
    def test_go_to_history_orders(self, auth_user, menu_page, account_page):
        menu_page = auth_user
        menu_page.open_page_by_profile()
        account_page.open_page_by_history_orders()
        assert "/account/order-history" in account_page.open_page_by_history_orders()

    @allure.title('Выйти из личного кабинета')
    def test_logout_to_profile(self, auth_user, menu_page, account_page):
        menu_page = auth_user
        menu_page.open_page_by_profile()
        assert account_page.logout_account() == True
