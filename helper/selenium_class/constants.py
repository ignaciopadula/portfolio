from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re

# keys module variables required by selenium action chains module
keys_selenium = {
    "ADD": Keys.ADD,
    "ALT": Keys.ALT,
    "ARROW_DOWN": Keys.ARROW_DOWN,
    "ARROW_LEFT": Keys.ARROW_LEFT,
    "ARROW_RIGHT": Keys.RIGHT,
    "ARROW_UP": Keys.ARROW_UP,
    "BACKSPACE": Keys.BACKSPACE,
    "BACK_SPACE": Keys.BACK_SPACE,
    "CANCEL": Keys.CANCEL,
    "CLEAR": Keys.CLEAR,
    "COMMAND": Keys.COMMAND,
    "CONTROL": Keys.CONTROL,
    "DECIMAL": Keys.DECIMAL,
    "DELETE": Keys.DELETE,
    "DIVIDE": Keys.DIVIDE,
    "DOWN": Keys.DOWN,
    "END": Keys.END,
    "ENTER": Keys.ENTER,
    "EQUALS": Keys.EQUALS,
    "ESCAPE": Keys.ESCAPE,
    "F1": Keys.F1,
    "F2": Keys.F2,
    "F3": Keys.F3,
    "F4": Keys.F4,
    "F5": Keys.F5,
    "F6": Keys.F6,
    "F7": Keys.F7,
    "F8": Keys.F8,
    "F9": Keys.F9,
    "F10": Keys.F10,
    "F11": Keys.F11,
    "F12": Keys.F12,
    "HELP": Keys.HELP,
    "HOME": Keys.HOME,
    "INSERT": Keys.INSERT,
    "LEFT": Keys.LEFT,
    "LEFT_ALT": Keys.LEFT_ALT,
    "LEFT_CONTROL": Keys.LEFT_CONTROL,
    "LEFT_SHIFT": Keys.LEFT_SHIFT,
    "META": Keys.META,
    "MULTIPLY": Keys.MULTIPLY,
    "NULL": Keys.NULL,
    "NUMPAD0": Keys.NUMPAD0,
    "NUMPAD1": Keys.NUMPAD1,
    "NUMPAD2": Keys.NUMPAD2,
    "NUMPAD3": Keys.NUMPAD3,
    "NUMPAD4": Keys.NUMPAD4,
    "NUMPAD5": Keys.NUMPAD5,
    "NUMPAD6": Keys.NUMPAD6,
    "NUMPAD7": Keys.NUMPAD7,
    "NUMPAD8": Keys.NUMPAD8,
    "NUMPAD9": Keys.NUMPAD9,
    "PAGE_DOWN": Keys.PAGE_DOWN,
    "PAGE_UP": Keys.PAGE_UP,
    "PAUSE": Keys.PAUSE,
    "RETURN": Keys.RETURN,
    "RIGHT": Keys.RIGHT,
    "SEMICOLON": Keys.SEMICOLON,
    "SEPARATOR": Keys.SEPARATOR,
    "SHIFT": Keys.SHIFT,
    "SPACE": Keys.SPACE,
    "SUBTRACT": Keys.SUBTRACT,
    "TAB": Keys.TAB
}

#Wait except variables required in class element  (helper/selenium_class/elements/Elements/wait_implicity())
wait_except = {
    "title_is": EC.title_is,
    "title_contains": EC.title_contains,
    "presence_of_element_located": EC.presence_of_element_located,
    "visibility_of_element_located": EC.visibility_of_element_located,
    "visibility_of": EC.visibility_of,
    "presence_of_all_elements_located": EC.presence_of_all_elements_located,
    "text_to_be_present_in_element": EC.text_to_be_present_in_element,
    "text_to_be_present_in_element_value": EC.text_to_be_present_in_element_value,
    "frame_to_be_available_and_switch_to_it": EC.frame_to_be_available_and_switch_to_it,
    "invisibility_of_element_located": EC.invisibility_of_element_located,
    "element_to_be_clickable": EC.element_to_be_clickable,
    "staleness_of": EC.staleness_of,
    "element_to_be_selected": EC.element_to_be_selected,
    "element_located_to_be_selected": EC.element_located_to_be_selected,
    "element_selection_state_to_be": EC.element_selection_state_to_be,
    "element_located_selection_state_to_be": EC.element_located_selection_state_to_be,
    "alert_is_present": EC.alert_is_present
}

