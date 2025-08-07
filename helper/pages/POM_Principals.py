from selenium.webdriver.common.by import By

class Principals:
    #General Search
    type = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-widget[2]/div/sa-widget/div/div[2]/div/panel-add-items/div/div[2]/fieldset/form/form-location-utx/div/form/form-input-select/div/div/div/div/div/div/select")

    # General Data
    select_id = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-widget[1]/div/sa-widget/div/div[2]/div/form/form-search-identificacion/div/div/form-input-select/div/div/div/div/div/div/select")
    select_legal_person_type = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-widget[1]/div/sa-widget/div/div[2]/div/form/form-tipo-persona/div/div/form-input-select[2]/div/div/div/div/div/div/select")
    name_general = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-widget[1]/div/sa-widget/div/div[2]/div/form/form-input-nombres/div/div/div[1]/form-input-text[1]/div/div[1]/div/div/div/div/input")
    last_name_general = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-widget[1]/div/sa-widget/div/div[2]/div/form/form-input-nombres/div/div/div[2]/form-input-text/div/div[1]/div/div/div/div/input")
    birthday_general = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-widget[1]/div/sa-widget/div/div[2]/div/form/div[1]/form-input-date/div/div/div/div/div/div/input")
    economic_activity_general_pre = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-widget[1]/div/sa-widget/div/div[2]/div/form/form-act-economica/div/div/div/div/div[2]/span/span[1]/span/span[1]")
    economic_activity_general = (By.XPATH, "/html/body/span/span/span[1]/input")
    phone_general = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-widget[1]/div/sa-widget/div/div[2]/div/form/div[3]/form-input-contacto/div/div[1]/form-input-text[1]/div/div[1]/div/div/div/div/input")
    email_general = (By.XPATH, "//input[contains(@placeholder, 'Email')]")
    agency_license_number_general = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/intermediarios/intermediarios-agregar/div/sa-widgets-grid/section/form/article/panel-widget[1]/div/sa-widget/div/div[2]/div/form/div[3]/form-input-text/div/div[1]/div/div/div/div/input")
    id_number_general = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-widget[1]/div/sa-widget/div/div[2]/div/form/form-search-identificacion/div/div/form-input-text/div/div[1]/div/div/div/div/input")
    expiration_general = (By.XPATH, "//input[contains(@placeholder, 'Expiration')]")
    nationality_general = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-widget[1]/div/sa-widget/div/div[2]/div/form/div[2]/div/form-input-select/div/div/div/div/div/div/select")


    # Addresses
    select_address = (By.XPATH,
            "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-widget[2]/div/sa-widget/div/div[2]/div/panel-add-items/div/div[2]/fieldset/form/form-location-utx/div/form/form-input-select/div/div/div/div/div/div/select")

    address_number = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-widget[2]/div/sa-widget/div/div[2]/div/panel-add-items/div/div[2]/fieldset/form/form-location-utx/div/form/form-input-text[1]/div/div[1]/div/div/div/div/input")
    address_street = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-widget[2]/div/sa-widget/div/div[2]/div/panel-add-items/div/div[2]/fieldset/form/form-location-utx/div/form/form-input-text[2]/div/div[1]/div/div/div/div/input")
    zip_code_pre = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-widget[2]/div/sa-widget/div/div[2]/div/panel-add-items/div/div[2]/fieldset/form/form-location-utx/div/form/form-zipcode-utx/div/form/form-input-text[2]/div/div[1]/div/div/div/div/input")
    zip_code = (By.XPATH, "/html/body/span/span/span[1]/input")
    state_pre = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-widget[2]/div/sa-widget/div/div[2]/div/panel-add-items/div/div[2]/fieldset/form/form-location-utx/div/form/form-zipcode-utx/div/form/form-input-select2[1]/div/div/div/div[1]/span/span[1]/span")
    state = (By.XPATH, "/html/body/span/span/span[1]/input")
    city_pre = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-widget[2]/div/sa-widget/div/div[2]/div/panel-add-items/div/div[2]/fieldset/form/form-location-utx/div/form/form-zipcode-utx/div/form/form-input-text[1]/div/div[1]/div/div/div/div/input")
    city = (By.XPATH, "/html/body/span/span/span[1]/input")

    # Broker
    broker_pre = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-info-canal-multiple/div/panel-widget/div/sa-widget/div/div[2]/div/panel-add-items/div/div[2]/fieldset/form/panel-info-canal/form/form-search-nombre/div/div/div/div/div[2]/span/span[1]/span")
    broker =  (By.XPATH, "/html/body/span/span/span[1]/input")

    # All
    btn_add = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/intermediarios/intermediarios-agregar/div/sa-widgets-grid/section/form/article/register-tools/div/a")
    btn_save = (By.XPATH, "//button[contains(text(), 'Save')]")
    btn_yes = (By.XPATH, "")

