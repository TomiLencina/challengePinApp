from selenium.webdriver.common.by import By
from features.pageObjects.basePage import *


class HomePinApp(Reusable):
    def __init__(self, driver):
        super().__init__(driver)

        # URL de la página
        self.url = "https://pinapp.tech/"

        # BOTONES
        self.menu = Locator(By.XPATH, "//button[@aria-label='menu']")
        self.inicio = Locator(By.XPATH, "//ul/div//div/span/a[contains(text(),'Inicio')]")
        self.nosotros = Locator(By.XPATH, "//ul/div//div/span/a[contains(text(),'Nosotros')]")
        self.servicios = Locator(By.XPATH, "//ul/div//div/span/a[contains(text(),'Servicios')]")
        self.casos_de_exitos = Locator(By.XPATH, "//ul/div//div/span/a[contains(text(),'Casos')]")


    def open_pin_app(self):
        self.driver.get(self.url)  # Método para abrir la URL de la aplicación

    def click_menu(self):
        super().elemento_cargado_en_web(self.menu)
        super().perform_action_on_element(self.menu, 'click')

    def click_opcion_menu(self, opcion):
        opcion_menu = opcion.lower()

        if opcion_menu == 'inicio':
            super().elemento_cargado_en_web(self.inicio)
            super().perform_action_on_element(self.inicio, 'click')

        elif opcion_menu == 'nosotros':
            super().elemento_cargado_en_web(self.nosotros)
            super().perform_action_on_element(self.nosotros, 'click')

        elif opcion_menu == 'servicios':
            super().elemento_cargado_en_web(self.servicios)
            super().perform_action_on_element(self.servicios, 'click')

        elif opcion_menu == 'casos de exito':
            super().elemento_cargado_en_web(self.casos_de_exitos)
            super().perform_action_on_element(self.casos_de_exitos, 'click')
        else:
            raise 'Ninguna opcion es valida'
