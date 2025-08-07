from time import sleep

from behave import *
import os

from selenium.webdriver.common.by import By

class ThenDefinition:

    @then(u'Valido que exista un resultado')
    def step_impl(context):
        page = context.elements.get_url()
        if "tomadores" in page:
            context.id_principals = context.idssn
        elif "intermediario" in page:
            context.id_broker = context.idssn
        elif "beneficiarios" in page:
            context.id_obligees = context.idssn
        sleep(3)
        context.elements.scroll_to(element_by=(context.selector.table))
        cantidad = context.elements._find_elements(element_by=(context.selector.table))
        assert cantidad is not None, "No se creo el Broker"
