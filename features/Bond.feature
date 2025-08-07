@regresion @bond @requests
Feature: Seguro garantia


  @create
  Scenario: Test - Validar la creación de una solucitud
    Given Estoy en el ingreso al portal sin loguearme
    When Me logueo con las credenciales "admin"
    When Despliego la seccion "Bond/Surety Management"
    And Me dirijo a la seccion "Requests"
    And Presiono el boton "New"
    And Selecciono en "1st Digit Code" "6 - Federal" en "General data"
    And Selecciono en "Class Description" "Bid or Proposal Bonds" en "General data"
    And Selecciono en "2nd & 3rd Digit Code" "0" en "General data"
    And Selecciono en "Principal" "174-54-3118" en "Contractor information"
    And Selecciono en "Insured" "155" en "Obligees Information"
    And Agrego un "Bid Contract Amount" "1000" en "Job description"
    And Presiono "Add"
    And Presiono "Save"
    And Presiono "Yes"
    And Guardo el numero de Request
    And Me dirijo a la seccion "Requests"
    And Busco la solicitud previamente creada
    And Presiono el boton para buscar

  @end
  Scenario: Test - Validar la finalizacion de una solucitud
    Given Estoy en el ingreso al portal sin loguearme
    When Me logueo con las credenciales "admin"
    When Despliego la seccion "Bond/Surety Management"
    And Me dirijo a la seccion "Requests"
    And Presiono el boton "New"
    And Selecciono en "1st Digit Code" "6 - Federal" en "General data"
    And Selecciono en "Class Description" "Bid or Proposal Bonds" en "General data"
    And Selecciono en "2nd & 3rd Digit Code" "0" en "General data"
    And Selecciono en "Principal" "174-54-3118" en "Contractor information"
    And Selecciono en "Insured" "155" en "Obligees Information"
    And Agrego un "Bid Contract Amount" "1000" en "Job description"
    And Presiono "Add"
    And Presiono "Save"
    And Presiono "Yes"
    And Guardo el numero de Request
    And Me dirijo a la seccion "Requests"
    And Busco la solicitud previamente creada
    And Presiono el boton para buscar
    And Presiono "Visualize"
    And Presiono "Add"
    And Presiono "Finish Registration"
    And Presiono "Yes"

  @edit
  Scenario: Test - Validar la edicion de una solucitud
    Given Estoy en el ingreso al portal sin loguearme
    When Me logueo con las credenciales "admin"
    When Despliego la seccion "Bond/Surety Management"
    And Me dirijo a la seccion "Requests"
    And Presiono el boton "New"
    And Selecciono en "1st Digit Code" "6 - Federal" en "General data"
    And Selecciono en "Class Description" "Bid or Proposal Bonds" en "General data"
    And Selecciono en "2nd & 3rd Digit Code" "0" en "General data"
    And Selecciono en "Principal" "174-54-3118" en "Contractor information"
    And Selecciono en "Insured" "155" en "Obligees Information"
    And Agrego un "Bid Contract Amount" "1000" en "Job description"
    And Presiono "Add"
    And Presiono "Save"
    And Presiono "Yes"
    And Guardo el numero de Request
    And Me dirijo a la seccion "Requests"
    And Busco la solicitud previamente creada
    And Presiono el boton para buscar
    And Presiono "Visualize"
    And Presiono "Add"
    And Presiono "Edit"
    And Agrego un "Comentario" "Prueba edit" en "General data"
    And Presiono "Add"
    And Presiono "Save"
    And Presiono "Yes"

 @Approve
  Scenario: Test - Aprobar una minuta
    Given Estoy en el ingreso al portal sin loguearme
    When Me logueo con las credenciales "admin"
    When Despliego la seccion "Bond/Surety Management"
    And Me dirijo a la seccion "Requests"
    And Presiono el boton "New"
    And Selecciono en "1st Digit Code" "6 - Federal" en "General data"
    And Selecciono en "Class Description" "Bid or Proposal Bonds" en "General data"
    And Selecciono en "2nd & 3rd Digit Code" "0" en "General data"
    And Selecciono en "Principal" "174-54-3118" en "Contractor information"
    And Selecciono en "Insured" "155" en "Obligees Information"
    And Agrego un "Bid Contract Amount" "1000" en "Job description"
    And Presiono "Add"
    And Presiono "Save"
    And Presiono "Yes"
    And Guardo el numero de Request
    And Me dirijo a la seccion "Requests"
    And Busco la solicitud previamente creada
    And Presiono el boton para buscar
    And Presiono "Visualize"
    And Presiono "Add"
    And Presiono "Edit"
    And Agrego un "Comentario" "Prueba edit" en "General data"
    And Presiono "Add"
    And Presiono "Save"
    And Presiono "Yes"
    And Presiono "Add"
    And Presiono "Finish Registration"
    And Presiono "Yes"

    @EndProposal
  Scenario: Test - Finalizar propuesta
    Given Estoy en el ingreso al portal sin loguearme
    When Me logueo con las credenciales "admin"
    When Despliego la seccion "Bond/Surety Management"
    And Me dirijo a la seccion "Requests"
    And Presiono el boton "New"
    And Selecciono en "1st Digit Code" "6 - Federal" en "General data"
    And Selecciono en "Class Description" "Bid or Proposal Bonds" en "General data"
    And Selecciono en "2nd & 3rd Digit Code" "0" en "General data"
    And Selecciono en "Principal" "174-54-3118" en "Contractor information"
    And Selecciono en "Insured" "155" en "Obligees Information"
    And Agrego un "Bid Contract Amount" "1000" en "Job description"
    And Presiono "Add"
    And Presiono "Save"
    And Presiono "Yes"
    And Guardo el numero de Request
    And Me dirijo a la seccion "Requests"
    And Busco la solicitud previamente creada
    And Presiono el boton para buscar
    And Presiono "Visualize"
    And Presiono "Add"
    And Presiono "Edit"
    And Agrego un "Comentario" "Prueba edit" en "General data"
    And Presiono "Add"
    And Presiono "Save"
    And Presiono "Yes"
    And Presiono "Add"
    And Presiono "Finish Registration"
    And Presiono "Yes"
    And Presiono "Finish Proposal"
    And Presiono "Yes"


  @ValidateCreate
  Scenario: Test - Validar la creación de una solucitud
    Given Estoy en el ingreso al portal sin loguearme
    When Me logueo con las credenciales "admin"
    When Despliego la seccion "Bond/Surety Management"
    And Me dirijo a la seccion "Requests"
    And Presiono el boton "New"
    And Selecciono en "1st Digit Code" "6 - Federal" en "General data"
    And Selecciono en "Class Description" "Bid or Proposal Bonds" en "General data"
    And Selecciono en "2nd & 3rd Digit Code" "0" en "General data"
    And Selecciono en "Principal" "174-54-3118" en "Contractor information"
    And Selecciono en "Insured" "155" en "Obligees Information"
    And Agrego un "Bid Contract Amount" "1000" en "Job description"
    And Presiono "Add"
    And Presiono "Save"
    And Presiono "Yes"
    And Guardo el numero de Request
    And Me dirijo a la seccion "Policies/Certificates"
    And Busco la solicitud previamente creada
    And Presiono el boton para buscar

  @PrintPolicy
  Scenario: Test - Imprimir poliza
    Given Estoy en el ingreso al portal sin loguearme
    When Me logueo con las credenciales "admin"
    When Despliego la seccion "Bond/Surety Management"
    And Me dirijo a la seccion "Requests"
    And Presiono el boton "New"
    And Selecciono en "1st Digit Code" "6 - Federal" en "General data"
    And Selecciono en "Class Description" "Bid or Proposal Bonds" en "General data"
    And Selecciono en "2nd & 3rd Digit Code" "0" en "General data"
    And Selecciono en "Principal" "174-54-3118" en "Contractor information"
    And Selecciono en "Insured" "155" en "Obligees Information"
    And Agrego un "Bid Contract Amount" "1000" en "Job description"
    And Presiono "Add"
    And Presiono "Save"
    And Presiono "Yes"
    And Guardo el numero de Request
    And Me dirijo a la seccion "Policies/Certificates"
    And Busco la solicitud previamente creada
    And Presiono el boton para buscar
    And Presiono "Visualize"
    And Presiono "Print policy"
    And Presiono "Yes"

     @emision
  Scenario: Test - Movimiento de emision
    Given Estoy en el ingreso al portal sin loguearme
    When Me logueo con las credenciales "admin"
    And Despliego la seccion "Bond/Surety Management"
    And Me dirijo a la seccion "Requests"
    And Presiono el boton "New"
    And Selecciono en "1st Digit Code" "6 - Federal" en "General data"
    And Selecciono en "Class Description" "Bid or Proposal Bonds" en "General data"
    And Selecciono en "2nd & 3rd Digit Code" "0" en "General data"
    And Selecciono en "Principal" "174-54-3118" en "Contractor information"
    And Selecciono en "Insured" "155" en "Obligees Information"
    And Agrego un "Bid Contract Amount" "1000" en "Job description"
    And Presiono "Add"
    And Presiono "Save"
    And Presiono "Yes"
    And Guardo el numero de Request
    And Me dirijo a la seccion "Requests"
    And Busco la solicitud previamente creada
    And Presiono el boton para buscar
    Given Estoy en el ingreso al portal de Kamui sin loguearme
    When Me logueo con las credenciales "admin"