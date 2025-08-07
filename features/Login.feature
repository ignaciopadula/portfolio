@login
Feature: Pruebas de Login

  @loginSuccess
  Scenario: Login exitoso
    Given Estar en la pantalla de inicio de sesion
    When Ingreso el usuario "admin"
    And Ingreso la pass para el user "admin_20240619_dev_SexJANCM6"
    And Uso el boton "Ingresar"
    Then Valido el texto "texto"