import allure 
import pytest


class TestPasswordRecovery:

    @allure.title('Перейти на страницу восстановления пароля')
    def test_go_to_forgot_password(self, menu_page, account_page):
        menu_page.open_page_by_sign()
        assert account_page.forgot_password()

    @allure.title('Ввести логин и восстановить пароль')
    def test_add_email_and_forgot_password(self, create_user, menu_page, account_page):
        token, email, password = create_user
        menu_page.open_page_by_sign()
        account_page.forgot_password()
        assert account_page.email_for_forgot_password(email)

    @allure.title('Проверка выделения поля пароля')
    def test_view_password(self, menu_page, account_page):
        menu_page.open_page_by_sign()
        assert "input_status_active" in account_page.email_view_password()
