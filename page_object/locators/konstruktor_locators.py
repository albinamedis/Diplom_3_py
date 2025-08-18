from selenium.webdriver.common.by import By

class KonstruktorLocators: 

    TITLE_BUILD_BURGER = [By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10' and text()='Соберите бургер']"]
    CLICK_TO_INGREDIENTS = [By.XPATH, "//ul[1]//img[@class='BurgerIngredient_ingredient__image__3e-07 ml-4 mr-4'][1]"]
    TITLE_ABOUT_INGREDIENT = [By.XPATH, "//h2[contains(@class, 'Modal_modal__title_modified__3Hjkd') and text()='Детали ингредиента']"]
    CLOSE_MODAL_ABOUT_INGREDIENT = [By.XPATH, "//div[@class='Modal_modal__contentBox__sCy8X pt-10 pb-15']/parent::div/button"]
    MODAL_ABOUT_INGREDIENT = [By.XPATH, "//div[@class='Modal_modal__contentBox__sCy8X pt-10 pb-15']/ancestor::section"]
    KONSTRUKTOR_BURGER = [By.CLASS_NAME, "BurgerConstructor_basket__list__l9dp_"]
    COUNT_INGREDIENTS = [By.XPATH, "//ul[1]//img[@class='BurgerIngredient_ingredient__image__3e-07 ml-4 mr-4'][1]/parent::a//p[@class='counter_counter__num__3nue1']"]
    BUTTON_CREATE_ORDER = [By.XPATH, "//button[text()='Оформить заказ']"]
    ID_ORDER = [By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq')]"]
    BUTTON_CLOSE_NEW_ORDER = [By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"]

    