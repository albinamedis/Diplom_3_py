from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    def find_elements_with_wait(self, locator):
        elements = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_all_elements_located(locator))
        return elements
    
    def find_element_with_text(self, locator, text):
        element = WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(locator))
        WebDriverWait(self.driver, 5).until(expected_conditions.text_to_be_present_in_element(locator, text))
        return element
    
    def wait_until_is_visibility(self, locator, text):
        try:
            WebDriverWait(self.driver, 15).until_not(expected_conditions.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            pass
    
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        element = self.find_element_with_wait(locator)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text
    
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def my_drag_and_drop(self, locator_from, locator_to):
        elem_from = self.find_element_with_wait(locator_from)
        elem_to = self.find_element_with_wait(locator_to)

        browser_name = self.driver.capabilities.get("browserName", "").lower()

        if browser_name == "firefox":
            # JS-имитация для Firefox
            js_code = """
            function createEvent(typeOfEvent) {
                var event = document.createEvent("CustomEvent");
                event.initCustomEvent(typeOfEvent, true, true, null);
                event.dataTransfer = {
                    data: {},
                    setData: function (key, value) { this.data[key] = value; },
                    getData: function (key) { return this.data[key]; }
                };
                return event;
            }

            function dispatchEvent(element, event, transferData) {
                if (transferData) {
                    event.dataTransfer = transferData;
                }
                if (element.dispatchEvent) {
                    element.dispatchEvent(event);
                } else if (element.fireEvent) {
                    element.fireEvent("on" + event.type, event);
                }
            }

            var dragStartEvent = createEvent('dragstart');
            dispatchEvent(arguments[0], dragStartEvent);
            var dropEvent = createEvent('drop');
            dispatchEvent(arguments[1], dropEvent, dragStartEvent.dataTransfer);
            var dragEndEvent = createEvent('dragend');
            dispatchEvent(arguments[0], dragEndEvent, dragStartEvent.dataTransfer);
            """
            self.driver.execute_script(js_code, elem_from, elem_to)
        else:
            # Обычный способ для Chrome и других браузеров
            actions = ActionChains(self.driver)
            actions.drag_and_drop(elem_from, elem_to).perform()

    def press_esc(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.ESCAPE).perform()

    def wait_for_modal_overlay_to_disappear(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(locator))
