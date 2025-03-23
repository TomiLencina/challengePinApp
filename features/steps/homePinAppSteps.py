import time

from behave import given, when, step, then
from features.pageObjects.inicioPage.inicioPage import HomePinApp  # Importa la clase HomePinApp
from features.pageObjects.casosExitoPage.casosExitosPage import CasosDeExitoPage

@given('El usuario ingresa a PinApp')
def step_impl(context):
    # Usa el método open_pin_app para abrir la URL
    home_pin_app = HomePinApp(context.driver)
    home_pin_app.open_pin_app()


@when('El usuario hace click en el menu')
def step_impl(context):
    home_pin_app = HomePinApp(context.driver)
    home_pin_app.click_menu()


@step('el usuario selecciona la opcion {opcion_menu}')
def step_impl(context, opcion_menu):
    home_pin_app = HomePinApp(context.driver)
    home_pin_app.click_opcion_menu(opcion_menu)


@step('el usuario valida la pantalla de casos de exito')
def step_impl(context):
    try:
        casos_exito_page = CasosDeExitoPage(context.driver)
        casos_exito_page.validar_casos_de_exito_page()
    except Exception as e:
        assert False, f'Error al validar los elementos de la page, {e}'

