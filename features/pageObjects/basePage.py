from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains


class Locator:
    def __init__(self, l_type, selector):
        self.l_type = l_type
        self.selector = selector


class Reusable:
    def __init__(self, driver):
        self.driver = driver

    def fluent_wait(self, condition):
        return WebDriverWait(self.driver, 5, poll_frequency=0.3, ignored_exceptions=[NoSuchElementException,
                                                                                     TimeoutException]).until(condition)

    def get_web_element(self, locator):
        return self.driver.find_element(locator.l_type, locator.selector)

    def elemento_cargado_en_web(self, locator) -> bool:
        return self.fluent_wait(ec.visibility_of_element_located((locator.l_type, locator.selector)))

    def esperar_clickeable(self, locator):
        try:
            self.fluent_wait(ec.element_to_be_clickable((locator.l_type, locator.selector)))
        except:
            assert False, f"Item no disponible para clickear -> {locator.selector}"

    def perform_action_on_element(self, locator, action, text=""):
        try:
            action = action.lower()

            if action == "click":
                self.esperar_clickeable(locator)
                self.get_web_element(locator).click()

            elif action == "type":
                self.elemento_cargado_en_web(locator)
                self.get_web_element(locator).send_keys(text)

                if text == "enter":
                    self.get_web_element(locator).send_keys(Keys.ENTER)

            elif action == "clear":
                self.elemento_cargado_en_web(locator)
                self.get_web_element(locator).clear()

            elif action == "scroll":
                self.driver.execute_script("arguments[0].scrollIntoView(true)", self.get_web_element(locator))

        except ElementClickInterceptedException:
            assert False, f"No se puede hacer click en el elemento {locator.selector}, un elemento intercepta el click"

        except Exception as e:
            assert False, f"Ocurrió un error - Error: " + str(e)

    def obtener_url_actual(self):
        # Retorna la URL actual de la página
        return self.driver.current_url
