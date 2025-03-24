from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import allure
import time


def before_all(context):
    # Configuración del WebDriver
    context.driver = webdriver.Chrome(service=Service(r"C:\Users\Usuario\env-pinApp\Scripts\chromedriver.exe"))
    print("Iniciando el WebDriver...")


def after_scenario(context, scenario):
    # Generar un nombre único para la captura usando el timestamp
    timestamp = time.time()  # Genera un timestamp único
    screenshot_path = f"screenshot_{int(timestamp)}.png"  # Nombre único para la captura

    # Capturar una captura de pantalla después de cada escenario (en el `then` final)
    context.driver.get_screenshot_as_file(screenshot_path)

    # Agregar la captura de pantalla al reporte de Allure solo en el escenario final
    with open(screenshot_path, "rb") as f:
        allure.attach(f.read(), name=f"screenshot_{int(timestamp)}", attachment_type=allure.attachment_type.PNG)

    print(f"Captura de pantalla tomada para el escenario: {screenshot_path}")

def after_all(context):
    # Cerrar el WebDriver después de que termine la ejecución
    context.driver.quit()
