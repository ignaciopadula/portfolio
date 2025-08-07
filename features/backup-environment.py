import os
from platform import system
import shutil
import pathlib
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType
from dotenv import load_dotenv

from helper.selenium_class.elements import Elements
from helper.selenium_class.window_control import WindowControl
from helper.selenium_class.js_script import JsScript
from helper.selenium_class.keyboard_actions import KeyboardActions
from helper.selenium_class.mouse_actions import MouseActions
import json

global scenarios
scenarios = []


###################################### BEFORE ALL ######################################
def before_all(context):
    # If environment variables not exist, then load environment variables from file .env
    if os.getenv('BROWSER') is None:
        load_dotenv(dotenv_path='.env')
        assert os.getenv('BROWSER') is not None, "You must to define environment variables"

    if os.getenv('RELOADBROWSER') != "true":
    # context.type_execution = "selenium"
        execution_selenium(context)


###################################### AFTER ALL ######################################
def after_all(context):
    ## EXECUTION OF RERUN SCRIPT
    # text_command='behave -t "'
    text_command = 'behave -f allure_behave.formatter:AllureFormatter -o reporte -t "'
    counter = os.getenv("COUNT")
    total_repeat = os.getenv("REPEAT")
    if counter < total_repeat and os.getenv("EXECUTE_RERUN") == "true":
        i = 0
        scenarios_to_rerun = os.getenv("FAILED_SCENARIO_ARRAY").replace("'", '"')
        # print(scenarios_to_rerun)
        scenarios_to_rerun = json.loads(scenarios_to_rerun)
        # print("escenarios to re run ",scenarios_to_rerun)
        for scen in scenarios_to_rerun:
            if i == len(scenarios_to_rerun) - 1:
                text_command = text_command + ' @' + scen + '"'
            else:
                text_command = text_command + ' @' + scen + ','
            i += 1

        os.environ["COUNT"] = str(int(counter) + 1)
        os.system(text_command)

    if os.getenv('EXECUTE_ALLURE') == "true":
        name_os = system()

        if name_os == 'Windows':
            os.system(
                str(pathlib.Path().absolute()) + '\\helper\\vendor\\allure-2.13.6\\bin\\allure.bat generate reporte -o report -c')

            if os.getenv('CANTIDAD') == 'Multiple':
                os.environ['SAVE_REPORT_ALLURE'] = 'true'
            if os.getenv('SAVE_REPORT_ALLURE') == "false":
                folder = str(pathlib.Path().absolute()) + '\\reporte'
                shutil.rmtree(folder, ignore_errors=True)

            shutil.copy(str(pathlib.Path().absolute()) + "\\\\helper\\vendor\\report-assets\\index.html",
                        str(pathlib.Path().absolute()) + "\\report\\index.html")
            shutil.copy(str(pathlib.Path().absolute()) + "\\\\helper\\vendor\\report-assets\\app.js",
                        str(pathlib.Path().absolute()) + "\\report\\app.js")
            shutil.copy(str(pathlib.Path().absolute()) + "\\\\helper\\vendor\\report-assets\\styles.css",
                        str(pathlib.Path().absolute()) + "\\report\\styles.css")
            shutil.copy(str(pathlib.Path().absolute()) + "\\\\helper\\vendor\\report-assets\\executors.json",
                        str(pathlib.Path().absolute()) + "\\report\\widgets\\executors.json")
            # # Para modificar el reporte y abrirlo sin web-server
            os.system("python .\helper\combineWindows.py .\\report")
            # eliminar un archivo
            if os.getenv("CLEAN_EXTRAS_REPORT_ALLURE") == "true":
                os.remove(str(pathlib.Path().absolute()) + "\\report\\index.html")
                os.remove(str(pathlib.Path().absolute()) + "\\report\\app.js")
                os.remove(str(pathlib.Path().absolute()) + "\\report\\styles.css")
                os.remove(str(pathlib.Path().absolute()) + "\\report\\sinon-9.2.4.js")
                os.remove(str(pathlib.Path().absolute()) + "\\report\\server.js")
                os.remove(str(pathlib.Path().absolute()) + "\\report\\favicon.ico")
                shutil.rmtree(str(pathlib.Path().absolute()) + "\\report\\widgets", ignore_errors=True)
                shutil.rmtree(str(pathlib.Path().absolute()) + "\\report\\export", ignore_errors=True)
                shutil.rmtree(str(pathlib.Path().absolute()) + "\\report\\data", ignore_errors=True)
                shutil.rmtree(str(pathlib.Path().absolute()) + "\\report\\history", ignore_errors=True)
                shutil.rmtree(str(pathlib.Path().absolute()) + "\\report\\plugins", ignore_errors=True)


        elif name_os == 'Linux' or name_os == 'Darwin':
            os.system(
                str(pathlib.Path().absolute()) + '/helper/vendor/allure-2.13.6/bin/allure generate reporte -o report -c')

            if os.getenv('CANTIDAD') == 'Multiple':
                os.environ['SAVE_REPORT_ALLURE'] = 'true'
            if os.getenv('SAVE_REPORT_ALLURE') == "false":
                folder = str(pathlib.Path().absolute()) + '/reporte'
                shutil.rmtree(folder, ignore_errors=True)

            shutil.copy(str(pathlib.Path().absolute()) + "/helper/vendor/report-assets/index.html",
                        str(pathlib.Path().absolute()) + "/report/index.html")
            shutil.copy(str(pathlib.Path().absolute()) + "/helper/vendor/report-assets/app.js",
                        str(pathlib.Path().absolute()) + "/report/app.js")
            shutil.copy(str(pathlib.Path().absolute()) + "/helper/vendor/report-assets/styles.css",
                        str(pathlib.Path().absolute()) + "/report/styles.css")
            shutil.copy(str(pathlib.Path().absolute()) + "/helper/vendor/report-assets/executors.json",
                        str(pathlib.Path().absolute()) + "/report/widgets/executors.json")

            # Para modificar el reporte y abrirlo sin web-server
            os.system("python3 ./helper/combine.py ./report")
            if os.getenv("CLEAN_EXTRAS_REPORT_ALLURE") == "true":
                os.remove(str(pathlib.Path().absolute()) + "/report/index.html")
                os.remove(str(pathlib.Path().absolute()) + "/report/app.js")
                os.remove(str(pathlib.Path().absolute()) + "/report/styles.css")
                os.remove(str(pathlib.Path().absolute()) + "/report/sinon-9.2.4.js")
                os.remove(str(pathlib.Path().absolute()) + "/report/server.js")
                os.remove(str(pathlib.Path().absolute()) + "/report/favicon.ico")
                shutil.rmtree(str(pathlib.Path().absolute()) + "/report/widgets", ignore_errors=True)
                shutil.rmtree(str(pathlib.Path().absolute()) + "/report/export", ignore_errors=True)
                shutil.rmtree(str(pathlib.Path().absolute()) + "/report/data", ignore_errors=True)
                shutil.rmtree(str(pathlib.Path().absolute()) + "/report/history", ignore_errors=True)
                shutil.rmtree(str(pathlib.Path().absolute()) + "/report/plugins", ignore_errors=True)