class Shareholders:

    # General Search
    type = (By.XPATH,
            "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-info-personas[1]/div/panel-widget/div/sa-widget/div/div[2]/div/div/panel-add-items/div/div[2]/fieldset/form/div[1]/form-input-persona/div/form-location-utx/div/form/form-input-select/div/div/div/div/div/div/select")

    # General Data
    select_id = (By.XPATH,
                 "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-info-personas[1]/div/panel-widget/div/sa-widget/div/div[2]/div/div/panel-add-items/div/div[2]/fieldset/form/div/form-input-persona/div/form-search-identificacion/div/div/form-input-select/div/div/div/div/div/div/select")
    select_legal_person_type = (By.XPATH,
                                "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-info-personas[1]/div/panel-widget/div/sa-widget/div/div[2]/div/div/panel-add-items/div/div[2]/fieldset/form/div/form-input-persona/div/div[5]/form-tipo-persona/div/div/form-input-select/div/div/div/div/div/div/select")
    name_general = (By.XPATH,
                    "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-info-personas[1]/div/panel-widget/div/sa-widget/div/div[2]/div/div/panel-add-items/div/div[2]/fieldset/form/div/form-input-persona/div/div[4]/form-input-nombres/div/div/div[1]/form-input-text[1]/div/div[1]/div/div/div/div/input")
    last_name_general = (By.XPATH,
                         "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-info-personas[1]/div/panel-widget/div/sa-widget/div/div[2]/div/div/panel-add-items/div/div[2]/fieldset/form/div/form-input-persona/div/div[4]/form-input-nombres/div/div/div[2]/form-input-text/div/div[1]/div/div/div/div/input")
    birthday_general = (By.XPATH,
                        "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-info-personas[1]/div/panel-widget/div/sa-widget/div/div[2]/div/div/panel-add-items/div/div[2]/fieldset/form/div/form-input-persona/div/div[6]/form-input-date/div/div/div/div/div/div/input")
    phone_general = (By.XPATH,
                     "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-info-personas[1]/div/panel-widget/div/sa-widget/div/div[2]/div/div/panel-add-items/div/div[2]/fieldset/form/div/form-input-persona/div/div[8]/form-input-text/div/div[1]/div/div/div/div/input")
    email_general = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-info-personas[1]/div/panel-widget/div/sa-widget/div/div[2]/div/div/panel-add-items/div/div[2]/fieldset/form/div/form-input-persona/div/div[10]/form-input-text/div/div[1]/div/div/div/div/input")
    agency_license_number_general = (By.XPATH,
                                     "/html/body/app-root/app-main-layout/div/views/intermediarios/intermediarios-agregar/div/sa-widgets-grid/section/form/article/panel-widget[1]/div/sa-widget/div/div[2]/div/form/div[3]/form-input-text/div/div[1]/div/div/div/div/input")
    id_number_general = (By.XPATH,
                         "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-info-personas[1]/div/panel-widget/div/sa-widget/div/div[2]/div/div/panel-add-items/div/div[2]/fieldset/form/div/form-input-persona/div/form-search-identificacion/div/div/form-input-text/div/div[1]/div/div/div/div/input")
    expiration_general = (By.XPATH, "//input[contains(@placeholder, 'Expiration')]")
    DBA_general = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-info-personas[1]/div/panel-widget/div/sa-widget/div/div[2]/div/div/panel-add-items/div/div[2]/fieldset/form/div/form-input-persona/div/div[7]/form-input-text/div/div[1]/div/div/div/div/input")
    nationality_general = (By.XPATH,
                           "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-widget[1]/div/sa-widget/div/div[2]/div/form/div[2]/div/form-input-select/div/div/div/div/div/div/select")

    # Addresses
    select_address = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-info-personas[1]/div/panel-widget/div/sa-widget/div/div[2]/div/div/panel-add-items/div/div[2]/fieldset/form/div[1]/form-input-persona/div/form-location-utx/div/form/form-input-select/div/div/div/div/div/div/select")
    address_number = (By.XPATH,
                      "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-info-personas[1]/div/panel-widget/div/sa-widget/div/div[2]/div/div/panel-add-items/div/div[2]/fieldset/form/div/form-input-persona/div/form-location-utx/div/form/form-input-text[1]/div/div[1]/div/div/div/div/input")
    address_street = (By.XPATH,
                      "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-info-personas[1]/div/panel-widget/div/sa-widget/div/div[2]/div/div/panel-add-items/div/div[2]/fieldset/form/div/form-input-persona/div/form-location-utx/div/form/form-input-text[2]/div/div[1]/div/div/div/div/input")
    zip_code_pre = (By.XPATH,
                    "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-info-personas[1]/div/panel-widget/div/sa-widget/div/div[2]/div/div/panel-add-items/div/div[2]/fieldset/form/div/form-input-persona/div/form-location-utx/div/form/form-zipcode-utx/div/form/form-input-text[2]/div/div[1]/div/div/div/div/input")
    zip_code = (By.XPATH, "/html/body/span/span/span[1]/input")
    state_pre = (By.XPATH,
                 "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-info-personas[1]/div/panel-widget/div/sa-widget/div/div[2]/div/div/panel-add-items/div/div[2]/fieldset/form/div/form-input-persona/div/form-location-utx/div/form/form-zipcode-utx/div/form/form-input-select2/div/div/div/div[1]/span/span[1]/span/span[1]")
    state = (By.XPATH, "/html/body/span/span/span[1]/input")
    city_pre = (By.XPATH,
                "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-info-personas[1]/div/panel-widget/div/sa-widget/div/div[2]/div/div/panel-add-items/div/div[2]/fieldset/form/div/form-input-persona/div/form-location-utx/div/form/form-zipcode-utx/div/form/form-input-text[1]/div/div[1]/div/div/div/div/input")
    city = (By.XPATH, "/html/body/span/span/span[1]/input")
    percentage_ownership = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-info-personas[1]/div/panel-widget/div/sa-widget/div/div[2]/div/div/panel-add-items/div/div[2]/fieldset/form/div/form-input-persona/div/div[12]/form-input-percentage/div/div/div/div/div/div/input[1]")

    # Economic group
    economic_group_pre = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/panel-info-grupo-economico/div/panel-widget/div/sa-widget/div/div[2]/div/form/div/div/div/div[2]/span/span[1]/span")
    economic_group = (By.XPATH, "/html/body/span/span/span[1]/input")
    # All
    btn_add = (By.XPATH,
               "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-agregar/div/sa-widgets-grid/section/form/article/register-tools/div/a")
    btn_save = (By.XPATH, "//button[contains(text(), 'Save')]")
    btn_yes = (By.XPATH, "")

class Home:
    select_type = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-listar/div/sa-widgets-grid/section/div/article/panel-search-mantenimiento/div/panel-widget/div/sa-widget/div/div[2]/div/form/form-search-identificacion/div/div/form-input-select/div/div/div/div/div/div/select")
    id_number_general = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-listar/div/sa-widgets-grid/section/div/article/panel-search-mantenimiento/div/panel-widget/div/sa-widget/div/div[2]/div/form/form-search-identificacion/div/div/form-input-text/div/div[1]/div/div/div/div/input")
    table = (By.XPATH, "/html/body/app-root/app-main-layout/div/views/tomadores/tomadores-listar/div/sa-widgets-grid/section/div/article/panel-widget/div/sa-widget/div/div[2]/div/panel-table/div/div[2]/sa-datatable/div/table/tbody/tr[1]")