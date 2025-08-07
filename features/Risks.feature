@regresion @risks
Feature: Gestión de riesgos

  @economic_group
  Scenario: Test - Validar la creación de un grupo económico
    Given Estoy en el ingreso al portal sin loguearme
    When Me logueo con las credenciales "admin"
    And Despliego la seccion "Risk Management"
    And Me dirijo a la seccion "Economic Groups"


  @create_minute
  Scenario: Test - Validar la creación de una minuta
    Given Estoy en el ingreso al portal sin loguearme
    When Me logueo con las credenciales "admin"
    And Despliego la seccion "Risk Management"
    And Me dirijo a la seccion "Approval Minutes"

  @edit_minute
  Scenario: Test - Validar la edicion de una minuta
    Given Estoy en el ingreso al portal sin loguearme
    When Me logueo con las credenciales "admin"
    And Despliego la seccion "Risk Management"
    And Me dirijo a la seccion "Approval Minutes"

  @send_to_approbe_minute
  Scenario: Test - Validar enviar a aprobar minuta
    Given Estoy en el ingreso al portal sin loguearme
    When Me logueo con las credenciales "admin"
    And Despliego la seccion "Risk Management"
    And Me dirijo a la seccion "Approval Minutes"

  @approbe_minute
  Scenario: Test - Validar aprobar minuta
    Given Estoy en el ingreso al portal sin loguearme
    When Me logueo con las credenciales "admin"
    And Despliego la seccion "Risk Management"
    And Me dirijo a la seccion "Approval Minutes"