###################################### AFTER FEATURE ######################################
def before_feature(context, feature):
    pass


###################################### AFTER FEATURE ######################################
def after_feature(context, feature):
    # Rellena la variable scenarios con todos los escenarios pertenecientes al feature
    if os.getenv("EXECUTE_RERUN") == "true":
        for sc in feature.scenarios:
            if sc.status == "failed":
                scenarios.append(sc.tags[0])
        os.environ["FAILED_SCENARIO_ARRAY"] = str(scenarios)
        print(os.getenv("FAILED_SCENARIO_ARRAY"))


###################################### BEFORE SCENARIO ######################################
def before_scenario(context, scenario):
    if os.getenv('RELOADBROWSER') == "true":
            context.type_execution = "selenium"
            execution_selenium(context)
    else:
        assert False, "BUG QA, no define tag to type execution in feature file"


###################################### AFTER SCENARIO ######################################
def after_scenario(context, scenario):
    if os.getenv('EXECUTE_ALLURE') == "true":
        attachment_browser_scenario_in_allure(context)
        update_personal_report_allure(context)

    if os.getenv('RELOADBROWSER') == "true":
        context.browser.quit()


###################################### AFTER STEP ######################################
def after_step(context, step):
    if os.getenv('EXECUTE_ALLURE') == "true":
        attachment_screenshot_step_in_allure(context)


