import requests
import random
import allure
import string
from data import BASE_URL

class AuthMethods:

    @allure.step("Регистрация нового пользователя")
    def post_register(self, params):
        response = requests.post(f"{BASE_URL}register", data = params)
        return response
    
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    
    @allure.step("Удалить пользователя")
    def delete_user(self, token):
        response = requests.delete(f"{BASE_URL}user", headers={'Authorization': token})
        return response
    
    @allure.step("Авторизация пользователя")
    def post_login(self, params):
        response = requests.post(f"{BASE_URL}login", data = params)
        return response