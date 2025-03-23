import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from behave.__main__ import main as behave_main
import os

"""no se usa 
def run_tests(tag=None):
    # Asegúrate de que la ruta de las features sea correcta
    features_dir = os.path.join(os.getcwd(), 'features')

    # Aquí construimos los argumentos para ejecutar Behave con Allure
    args = [
        features_dir,  # Directorio donde están los archivos .feature
        '--tags', f'@{tag}' if tag else '',  # Filtra por el tag especificado
        '-f', 'allure_behave.formatter:AllureFormatter',  # Usa el formateador de Allure
        '-o', 'reports/allure-results',  # Directorio de salida donde se guardarán los archivos de resultados de Allure
    ]

    # Llama a Behave con los argumentos configurados
    behave_main.main(args)
"""

if __name__ == "__main__":
    tag = "test"  # Cambia esto al tag que quieres ejecutar, por ejemplo, "@test"
    #run_tests(tag)
    behave_main('features --tags=@test -f allure_behave.formatter:AllureFormatter -o report/')