########### SELENIUM FUNCTIONS
def execution_selenium(context):
    if os.getenv('EXECUTION_SELENIUM_IP') == "localhost":
        name_os = system()
        try:
            if os.getenv('BROWSER') == "chrome":
                if name_os == "Windows":
                    rute_driver = str(pathlib.Path().absolute(
                    )) + "/helper/selenium_class/web_driver/" + os.getenv(
                        'BROWSER') + "/" + name_os + "/chromedriver.exe"
                elif name_os == "Linux" or name_os == "Darwin":
                    rute_driver = str(pathlib.Path().absolute(
                    )) + "/helper/selenium_class/web_driver/" + os.getenv('BROWSER') + "/" + name_os + "/chromedriver"
                else:
                    assert False, "Operative System not recognize"
                rute_driver = rute_driver.replace("\\", "/")

                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument("--start-maximized")
                chrome_options.add_argument("--disable-xss-auditor")
                chrome_options.add_argument("--disable-web-security")
                chrome_options.add_argument("--allow-running-insecure-content")
                chrome_options.add_argument("--no-sandbox")
                chrome_options.add_argument("--disable-setuid-sandbox")
                chrome_options.add_argument("--disable-webgl")
                chrome_options.add_argument("--disable-popup-blocking")
                cur_dir = os.path.dirname(os.path.realpath(__file__)).replace("features", "downloads")
                pref = {"download.default_directory": cur_dir}
                chrome_options.add_experimental_option("prefs", pref)
                context.browser = webdriver.Chrome(executable_path=rute_driver, options=chrome_options)


            elif os.getenv('BROWSER') == "firefox":
                if name_os == "Windows":
                    rute_driver = str(pathlib.Path().absolute(
                    )) + "/helper/selenium_class/web_driver/" + os.getenv(
                        'BROWSER') + "/" + name_os + "/geckodriver.exe"
                elif name_os == "Linux" or name_os == "Darwin":
                    rute_driver = str(pathlib.Path().absolute(
                    )) + "/helper/selenium_class/web_driver/" + os.getenv('BROWSER') + "/" + name_os + "/geckodriver"
                else:
                    assert False, "Operative System not recognize"
                rute_driver = rute_driver.replace("\\", "/")

                options = webdriver.FirefoxOptions()
                options.set_preference("dom.webnotifications.serviceworker.enabled", False)
                options.set_preference("dom.webnotifications.enabled", False)
                context.browser = webdriver.Firefox(options=options, executable_path=rute_driver)
                if context.type_execution == "mobile":
                    options.add_argument("--width=375")
                    options.add_argument("--height=667")
                else:
                    options.add_argument('--maximized')
                    context.browser.maximize_window()
            elif os.getenv('BROWSER') == "opera":
                if name_os == "Windows":
                    rute_driver = str(pathlib.Path().absolute(
                    )) + "/helper/selenium_class/web_driver/" + os.getenv(
                        'BROWSER') + "/" + name_os + "/operadriver.exe"
                elif name_os == "Linux" or name_os == "Darwin":
                    rute_driver = str(pathlib.Path().absolute(
                    )) + "/helper/selenium_class/web_driver/" + os.getenv('BROWSER') + "/" + name_os + "/operadriver"
                else:
                    assert False, "Operative System not recognize"
                rute_driver = rute_driver.replace("\\", "/")

                context.browser = webdriver.Opera(executable_path=rute_driver)

            elif os.getenv('BROWSER') == "edge":
                if name_os == "Windows":
                    rute_driver = str(pathlib.Path().absolute(
                    )) + "/helper/selenium_class/web_driver/" + os.getenv(
                        'BROWSER') + "/" + name_os + "/msedgedriver.exe"
                elif name_os == "Linux" or name_os == "Darwin":
                    rute_driver = str(pathlib.Path().absolute(
                    )) + "/helper/selenium_class/web_driver/" + os.getenv('BROWSER') + "/" + name_os + "/msedgedriver"
                else:
                    assert False, "Operative System not recognize"
                rute_driver = rute_driver.replace("\\", "/")

                context.browser = webdriver.Edge(executable_path=rute_driver)

            elif os.getenv('BROWSER') == "safari":
                if name_os == "Windows" or name_os == "Linux":
                    assert False, "Safari is not support in Windows or Linux"

                elif name_os == "Darwin":
                    try:
                        context.browser = webdriver.Safari()
                    except:
                        assert False, "not found Safari in your operative system. Remember must be to activate webdriver in MAC"
                else:
                    assert False, "Operative System not recognize"

            context.browser.set_page_load_timeout(time_to_wait=200)
        except:
            assert False, "Connection webdriver is not correct, you should check connection rute"
    else:
        if os.getenv('BROWSER') == "chrome":

            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--start-maximized")
            cur_dir = os.path.dirname(os.path.realpath(__file__)).replace("features", "downloads")
            pref = {"download.default_directory": cur_dir}
            chrome_options.add_experimental_option("prefs", pref)
            options = chrome_options

        elif os.getenv('BROWSER') == "firefox":
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument("--headless")
            firefox_options.add_argument("--width=" + os.getenv('WIDTH_RESOLUTION'))
            firefox_options.add_argument("--height=" + os.getenv('HEIGHT_RESOLUTION'))
            # firefox_options.add_argument("--window-size="+os.getenv('WIDTH_RESOLUTION')+","+os.getenv('HEIGHT_RESOLUTION'))
            options = firefox_options

        elif os.getenv('BROWSER') == "edge":
            edge_options = webdriver.EdgeOptions()
            edge_options.use_chromium = True
            edge_options.add_argument("--headless")
            edge_options.add_argument("--window-size=1920,1080")
            options = edge_options

            assert False, "Falta agregar en arquetipo"

        elif os.getenv('BROWSER') == "opera":
            capabilities = webdriver.DesiredCapabilities().OPERA
            capabilities['browserName'] = "operablink"
            # capabilities['width'] = "1299"
            # capabilities['height'] = "999"


        elif os.getenv('BROWSER') == "safari":
            options = "falta agregar en arquetipo"
            assert False, "Falta agregar en arquetipo"

        else:
            assert False, "Not exist BROWSER required"

        try:
            if os.getenv('USER_SAUCELAB_SELENIUM') is not None and os.getenv('TOKEN_SAUCELAB_SELENIUM') is not None:

                capabilities = {
                    'browserName': os.getenv('BROWSER'),
                    'browserVersion': os.getenv('BROWSER_VERSION_SELENIUM'),
                    'platformName': os.getenv('PLATFORM_NAME_SELENIUM'),
                    'sauce:options': {
                    }
                }
                context.browser = webdriver.Remote("https://" + os.getenv('USER_SAUCELAB_SELENIUM') + ":" + os.getenv(
                    'TOKEN_SAUCELAB_SELENIUM') + "@" + os.getenv('EXECUTION_SELENIUM_IP') + ":443/wd/hub", capabilities)

            else:
                if os.getenv('BROWSER') == 'opera':
                    context.browser = webdriver.Remote('http://' + os.getenv("EXECUTION_SELENIUM_IP") + ':4444/wd/hub',
                                                       capabilities)
                else:
                    context.browser = webdriver.Remote(
                        command_executor='http://' + os.getenv("EXECUTION_SELENIUM_IP") + ':4444/wd/hub',
                        desired_capabilities=options.to_capabilities())

            context.browser.set_page_load_timeout(time_to_wait=200)
        except:
            assert False, "Connection Selenium is not correct, you should check Selenium Grid server"

    context.window_control = WindowControl(context.browser)
    context.elements = Elements(context.browser)
    context.js_script = JsScript(context.browser)
    context.mouse_action = MouseActions(context.browser)
    context.keyboard_action = KeyboardActions(context.browser)

