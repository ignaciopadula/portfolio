import re
import time
from time import sleep
from behave import *
import os

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from helper.pages.POM_Actions import acciones_por_campo, acciones_input_por_campo
from helper.users import login
from helper.pages import POM_Login, POM_Obligees
from helper.pages import POM_Brokers
from helper.pages import POM_Principals

@when(u'Me logueo con las credenciales "{user}"')
def step_impl(context, user):
    #sleep(10)
    context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")),
                                     element_by=POM_Login.Login.txt_user).send_keys(
        login.get_user(user))
    context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")),
                                     element_by=POM_Login.Login.txt_password).send_keys(
        login.get_pass(user))
    context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")),
                                     element_by=POM_Login.Login.btn_login).click()

@when(u'Me dirijo a la seccion "{section}"')
def step_impl(context, section):
    context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")),
                                     element_by=(By.XPATH, "//a[contains(text(), '" + section + "')]")).click()
    if hasattr(context, "selector"):
        pass
    else:
        context.elements.get_selector()


@when(u'Despliego la seccion "{section}"')
def step_impl(context, section):
    context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")),
                                     element_by=(By.XPATH, "//span[contains(text(), '" + section + "')]")).click()

@when(u'Presiono el boton "{button}"')
def step_impl(context, button):
    try:
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")),
                                         element_by=(By.XPATH, "//span[contains(text(), '" + button + "')]")).click()
    except:
        sleep(1)
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")),
                                         element_by=(By.XPATH, "//button[contains(text(), '" + button + "')]")).click()

@when(u'Selecciono en "{campo}" "{opcion}" en "{seccion}"')
def step_impl(context, campo, opcion, seccion):
    context.selector = context.elements.get_selector(seccion)
    if campo in acciones_por_campo:
        acciones_por_campo[campo](context, opcion)

@when(u'Agrego un "{campo}" "{valor}" en "{seccion}"')
def step_impl(context, campo, valor, seccion):
    context.selector = context.elements.get_selector(seccion)

    if campo in acciones_input_por_campo:
        acciones_input_por_campo[campo](context, valor)

@when(u'Seteo "{campo}" en "{opcion}" en "{seccion}"')
def step_impl(context, campo, opcion, seccion):
    context.selector = context.elements.get_selector(seccion)

    if campo == "Expiration":
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.expiration_general).send_keys(
            str(opcion))
    if campo == "Date of Birth":
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.birthday_general).send_keys(
            str(opcion))
    if campo == "Broker":
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")),
                                         element_by=context.selector.broker_pre).click()
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")),
                                         element_by=context.selector.broker).send_keys(opcion)
        sleep(2)
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")),
                                         element_by=context.selector.broker).send_keys(Keys.ENTER)

@when(u'Presiono "{opcion}" en "Agency Licenses"')
def step_impl(context, opcion):
    context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")),
                                     element_by=context.selector.select_alaska).click()

@when(u'Presiono "{boton}"')
def step_impl(context, boton):
    try:
        if boton == "Add":
            context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")),
                                             element_by=context.selector.btn_add).click()
        if boton == "Save":
            context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")),
                                             element_by=context.selector.btn_save).click()

        if boton == "Yes" or boton == "Edit" or boton == "Print policy":
            context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")),
                                             element_by=(
                                                 (By.XPATH, "//button[contains(text(), '" + boton + "')]"))).click()
            sleep(5)
        if boton == "Visualize":
            sleep(3)
            context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")),
                                             element_by=(
                                                 (By.XPATH, "//a[contains(@title, '" + boton + "')]"))).click()
        if boton == "Finish Registration":
            context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")),
                                             element_by=context.selector.btn_finish_registration).click()
    except:
        assert False, "Boton " + boton + " no encontrado en el DOM"


@when(u'Selecciono "{opcion}" en "{seccion}"')
def step_impl(context, opcion, seccion):
    context.selector = context.elements.get_selector(seccion)
    context.elements.create_select_option_xpath(opcion, element_by=context.selector.type)

@when(u'Presiono el boton para buscar')
def step_impl(context):
    context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")),
                                     element_by=(
                                         (By.XPATH, "//button[contains(text(), 'Search')]"))).click()

@when(u'Selecciono "{opcion}"')
def step_impl(context, opcion):
    if context.selector == POM_Principals.Shareholders:
        context.selector = POM_Principals.Home
    elif context.selector == POM_Brokers.Principals:
        context.selector = POM_Brokers.Home
    elif context.selector == POM_Obligees.Principals:
        context.selector = POM_Obligees.Home
        context.elements.create_select_option_xpath(opcion, element_by=context.selector.select_type)

@when(u'Agrego un "ID Number"')
def step_impl(context):
    if hasattr(context, "idssn2"):
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")),
                                         element_by=context.selector.id_number_general).send_keys(
            str(context.idssn2))
    else:
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")),
                                         element_by=context.selector.id_number_general).send_keys(
            str(context.idssn))

@when(u'Guardo el numero de Request')
def step_impl(context):
    id_request = context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")),
                                         element_by=context.selector.message_number).text
    # Extrae el número con regex
    match = re.search(r'\d+', id_request)
    if match:
        numero = int(match.group())
        context.id_request = numero
    else:
        print("No se encontró ningún número.")

@when(u'Busco la solicitud previamente creada')
def step_impl(context):
    try:
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")),
                                     element_by=context.selector.search_input).send_keys(context.id_request)
    except:
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")),
                                     element_by=(By.XPATH, "//input[contains(@placeholder, 'Policy number')]")).send_keys(context.id_request)














