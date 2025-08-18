import requests
import allure
from data import BASE_URL

class AuthMethods:

    @allure.step("Регистрация нового пользователя")
    def post_register(self, params):
        response = requests.post(f"{BASE_URL}api/auth/register", data = params)
        return response
    
    @allure.step("Удалить пользователя")
    def delete_user(self, token):
        response = requests.delete(f"{BASE_URL}api/auth/user", headers={'Authorization': token})
        return response
    
    @allure.step("Авторизация пользователя")
    def post_login(self, params):
        response = requests.post(f"{BASE_URL}api/auth/login", data = params)
        return response