from selenium.webdriver.common.by import By


class Principals:
    digit_code = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/solicitudes/solicitudes-agregar/solicitudes-agregar-garantia/div/sa-widgets-grid/section/form/article/panel-widget[1]/div/sa-widget/div/div[2]/div/form/panel-classification-code/div/div/div/form-input-select[1]/div/div/div/div/div/div/select")
    select_class = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/solicitudes/solicitudes-agregar/solicitudes-agregar-garantia/div/sa-widgets-grid/section/form/article/panel-widget[1]/div/sa-widget/div/div[2]/div/form/panel-classification-code/div/div/div/form-input-select[2]/div/div/div/div/div/div/select")
    second_digit_pre = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/solicitudes/solicitudes-agregar/solicitudes-agregar-garantia/div/sa-widgets-grid/section/form/article/panel-widget[1]/div/sa-widget/div/div[2]/div/form/panel-classification-code/div/div/div/form-input-select2/div/div/div/div[1]/span/span[1]/span")
    second_digit = (By.XPATH, "/html/body/span/span/span[1]/input")
    btn_add = (By.XPATH,
               "/html/body/app-root/app-main-layout/div/views/solicitudes/solicitudes-agregar/solicitudes-agregar-garantia/div/sa-widgets-grid/section/form/article/register-tools/div/a")
    btn_save = (By.XPATH, "//button[contains(text(), 'Save')]")
    btn_yes = (By.XPATH, "")
    text_comentario = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/solicitudes/solicitudes-agregar/solicitudes-agregar-garantia/div/sa-widgets-grid/section/form/article/panel-parrafo-poliza[1]/div/panel-widget/div/sa-widget/div/div[2]/div/form/form-input-textarea/div/div[1]/div/div/div/textarea")
    btn_finish_registration = (By.XPATH,
                               "//*[@id='widgets-grid']/form/article/register-tools/div/popover-content/div/div[3]/form/div[4]/button")


class Contractor:
    principal_pre = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/solicitudes/solicitudes-agregar/solicitudes-agregar-garantia/div/sa-widgets-grid/section/form/article/panel-info-intermediario-multiple/div/panel-widget/div/sa-widget/div/div[2]/div/form/form-search-nombre/div/div/div/div/div[2]/span/span[1]/span/span[1]/span")
    principal = (By.XPATH, "/html/body/span/span/span[1]/input")
    btn_add = (By.XPATH,
               "/html/body/app-root/app-main-layout/div/views/solicitudes/solicitudes-agregar/solicitudes-agregar-garantia/div/sa-widgets-grid/section/form/article/register-tools/div/a")
    btn_save = (By.XPATH, "//button[contains(text(), 'Save')]")
    btn_yes = (By.XPATH, "")


class Obligees:
    insured_pre = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/solicitudes/solicitudes-agregar/solicitudes-agregar-garantia/div/sa-widgets-grid/section/form/article/panel-info-beneficiarios/div/panel-widget/div/sa-widget/div/div[2]/div/panel-add-items/div/div[2]/fieldset/form/form-search-nombre/div/div/div/div/div[2]/span/span[1]/span")
    insured = (By.XPATH, "/html/body/span/span/span[1]/input")
    btn_add = (By.XPATH,
               "/html/body/app-root/app-main-layout/div/views/solicitudes/solicitudes-agregar/solicitudes-agregar-garantia/div/sa-widgets-grid/section/form/article/register-tools/div/a")
    btn_save = (By.XPATH, "//button[contains(text(), 'Save')]")
    btn_yes = (By.XPATH, "")


class Job:
    ECP = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/solicitudes/solicitudes-agregar/solicitudes-agregar-garantia/div/sa-widgets-grid/section/form/article/panel-widget[2]/div/sa-widget/div/div[2]/div/panel-info-cobertura/div/form/div[2]/form-input-amount/div/div/div/div/div/div/input")
    btn_add = (By.XPATH,
               "/html/body/app-root/app-main-layout/div/views/solicitudes/solicitudes-agregar/solicitudes-agregar-garantia/div/sa-widgets-grid/section/form/article/register-tools/div/a")
    btn_save = (By.XPATH, "//button[contains(text(), 'Save')]")
    btn_yes = (By.XPATH, "")
    message_number = (By.XPATH, "/html/body/div[4]/div/div[1]/p/i[2]")
    search_input = (By.XPATH, "//input[contains(@placeholder, 'No. of Request number')]")
    btn_finish_registration = (By.XPATH,
                               "//*[@id='widgets-grid']/form/article/register-tools/div/popover-content/div/div[3]/form/div[4]/button")
