from features.pageObjects.casosExitoPage.casosExitosPage import CasosDeExitoPage
from features.pageObjects.inicioPage.inicioPage import HomePinApp
from features.pageObjects.footerPage.footerPage import FooterPage
from behave import given, when, step


@given('El usuario ingresa a PinApp')
def step_impl(context):
    # Usa el método open_pin_app para abrir la URL
    home_pin_app = HomePinApp(context.driver)
    home_pin_app.open_pin_app()


@when('El usuario hace click en el menu')
def step_impl(context):
    try:
        home_pin_app = HomePinApp(context.driver)
        home_pin_app.click_menu()
    except Exception as e:
        assert False, f'Error al seleccionar el menu, {e}'


@step('el usuario selecciona la opcion {opcion_menu}')
def step_impl(context, opcion_menu):
    try:
        home_pin_app = HomePinApp(context.driver)
        home_pin_app.click_opcion_menu(opcion_menu)
    except Exception as e:
        assert False, f'Error al seleccionar la opcion de menu, {e}'


@step('el usuario valida la pantalla de casos de exito')
def step_impl(context):
    try:
        casos_exito_page = CasosDeExitoPage(context.driver)
        casos_exito_page.validar_casos_de_exito_page()
    except Exception as e:
        assert False, f'Error al validar los elementos de la page, {e}'


@step('el usuario valida la presencia de los elementos del footer')
def step_impl(context):
    try:
        footer_page = FooterPage(context.driver)
        footer_page.validar_presencia_elementos_footer()
    except Exception as e:
        assert False, f'Error al validar los elementos de la page, {e}'


@step('el usuario valida la redireccion a las redes sociales')
def step_impl(context):
    try:
        footer_page = FooterPage(context.driver)
        footer_page.validar_redireccion_redes_sociales()
    except Exception as e:
        assert False, f'Error al validar los elementos de la page, {e}'
