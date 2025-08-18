import allure 
import pytest


class TestLentaOrders:

    @allure.title('Открыть заказ на просмотр')
    def test_go_to_lenta_orders(self, menu_page, lenta_orders_page):
        menu_page.open_page_by_lenta_orders() 
        assert lenta_orders_page.open_modal_about_orders()

    @allure.title('Проверка отображения заказа пользователя в ленте заказов')
    def test_create_order(self, auth_user, menu_page, lenta_orders_page, konstruktor_page):
        menu_page = auth_user
         # создаем заказ
        konstruktor_page.add_ingredient()
        order_number = konstruktor_page.create_order()
        konstruktor_page.press_esc()
        lenta_orders_page.close_overlay()
        menu_page.open_page_by_lenta_orders()
        assert (f"#0{order_number}") in lenta_orders_page.find_order_user()

    @allure.title('Проверка, что счётчик Выполнено за всё время увеличивается')
    def test_get_count_all_time_orders(self, auth_user, menu_page, lenta_orders_page, konstruktor_page):
        # Открыть ленту с заказами
        menu_page = auth_user
        menu_page.open_page_by_lenta_orders() 
        orders_old = lenta_orders_page.get_count_all_time_orders().text
        menu_page.open_page_by_konstruktor()
        # Создать заказ
        konstruktor_page.add_ingredient()
        konstruktor_page.create_order()
        konstruktor_page.press_esc()
        # Открыть ленту с заказами
        lenta_orders_page.close_overlay()
        menu_page.open_page_by_lenta_orders()
        orders_new = lenta_orders_page.get_count_all_time_orders().text
        assert int(orders_old) < int(orders_new)

    @allure.title('Проверка, что счётчик Выполнено за сегодня увеличивается')
    def test_get_count_today_orders(self, auth_user, menu_page, lenta_orders_page, konstruktor_page):
        menu_page = auth_user
        # Открыть ленту с заказами
        menu_page.open_page_by_lenta_orders() 
        orders_old = lenta_orders_page.get_count_today_orders().text
        menu_page.open_page_by_konstruktor()
        # Создать заказ
        konstruktor_page.add_ingredient()
        konstruktor_page.create_order()
        konstruktor_page.press_esc()
        # Открыть ленту с заказами
        lenta_orders_page.close_overlay()
        menu_page.open_page_by_lenta_orders()
        orders_new = lenta_orders_page.get_count_today_orders().text
        assert int(orders_old) < int(orders_new)

    @allure.title('Проверка, что заказ отобразился в поле В работе')
    def test_get_order_in_work(self, auth_user, menu_page, lenta_orders_page, konstruktor_page):
        menu_page = auth_user
        menu_page.open_page_by_konstruktor()
        # Создать заказ
        konstruktor_page.add_ingredient()
        order_number = konstruktor_page.create_order()
        konstruktor_page.press_esc()
        # Открыть ленту с заказами
        lenta_orders_page.close_overlay()
        menu_page.open_page_by_lenta_orders()
        orders_new = lenta_orders_page.get_order_in_work(order_number)
        assert f"0{order_number}" == orders_new
      