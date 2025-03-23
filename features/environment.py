from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def before_all(context):
    # Configuración del WebDriver
    context.driver = webdriver.Chrome(service=Service(r"C:\Users\Usuario\env-pinApp\Scripts\chromedriver.exe"))
    print("Iniciando el WebDriver...")


def after_all(context):
    # Cerrar el WebDriver después de que termine la ejecución
    context.driver.quit()
