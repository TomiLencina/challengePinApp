Feature: Validar web PinApp

@test
Scenario Outline: El usuario ingresa a PinApp y realiza validaciones la page casos de exito
    Given El usuario ingresa a PinApp
    When  El usuario hace click en el menu
    And   el usuario selecciona la opcion <opcionMenu>
    Then  el usuario valida la pantalla de casos de exito
Examples:
  |opcionMenu    |
  #|Inicio        |
  #|Nosotros      |
  #|Servicios     |
  |Casos de exito|