########### ALLURE FUNCTIONS
def attachment_browser_scenario_in_allure(context):
    if context.type_execution == "selenium":
        allure.attach(context.browser.name, name="Browser", attachment_type=AttachmentType.TEXT)


def attachment_screenshot_step_in_allure(context):
    if context.type_execution == "selenium":
        allure.attach(context.browser.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

# TODO Refactor condiciones recursivas por S.O
def update_personal_report_allure(context):
    name_os = system()
    if name_os == 'Linux':
        file = open(str(pathlib.Path().absolute()) + "/reporte/environment.properties", "w+")
        if context.type_execution == "selenium":
            file.write("Browser=" + context.browser.name.capitalize() + os.linesep)
            file.write("Browser.Version=Latest" + os.linesep)
        elif context.type_execution == "service":
            file.write("Browser=service" + os.linesep)
        else:
            assert False, "BUG QA, no define tag to type execution in feature file"
        file.write("Stand=Develop")
        file.close()
    elif name_os == 'Windows':
        file = open(str(pathlib.Path().absolute()) + "\\reporte\\environment.properties", "w+")
        if context.type_execution == "selenium":
            file.write("Browser=" + context.browser.name.capitalize() + os.linesep)
            file.write("Browser.Version=Latest" + os.linesep)
        elif context.type_execution == "service":
            file.write("Browser=service" + os.linesep)
            file.write("Browser.Version=Latest" + os.linesep)
        else:
            assert False, "BUG QA, no define tag to type execution in feature file"

        file.write("Stand=Develop")
        file.close()
    elif name_os == 'Darwin':
        file = open(str(pathlib.Path().absolute()) + "/reporte/environment.properties", "w+")
        if context.type_execution == "selenium":
            file.write("Browser=" + context.browser.name.capitalize() + os.linesep)
            file.write("Browser.Version=Latest" + os.linesep)
        elif context.type_execution == "service":
            file.write("Browser=service" + os.linesep)
        else:
            assert False, "BUG QA, no define tag to type execution in feature file"

        file.write("Stand=Develop")
        file.close()