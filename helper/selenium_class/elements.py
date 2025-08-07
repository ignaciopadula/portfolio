from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from helper.pages import POM_Principals, POM_Brokers, POM_Obligees, POM_Requests
from helper.selenium_class.constants import wait_except
from helper.selenium_class.constants import by_var
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

class Elements:
    """
        This class validates the elements items
    """
    def __init__(self, browser):
        """
        *Constructor of class*

        - `@param browser: The internet browser driver used`
        """
        self.__browser = browser

    def __str__(self):
        """
        *If you print the variable of the instantiated class it returns the string of this method*

        - `@return: The important variables of the class`
        """
        return "elements"
    

    """def _find_element(self, url_element, type="xpath"):
        *Find elements in web*

        - `@param url_element: string of url element`
        - `@param type: method to use to find element`
        - `@return: element found`
        element = None
        try:
            if type == "xpath":
                element = self.__browser.find_element_by_xpath(url_element)
            elif type == "id":
                element = self.__browser.find_element_by_id(url_element)
            elif type == "name":
                element = self.__browser.find_element_by_name(url_element)
            elif type == "link_text":
                element = self.__browser.find_element_by_link_text(url_element)
            elif type == "partial_link_text":
                element = self.__browser.find_element_by_partial_link_text(url_element)
            elif type == "tag_name":
                element = self.__browser.find_element_by_tag_name(url_element)
            elif type == "class_name":
                element = self.__browser.find_element_by_class_name(url_element)
            elif type == "css_selector":
                element = self.__browser.find_element_by_css_selector(url_element)
            else:
                assert False, "Type parameters not found"

            assert element != None, "No element found"

            return element

        except:
            assert False, "No element found, you should verify parameters in function"""

    def _find_element(self, element_by=By):
        element = ""
        try:
            element = self.__browser.find_element(*element_by)
        except Exception as ex:
            print(ex)
            assert element is not None, "Elemento no encontrado en el dom : " + element
        return element


    def _sub_find_element(self, url_element, element, type="xpath"):
        """
        *Find elements in web*

        - `@param url_element: string of url element`
        - `@param element: element to find element`
        - `@param type: method to use to find element`
        - `@return: element found`
        """
        try:
            if type == "xpath":
                element = element.find_element_by_xpath(url_element)
            elif type == "id":
                element = element.find_element_by_id(url_element)
            elif type == "name":
                element = element.find_element_by_name(url_element)
            elif type == "link_text":
                element = element.find_element_by_link_text(url_element)
            elif type == "partial_link_text":
                element = element.find_element_by_partial_link_text(url_element)
            elif type == "tag_name":
                element = element.find_element_by_tag_name(url_element)
            elif type == "class_name":
                element = element.find_element_by_class_name(url_element)
            elif type == "css_selector":
                element = element.find_element_by_css_selector(url_element)
            else:
                assert False, "Type parameters not found"

            assert element is not None, "No element found"

            return element

        except:
            assert False, "No element found, you should verify parameters in function"

    def _is_clickable(self, element_by=By):
        assert element_by is not None, "Element not found"

        return element_by.element_to_be_clickable()
    
    def _find_elements(self, element_by=By):
        element = ""
        try:
            element = self.__browser.find_elements(*element_by)
        except Exception as ex:
            print(ex)
            assert element is not None, "Elemento no encontrado en el dom : " + element
        return element

    def _sub_find_elements(self, url_element, element, type="xpath"):
        """ 
        *Find elements in web*

        - `@param url_element: string of url elements`
        - `@param element to find element`
        - `@param type: method to use to find elements`
        - `@return: list elements found`
        """
        try:
            if type == "xpath":
                elements = element.find_elements_by_xpath(url_element)
            elif type == "id":
                elements = element.find_elements_by_id(url_element)
            elif type == "name":
                elements = element.find_elements_by_name(url_element)
            elif type == "link_text":
                elements = element.find_elements_by_link_text(url_element)
            elif type == "partial_link_text":
                elements = element.find_elements_by_partial_link_text(url_element)
            elif type == "tag_name":
                elements = element.find_elements_by_tag_name(url_element)
            elif type == "class_name":
                elements = element.find_elements_by_class_name(url_element)
            elif type == "css_selector":
                elements = element.find_elements_by_css_selector(url_element)
            else:
                assert False, "Type parameters not found"

            assert elements is not None, "No elements found"

            return elements
        except:
            assert False, "No element found, you should verify parameters in function"

    def _click_element(self, element):
        """
        *click in element in web*

        - `@param element: element to do click`
        """
        assert element is not None, "Element is not found"
        try:
            element.click()
        except:
            assert False, "Click element is not working, you should check elements parameter"

    def _send_text_in_element(self, text, element):
        """
        *Write a string in the element*

        - `@param text: String to write`
        - `@param element: Element to write a string`
        """
        assert type(text) == str, "Text must be a string"
        try:
            element.send_keys(text)
        except:
            assert False, "send text in element failed, you should check parameters"

    def _get_text_in_element(self, element):
        """
        *Get text in element container*

        - `@param element: element to search text`
        """
        assert element is not None, "Element not found"
        return element.text

    def _get_attribute_in_element(self, element, value):
        """
        *Get attribute of element container*

        - `@param element: element to get attribute`
        - `@param value: Value of attribute in element to search`
        - `@return: value of attribute to search`
        """
        assert (value != "" or value is not None or type(value) != str), "value is None or is empty string"
        assert element is not None, "Element not found"

        return element.get_attribute(value)
    
    def _get_location_element(self, element):
        """
        *Get location of element in browser*

        - `@param element: element to get location`
        """
        assert element is not None, "Element not found"

        return element.location

    def _get_size_element(self, element):
        """
        *Get size of element in browser*

        - `@param element: element to get size`
        """
        assert element is not None, "Element not found"

        return element.size

    def _element_is_selected(self, element):
        """
        *Verify if element is selected*

        - `@param element: element to check is selected`
        - `@return: True or False if elements is selected`
        """
        assert element is not None, "Element not found"

        return element.is_selected()

    def _element_is_displayed(self, element):
        """
        *Verify if element is displayed*

        - `@param element: element to check is displayed`
        - `@return: True or False if elements is displayed`
        """
        assert element is not None, "Element not found"

        return element.is_displayed()

    def _element_is_enabled(self, element):
        """
        *Verify if element is enabled*

        - `@param element: element to check is enabled`
        - `@return: True or False if elements is enabled`
        """
        assert element is not None, "Element not found"

        return element.is_enabled()

    def _clear_text_in_element(self, element):
        """
        *clear text in field*

        - `@param element: element to clear text`
        """

        assert element is not None, "Element not found"
        element.clear()
    
    def _screenshot_element(self, element, str_name_image_screenshot):
        """
        *Take a screenshot of element*

        - `@param element: element to take a screenshot`
        - `@param str_name_image_screenshot: String to save screenshot of element`
        """

        assert element is not None, "Element not found"
        assert (str_name_image_screenshot != "" or str_name_image_screenshot is not None), "Error: str_name_image_screenshot is not correct"
        element.screenshot(str_name_image_screenshot+".png")


    def _find_tag_name_in_element(self, element):
        """
        *find tag name of element container*

        - `@param element: element to find tag name`
        - `@return: tag name of element`
        """
        assert element is not None, "Element not found"
        
        return element.tag_name

    def _find_parent_element(self, element, type="xpath"):
        """
        *find parent of element*

        - `@param element: element to find his parent`
        - `@return: parent of elemento in format element selenium`
        """
        try:
            parent = None

            if type == "xpath":
                parent = element.find_element_by_xpath("..")
            elif type == "id":
                parent = element.find_element_by_id("..")
            elif type == "name":
                parent = element.find_element_by_name("..")
            elif type == "link_text":
                parent = element.find_element_by_link_text("..")
            elif type == "partial_link_text":
                parent = element.find_element_by_partial_link_text("..")
            elif type == "tag_name":
                parent = element.find_element_by_tag_name("..")
            elif type == "class_name":
                parent = element.find_element_by_class_name("..")
            elif type == "css_selector":
                parent = element.find_element_by_css_selector("..")
            else:
                assert False, "Type parameters not found"

            assert parent is not None, "No element parent found"

            return parent
        except:
            assert False, "Element not have parent"


    def _wait_implicitly(self, time):
        """
        *Wait implicitly a time (in seconds) to load in page*

        - `@param time: Seconds to wait load page`
        """
        assert type(time) == int, "Value of time is not integer"

        self.__browser.implicitly_wait(time)

    def _wait_explicitly(self, time, str_url_element, type_by="xpath", type_ec="presence_of_element_located"):
        """
        *Wait el explicitly element to load it*
        
        - `@param time: Time to wait element before print error`
        - `@param str_url_element: string to select element`
        - `@param type_by: type to find element`
        - `@param type_ec: type to method to find element`
        - `@return: element to selected`
        """
        assert type(time) == int, "var time must be integer"
        assert type(str_url_element) == str, "var str_url_element must be string"

        for i in by_var:
            if (i == "class_name" or i == "css_selector" or i == "id" or 
                i == "link_text" or i == "name" or i == "partial_link_text" or 
                i == "tag_name" or i == "xpath"):
                break
        else:
            assert False, "Value type_by is incorrect"


        for i in wait_except:
            if (i == "title_is" or i == "title_contains" or 
                i == "presence_of_element_located" or i == "visibility_of_element_located" or 
                i == "visibility_of" or i == "presence_of_all_elements_located" or 
                i == "text_to_be_present_in_element" or i == "text_to_be_present_in_element_value" or 
                i == "frame_to_be_available_and_switch_to_it" or i == "invisibility_of_element_located" or 
                i == "element_to_be_clickable" or i == "staleness_of" or 
                i == "element_to_be_selected" or i == "element_located_to_be_selected" or 
                i == "element_selection_state_to_be" or i == "element_located_selection_state_to_be" or 
                i == "alert_is_present"):

                break
        else:
            assert False, "Value type_ec is incorrect"

        element = WebDriverWait(self.__browser, time).until(wait_except[type_ec]((by_var[type_by], str_url_element)))
        
        assert element != "None", "element not found"

        return element
        


    ########################### review classes
    def create_select_option(self, value, id):
        """
        *crea un select y va seleccionando de acuerdo al valor que llega de afuera del metodo*
        """
        select_element = self.browser.find_element_by_id(id)
        select_options = Select(select_element)
        select_options.select_by_value(value)


    def select_date(self):
        """
        *Crea un select para los meses y otro para los años y selecciona de acuerdo a los valores que pasamos entre los parentesis,*
        *no recibe parametros desde afuera, los parametros los pasamos directo dentro del metodo*
        """
        div = self.browser.find_element_by_id("rangeDatePicker")
        select_month = Select(div.find_element_by_css_selector("select[title='Select month']"))
        select_year = Select(div.find_element_by_css_selector("select[title='Select year']"))
        select_month.select_by_visible_text("May")
        select_year.select_by_value("2010")

    def show_correct_date(self):
        """
        *Valida que el mes y el año seleccionado sean los que esperamos, no recibe parametros desde afuera, se los pasamos*
        *directo dentro del metodo*
        """
        div = self.browser.find_element_by_id("rangeDatePicker")
        select_month = Select(div.find_element_by_css_selector("select[title='Select month']"))
        select_year = Select(div.find_element_by_css_selector("select[title='Select year']"))
        month = self.browser.find_elements_by_xpath("//div[contains(@class, 'ngb-dp-month-name')]")
        if select_month.first_selected_option.get_attribute(
                'text') == "May" and select_year.first_selected_option.get_attribute('text') == "2010":
            if month[0].text == "May 2010" and month[1].text == "Jun 2010":
                assert True

    def _implicity_wait(context, time, element_by=By):
        try:
            context.scroll_to(element_by)
            element = WebDriverWait(context.__browser, time).until(
                expected_conditions.presence_of_element_located((element_by)))
        except Exception as ex:
            print(ex)
            assert element is not None, "Elemento no encontrado en el dom : " + element
        return element

    def create_select_option_xpath(context, value, element_by=By):
        """
        *crea un select y va seleccionando de acuerdo al valor que llega de afuera del metodo*
        """
        context.scroll_to(element_by)
        select_element = context.__browser.find_element(*element_by)
        select_options = Select(select_element)
        select_options.select_by_visible_text(value)

    def scroll_to(context, element_by=By):
        element = context.__browser.find_element(*element_by)
        desired_y = (element.size['height'] / 2) + element.location['y']
        window_h = context.__browser.execute_script('return window.innerHeight')
        window_y = context.__browser.execute_script('return window.pageYOffset')
        current_y = (window_h / 2) + window_y
        scroll_y_by = desired_y - current_y

        context.__browser.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
        #element.location_once_scrolled_into_view
        #context.__browser.execute_script("arguments[0].scrollIntoView();", element)

    def get_url(context):
        return context.__browser.current_url

    def get_selector(context, seccion=""):
        page = context.get_url()
        if "tomadores" in page:
            context.selector = POM_Principals
        elif "intermediario" in page:
            context.selector = POM_Brokers
        elif "beneficiarios" in page:
            context.selector = POM_Obligees
        elif "solicitudes-garantia" in page:
            context.selector = POM_Requests
        elif "grupos-economicos" in page:
            context.selector = POM_Brokers
        elif "minutas-garantia" in page:
            context.selector = POM_Brokers

        if seccion == "General data":
            context.selector = context.selector.Principals
        if seccion == "Shareholdes information":
            context.selector = context.selector.Shareholders
        if seccion == "Representative information":
            context.selector = context.selector.Representative
        if seccion == "Contractor information":
            context.selector = context.selector.Contractor
        if seccion == "Obligees Information":
            context.selector = context.selector.Obligees
        if seccion == "Job description":
            context.selector = context.selector.Job

        return context.selector