# By module variables required in class element  (helper/selenium_class/elements/Elements/wait_implicity())
by_var = {
    "class_name": By.CLASS_NAME,
    "css_selector": By.CSS_SELECTOR,
    "id": By.ID,
    "link_text": By.LINK_TEXT,
    "name": By.NAME,
    "partial_link_text": By.PARTIAL_LINK_TEXT,
    "tag_name": By.TAG_NAME,
    "xpath": By.XPATH
}

# Translate words in english from spanish
translate = {
    "elementos"     : "elements",
    "formularios"   : "forms",
    "eventos"       : "alerts",
    "widgets"       : "widgets",
    "interacciones" : "interactions",
    "ID"            : "id",
    "Nombre"        : "name",
    "Correo"        : "email",
    "País"          : "country"
}

# normalize strings to modify character without ´
def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
        
    return s


##################### Personal constants of ikso projects ############################
body_regex = re.compile('''
    ^(?!\.)                            # name may not begin with a dot
    (
      [-a-z0-9!\#$%&'*+/=?^_`{|}~]     # all legal characters except dot
      |
      (?<!\.)\.                        # single dots only
    )+
    (?<!\.)$                            # name may not end with a dot
    ''', re.VERBOSE | re.IGNORECASE)


domain_regex = re.compile('''
    (
      localhost
      |
      (
        [a-z0-9]
            # [sub]domain begins with alphanumeric
        (
          [-\w]*                         # alphanumeric, underscore, dot, hyphen
          [a-z0-9]                       # ending alphanumeric
        )?
      \.                               # ending dot
      )+
      [a-z]{2,}                        # TLD alpha-only
    )$
    ''', re.VERBOSE | re.IGNORECASE)


def is_valid_email(email):
    if not isinstance(email, str) or not email or '@' not in email:
        return False
    
    body, domain = email.rsplit('@', 1)

    match_body = body_regex.match(body)
    match_domain = domain_regex.match(domain)

    if not match_domain:
        # check for Internationalized Domain Names
        # see https://docs.python.org/2/library/codecs.html#module-encodings.idna
        try:
            domain_encoded = domain.encode('idna').decode('ascii')
        except UnicodeError:
            return False
        match_domain = domain_regex.match(domain_encoded)

    return (match_body is not None) and (match_domain is not None)


# Validate password in 
def validate_password(word):
    validate = True
    if not any(c.isupper() for c in word):
        validate = False

    if not any(c.islower() for c in word):
        validate = False

    if not any(c.isdigit() for c in word):
        validate = False

    return validate

def filter_identity_card(identity_card):
    caracteres = "1234567890k"
    rutx = ""
    for cambio in identity_card.lower():
        if cambio in caracteres:
            rutx += cambio
    return rutx

def validate_identity_card(identity_card):
    rfiltro = filter_identity_card(identity_card)
    rutx = str(rfiltro[0:len(rfiltro)-1])
    digito = str(rfiltro[-1])
    multiplo = 2
    total = 0
    for reverso in reversed(rutx):
        total += int(reverso) * multiplo
        if multiplo == 7:
            multiplo = 2
        else:
            multiplo += 1
        modulus = total % 11
        verificador = 11 - modulus
        if verificador == 10:
            div = "k"
        elif verificador == 11:
            div = "0"
        else:
            if verificador < 10:
                div = verificador
    if str(div) == str(digito):
        retorno = True
        
    else:
        retorno = False
    return retorno