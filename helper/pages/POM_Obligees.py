from selenium.webdriver.common.by import By

class Principals:
    select_id = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/beneficiarios/beneficiarios-agregar/div/sa-widgets-grid/section/form/article/panel-widget[1]/div/sa-widget/div/div[2]/div/form/form-search-identificacion/div/div/form-input-select/div/div/div/div/div/div/select")
    id_number_general = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/beneficiarios/beneficiarios-agregar/div/sa-widgets-grid/section/form/article/panel-widget[1]/div/sa-widget/div/div[2]/div/form/form-search-identificacion/div/div/form-input-text/div/div[1]/div/div/div/div/input")
    select_legal_person_type =  (By.XPATH, "/html/body/app-root/app-main-layout/div/views/beneficiarios/beneficiarios-agregar/div/sa-widgets-grid/section/form/article/panel-widget[1]/div/sa-widget/div/div[2]/div/form/form-tipo-persona/div/div/form-input-select/div/div/div/div/div/div/select")
    name_general = (By.XPATH, "//input[contains(@placeholder, 'First Name')]")
    last_name_general = (By.XPATH, "//input[contains(@placeholder, 'Last Name')]")
    company_type_general = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/beneficiarios/beneficiarios-agregar/div/sa-widgets-grid/section/form/article/panel-widget[1]/div/sa-widget/div/div[2]/div/form/form-empresa/div/div/form-input-select/div/div/div/div/div/div/select")
    type = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/beneficiarios/beneficiarios-agregar/div/sa-widgets-grid/section/form/article/panel-widget[2]/div/sa-widget/div/div[2]/div/panel-add-items/div/div[2]/fieldset/form/form-location-utx/div/form/form-input-select/div/div/div/div/div/div/select")
    address_number = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/beneficiarios/beneficiarios-agregar/div/sa-widgets-grid/section/form/article/panel-widget[2]/div/sa-widget/div/div[2]/div/panel-add-items/div/div[2]/fieldset/form/form-location-utx/div/form/form-input-text[1]/div/div[1]/div/div/div/div/input")
    address_street = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/beneficiarios/beneficiarios-agregar/div/sa-widgets-grid/section/form/article/panel-widget[2]/div/sa-widget/div/div[2]/div/panel-add-items/div/div[2]/fieldset/form/form-location-utx/div/form/form-input-text[2]/div/div[1]/div/div/div/div/input")
    address_street2 = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/beneficiarios/beneficiarios-agregar/div/sa-widgets-grid/section/form/article/panel-widget[2]/div/sa-widget/div/div[2]/div/panel-add-items/div/div[2]/fieldset/form/form-location-utx/div/form/form-input-text[3]/div/div[1]/div/div/div/div/input")
    zip_code_pre = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/beneficiarios/beneficiarios-agregar/div/sa-widgets-grid/section/form/article/panel-widget[2]/div/sa-widget/div/div[2]/div/panel-add-items/div/div[2]/fieldset/form/form-location-utx/div/form/form-zipcode-utx/div/form/form-input-text[2]/div/div[1]/div/div/div/div/input")
    state_pre = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/beneficiarios/beneficiarios-agregar/div/sa-widgets-grid/section/form/article/panel-widget[2]/div/sa-widget/div/div[2]/div/panel-add-items/div/div[2]/fieldset/form/form-location-utx/div/form/form-zipcode-utx/div/form/form-input-select2/div/div/div/div[1]/span/span[1]/span")
    state = (By.XPATH, "/html/body/span/span/span[1]/input")
    city_pre = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/beneficiarios/beneficiarios-agregar/div/sa-widgets-grid/section/form/article/panel-widget[2]/div/sa-widget/div/div[2]/div/panel-add-items/div/div[2]/fieldset/form/form-location-utx/div/form/form-zipcode-utx/div/form/form-input-text[1]/div/div[1]/div/div/div/div/input")

    btn_add = (By.XPATH,
               "/html/body/app-root/app-main-layout/div/views/beneficiarios/beneficiarios-agregar/div/sa-widgets-grid/section/form/article/register-tools/div/a")
    btn_save = (By.XPATH, "//button[contains(text(), 'Save')]")
    btn_yes = (By.XPATH, "")


class Home:
    table = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/beneficiarios/beneficiarios-listar/div/sa-widgets-grid/section/div/article/panel-widget/div/sa-widget/div/div[2]/div/panel-table/div/div[2]/sa-datatable/div/table/tbody/tr")
    select_type = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/beneficiarios/beneficiarios-listar/div/sa-widgets-grid/section/div/article/panel-search-mantenimiento/div/panel-widget/div/sa-widget/div/div[2]/div/form/form-search-identificacion/div/div/form-input-select/div/div/div/div/div/div/select")
    id_number_general = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/beneficiarios/beneficiarios-listar/div/sa-widgets-grid/section/div/article/panel-search-mantenimiento/div/panel-widget/div/sa-widget/div/div[2]/div/form/form-search-identificacion/div/div/form-input-text/div/div[1]/div/div/div/div/input")
