from selenium.webdriver.common.by import By
from features.pageObjects.basePage import *


class CasosDeExitoPage(Reusable):
    def __init__(self, driver):
        super().__init__(driver)

        # URL de la página
        self.url = "https://pinapp.tech/casos"

        # TITULO
        self.titulo_casos_exito = Locator(By.XPATH, "(//div/span[contains(text(),'Casos')])[1]")

        # PRODUCTOS DE EXITOS
        self.agora_pay = Locator(By.XPATH, "(//div/span[contains(text(),'AGORA PAY')])[1]")
        self.agora_shop = Locator(By.XPATH, "(//div/span[contains(text(),'AGORA SHOP')])[1]")
        self.agora_ahorra_mas = Locator(By.XPATH, "(//div/span[contains(text(),'AGORA AHORRAMÁS')])[1]")
        self.agora_club = Locator(By.XPATH, "(//div/span[contains(text(),'AGORA CLUB')])[1]")


    def validar_casos_de_exito_page(self):
        # titulo
        super().elemento_cargado_en_web(self.titulo_casos_exito)
        # 4 productos
        assert super().elemento_cargado_en_web(self.agora_club)
        assert super().elemento_cargado_en_web(self.agora_shop)
        assert super().elemento_cargado_en_web(self.agora_pay)
        assert super().elemento_cargado_en_web(self.agora_ahorra_mas)
        # url
        url_actual = super().obtener_url_actual()
        assert url_actual == self.url, f'No coinciden las URL, la URL esperada es {self.url}'

