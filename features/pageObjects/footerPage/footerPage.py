import time

from selenium.webdriver.common.by import By
from features.pageObjects.basePage import *


class FooterPage(Reusable):
    def __init__(self, driver):
        super().__init__(driver)

        # TITULO ¿EN QUE TE PODEMOS AYUDAR?
        self.texto_footer = Locator(By.XPATH, "//div/span[contains(text(),'En qué te podemos ayudar')]")
        # CAJA DE TEXTO
        self.caja_texto = Locator(By.XPATH, "//div/input")
        # BOTON ENVIAR
        self.btn_enviar = Locator(By.XPATH, "//button/img")

        # CONTACTO
        self.mail = Locator(By.XPATH, "//div/span[contains(text(),'comunicaciones@pinapp.tech')]")
        self.telefono_uno = Locator(By.XPATH, "//div/span[contains(text(),'+5493516007243')]")
        self.telefono_dos = Locator(By.XPATH, "//div/span[contains(text(),'+51982414577')]")

        # REDES SOCIALES
        self.facebook = Locator(By.XPATH, "//div/a[1]/img/..")
        self.instagram = Locator(By.XPATH, "//div/a[2]/img/..")
        self.linkedin = Locator(By.XPATH, "//div/a[3]/img/..")

        # URL REDIRECCION REDES SOCIALES
        self.facebook_url = 'https://www.facebook.com/share/199CsQ2A6f/?mibextid=wwXIfr'
        self.instagram_url = 'https://www.instagram.com/pinapp_development/'
        self.linkedin_url = 'https://www.linkedin.com/company/pinapp-development/'


    def validar_presencia_elementos_footer(self):
        time.sleep(2)
        #SCROLLEAR HASTA EL FOOTER
        super().perform_action_on_element(self.texto_footer, 'scroll')

        # ESPERAR AL FOOTER
        super().esperar_clickeable(self.texto_footer)
        super().esperar_clickeable(self.mail)

        # TEXTO, INPUT Y BTN ENVIAR CONSULTA
        assert super().elemento_cargado_en_web(self.texto_footer)
        assert super().elemento_cargado_en_web(self.caja_texto)
        assert super().elemento_cargado_en_web(self.btn_enviar)

        # CONTACTO
        assert super().elemento_cargado_en_web(self.mail)
        assert super().elemento_cargado_en_web(self.telefono_uno)
        assert super().elemento_cargado_en_web(self.telefono_dos)

        # REDES
        super().esperar_clickeable(self.facebook)
        super().esperar_clickeable(self.instagram)
        super().esperar_clickeable(self.linkedin)
        assert super().elemento_cargado_en_web(self.facebook)
        assert super().elemento_cargado_en_web(self.instagram)
        assert super().elemento_cargado_en_web(self.linkedin)

    def validar_redireccion_redes_sociales(self):
        super().perform_action_on_element(self.texto_footer, 'scroll')

        url_redireccion_linkedin = super().get_href((self.linkedin.l_type, self.linkedin.selector))
        assert url_redireccion_linkedin == self.linkedin_url, f'No coinciden las URL, la URL esperada para linkedin' \
                                                              f' es {self.linkedin_url}'

        url_redireccion_instagram = super().get_href((self.instagram.l_type, self.instagram.selector))
        assert url_redireccion_instagram == self.instagram_url, f'No coinciden las URL, la URL esperada para instagram ' \
                                                                f'es  {self.instagram_url}'


        url_redireccion_facebook = super().get_href((self.facebook.l_type, self.facebook.selector))
        assert url_redireccion_facebook == self.facebook_url, f'No coinciden las URL, la URL esperada para facebook es' \
                                                              f' {self.facebook_url}'

