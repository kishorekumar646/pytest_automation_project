from selenium.webdriver import ActionChains
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote import webelement


class Locators:

    def __init__(self, driver, by: str, value: str) -> None:
        self.driver = driver
        self.by = by
        self.value = value

    def send_keys(self, string) -> bool:
        try:
            self.driver.find_element(self.by, self.value).send_keys(string)
        except Exception as e:
            print("Send keys not worked at \n" + self.by + "\n" + self.value + "\n Exception: \n" + str(e))
            return False
        else:
            return True

    def click(self) -> bool:
        try:
            self.driver.find_element(self.by, self.value).click()
        except Exception as e:
            print("click not worked at \n" + self.by + "\n" + self.value + "\n Exception: \n" + str(e))
            return False
        else:
            return True

    def mouse_over(self) -> bool:
        hovering_element = self.driver.find_element(self.by, self.value)
        hover = ActionChains(self.driver).move_to_element(hovering_element)
        try:
            hover.perform()
        except Exception as e:
            print("mouse_over not worked at \n" + self.by + "\n" + self.value + "\n Exception: \n" + str(e))
            return False
        else:
            return True

    def text(self) -> str:
        try:
            txt_value = self.driver.find_element(self.by, self.value).text
        except Exception as e:
            print("get text not worked at \n" + self.by + "\n" + self.value + "\n Exception: \n" + str(e))
            return False
        else:
            return txt_value

    def select(self, string):
        try:
            select = Select(self.driver.find_element(self.by, self.value))
            select.select_by_visible_text(string)

        except Exception as e:
            print("select not worked at \n" + self.by + "\n" + self.value + "\n Exception: \n" + str(e))

    def get_attribute(self, name) -> str:
        try:
            att_value = self.driver.find_element(self.by, self.value).get_attribute(name)
        except Exception as e:
            print("get attribute not worked at \n" + self.by + "\n" + self.value + "\n Exception: \n" + str(e))
            return False
        else:
            return att_value

    def texts(self) -> list:
        try:
            arr_text = []
            elements = self.driver.find_elements(self.by, self.value)
            for ele in elements:
                arr_text.append(ele.text)
        except Exception as e:
            print("get texts not worked at \n" + self.by + "\n" + self.value + "\n Exception: \n" + str(e))
            return [False]
        else:
            return arr_text

    def texts_as_string(self) -> str:
        try:
            arr_text = []
            elements = self.driver.find_elements(self.by, self.value)
            for ele in elements:
                arr_text.append(ele.text)
        except Exception as e:
            print("get texts not worked at \n" + self.by + "\n" + self.value + "\n Exception: \n" + str(e))
            return ""
        else:
            return ''.join(map(str, arr_text))

    def is_displayed(self) -> bool:
        try:
            return self.driver.find_elements(self.by, self.value).is_displayed()
        except Exception as e:
            print("is_displayed not worked at \n" + self.by + "\n" + self.value + "\n Exception: \n" + str(e))
            return False

    def is_enabled(self) -> bool:
        try:
            return self.driver.find_elements(self.by, self.value).is_enabled()
        except Exception as e:
            print("is_enabled not worked at \n" + self.by + "\n" + self.value + "\n Exception: \n" + str(e))
            return False

    def is_displayed_with_wait(self, timeout=10) -> bool:
        try:
            wait = ui.WebDriverWait(self.driver, timeout)
            return wait.until(lambda element: self.driver.find_element(self.by, self.value).is_displayed())
        except Exception as e:
            print("is_displayed_with_wait not worked at \n" + self.by + "\n" + self.value + "\n Exception: \n" + str(e))
            return False

    def wait_till_displayed(self, timeout=10) -> bool:
        try:
            wait = ui.WebDriverWait(self.driver, timeout)
            return wait.until(lambda element: self.driver.find_element(self.by, self.value).is_displayed())
        except Exception as e:
            print("wait_till_displayed not worked at \n" + self.by + "\n" + self.value + "\n Exception: \n" + str(e))
            return False

    def click_if_displayed(self) -> bool:
        try:
            self.is_displayed_with_wait()
            var = self.driver.find_element(self.by, self.value).click
            print("Click action complete on:" + self.by + "with " + self.value + "return value: " + var)
        except Exception as e:
            print("click if displayed not worked at \n" + self.by + "\n" + self.value + "\n Exception: \n" + str(e))
            return False
        else:
            return True

    def scroll_to_locator(self) -> bool:
        try:
            scroll_locator = self.driver.find_element(self.by, self.value)
            actions = ActionChains(self.driver)
            actions.move_to_element(scroll_locator)
            actions.perform()
        except Exception as e:
            print("scroll to locator not worked at \n" + self.by + "\n" + self.value + "\n Exception: \n" + str(e))
            return False
        else:
            return True

    def scroll_to_locator_using_js(self) -> bool:
        try:
            scroll_locator = self.driver.find_element(self.by, self.value)
            self.driver.execute_script('arguments[0].scrollIntoView(true);', scroll_locator)
        except Exception as e:
            print("scroll to locator using js not worked at:" + self.by + ":" + self.value + " Exception: " + str(e))
            return False
        else:
            return True

    def move_and_click(self) -> bool:
        try:
            self.scroll_to_locator()
            self.mouse_over()
            self.click()
        except Exception as e:
            print("move and click not worked at \n" + self.by + "\n" + self.value + "\n Exception: \n" + str(e))
            return False
        else:
            return True

    def get_element(self) -> webelement.WebElement:
        try:
            return self.driver.find_element(self.by, self.value)
        except Exception as e:
            print("get element not worked at \n" + self.by + "\n" + self.value + "\n Exception: \n" + str(e))

    def clear_and_send_keys(self, string) -> bool:
        try:
            var = self.driver.find_element(self.by, self.value).clear()
            print("Clear action completed on: " + self.by + " and " + self.value + " Return value is: " + var)
            self.driver.find_element(self.by, self.value).send_keys(string)
        except Exception as e:
            print("Clear and Send keys not worked at \n" + self.by + "\n" + self.value + "\n Exception: \n" + str(e))
            return False
        else:
            return True

    def get(self):
        return "By: " + self.by + " Value: " + self.value