from behave import *
import os
from time import sleep

from helper.pages import POM_Login
from helper.users import login


class GivenDefinition:
    @given(u'Estoy en el ingreso al portal sin loguearme')
    def step_impl(context):
        context.browser.get(os.getenv('URL_AMARU'))

    @given(u'Estoy en el ingreso al portal de Kamui sin loguearme')
    def step_impl(context):
        context.browser.get(os.getenv('URL_KAMUI'))
