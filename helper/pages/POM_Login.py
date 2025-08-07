from selenium.webdriver.common.by import By


class Login:
    txt_user = (By.XPATH, "//input[@name='username']")
    txt_password = (By.XPATH, "//input[@name='password']")
    btn_login = (By.XPATH, "//button[contains(text(), 'Ingresar')]")
    validate_logged = (By.XPATH, "//div[@title='Información de usuario']")





