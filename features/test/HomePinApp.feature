Feature: Validar web PinApp
Background:
  Given El usuario ingresa a PinApp

@TC_CasosDeExito_001
Scenario Outline: El usuario ingresa a PinApp y realiza validaciones la page casos de exito
    When  El usuario hace click en el menu
    And   el usuario selecciona la opcion <opcionMenu>
    Then  el usuario valida la pantalla de casos de exito
Examples:
  |opcionMenu    |
  |Casos de exito|


@TC_Footer_001
Scenario Outline: El usuario ingresa a PinApp y realiza validaciones del footer en las pages que lo contienen
    When  El usuario hace click en el menu
    And   el usuario selecciona la opcion <opcionMenu>
    Then  el usuario valida la presencia de los elementos del footer
    And   el usuario valida la redireccion a las redes sociales
Examples:
  |opcionMenu    |
  |Nosotros      |
  |Servicios     |
  |Casos de exito|
