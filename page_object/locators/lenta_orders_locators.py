from selenium.webdriver.common.by import By

class LentaOrdersLocators: 

    TITLE_LENTA_ORDERS = [By.XPATH, "//h1[@class='text text_type_main-large mt-10 mb-5' and text()='Лента заказов']"]
    CLICK_FOR_ORDER = [By.XPATH, "//h2[@class='text text_type_main-medium mb-2'][1]"]
    FORM_ABOUT_ORDER = [By.XPATH, "//p[@class='text text_type_main-medium mb-8']"]
    LIST_ORDERS = [By.XPATH, "//p[@class='text text_type_digits-default']"]
    ALL_TIME_ORDERS = [By.XPATH, "//p[text()='Выполнено за все время:']/parent::div/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"]
    TODAY_ORDERS = [By.XPATH, "//p[text()='Выполнено за сегодня:']/parent::div/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"]
    OVERLAY = [By.CSS_SELECTOR, "div.Modal_modal_overlay__x2ZCr"]
    ORDER_IN_WORK = [By.XPATH, "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li"]