from time import sleep, time
import os
from selenium.webdriver.common.keys import Keys

# Diccionario que mapea cada campo a una función anónima que ejecuta la acción correspondiente
acciones_por_campo = {
    "ID Type": lambda context, opcion: (
        setattr(context, 'idssn2', getattr(context, 'idssn')) if hasattr(context, 'idssn') else (
            setattr(context, 'idssn', int(time())),
            sleep(2),
            context.elements.scroll_to(element_by=context.selector.select_id),
            context.elements.create_select_option_xpath(opcion, element_by=context.selector.select_id)
        )
    ),
    "Address Type": lambda context, opcion: (
        context.elements.scroll_to(element_by=context.selector.select_address),
        context.elements.create_select_option_xpath(opcion, element_by=context.selector.select_address)
    ),
    "State": lambda context, opcion: (
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.state_pre).click(),
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.state).send_keys(opcion),
        sleep(1),
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.state).send_keys(Keys.ENTER)
    ),
    "City": lambda context, opcion: (
        context.elements.scroll_to(element_by=context.selector.city_pre),
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.city_pre).click(),
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.city_pre).send_keys(opcion)
    ),
    "Legal Person Type": lambda context, opcion: (
        context.elements.create_select_option_xpath(opcion, element_by=context.selector.select_legal_person_type),
        sleep(2)
    ),
    "Nationality": lambda context, opcion: (
        context.elements.create_select_option_xpath(opcion, element_by=context.selector.nationality_general),
    ),
    "Economic Activity": lambda context, opcion: (
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.economic_activity_general_pre).click(),
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.economic_activity_general).send_keys(opcion),
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.economic_activity_general).send_keys(Keys.ENTER)
    ),
    "Economic Group": lambda context, opcion: (
        context.elements.scroll_to(element_by=context.selector.economic_group_pre),
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.economic_group_pre).click(),
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.economic_group).send_keys(opcion),
        sleep(1),
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.economic_group).send_keys(Keys.ENTER)
    ),
    "Company Type": lambda context, opcion: (
        context.elements.create_select_option_xpath(opcion, element_by=context.selector.company_type_general),
    ),
    "1st Digit Code": lambda context, opcion: (
        sleep(3),
        context.elements.create_select_option_xpath(opcion, element_by=context.selector.digit_code),
    ),
    "Class Description": lambda context, opcion: (
        context.elements.create_select_option_xpath(opcion, element_by=context.selector.select_class),
    ),
    "2nd & 3rd Digit Code": lambda context, opcion: (
        sleep(3),
        context.elements.scroll_to(element_by=context.selector.second_digit_pre),
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.second_digit_pre).click(),
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.second_digit).send_keys(opcion),
        sleep(3),
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.second_digit).send_keys(Keys.ENTER)
    ),
    "Principal": lambda context, opcion: (
        context.elements.scroll_to(element_by=context.selector.principal_pre),
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.principal_pre).click(),
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.principal).send_keys(opcion),
        sleep(3),
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.principal).send_keys(Keys.ENTER)
    ),
    "Insured": lambda context, opcion: (
        context.elements.scroll_to(element_by=context.selector.insured_pre),
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.insured_pre).click(),
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.insured).send_keys(opcion),
        sleep(1),
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.insured).send_keys(Keys.ENTER)
    ),
}


acciones_input_por_campo = {
    "Name": lambda context, valor=None: (
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.name_general).send_keys("Prueba"),
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.last_name_general).send_keys("Test")
    ),
    "Phone Number": lambda context, valor=None: (
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.phone_general).send_keys("1111111111")
    ),
    "Email": lambda context, valor=None: (
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.email_general).send_keys("test@prueba.com")
    ),
    "Agency License Number": lambda context, valor=None: (
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.agency_license_number_general).send_keys("123456")
    ),
    "ID Number": lambda context, valor=None: (
        context.elements.scroll_to(element_by=context.selector.id_number_general),
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.id_number_general).send_keys(str(context.idssn))
    ),
    "Address Number": lambda context, valor=None: (
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.address_number).click(),
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.address_number).send_keys("123")
    ),
    "Street Name": lambda context, valor=None: (
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.address_street).click(),
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.address_street).send_keys("Prueba")
    ),
    "Street Name 2": lambda context, valor=None: (
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.address_street2).click(),
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.address_street2).send_keys("Prueba dos")
    ),
    "ZIP Code": lambda context, valor=None: (
        context.elements.scroll_to(element_by=context.selector.zip_code_pre),
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.zip_code_pre).click(),
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.zip_code_pre).send_keys("555")
    ),
    "DBA": lambda context, valor=None: (
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.DBA_general).send_keys(str(context.idssn))
    ),
    "Range": lambda context, valor: (
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.range).send_keys(str(valor))
    ),
    "Percentage Ownership": lambda context, valor: (
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.percentage_ownership).send_keys(str(valor))
    ),
    "Bid Contract Amount": lambda context, valor: (
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.ECP).send_keys(str(valor))
    ),
    "Comentario": lambda context, valor: (
        context.elements._implicity_wait(int(os.getenv("IMPLICITY_WAIT")), element_by=context.selector.text_comentario).send_keys(str(valor))
    ),
}
