import sys

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BingPageObject:
    def __init__(self, web_driver):
        self.__web_driver = web_driver
        self.__wait = WebDriverWait(self.__web_driver, 10) # Explicitly wait
        self.__action = ActionChains(self.__web_driver)

    @property
    def search_field(self):
        return self.__wait.until(EC.element_to_be_clickable((By.ID, "sb_form_q")))

    @property
    def search_button(self):
        return self.__wait.until(EC.element_to_be_clickable((By.ID, "sb_form_go")))

    @property
    def command_key(self):
        if sys.platform == 'darwin':
            return Keys.COMMAND
        else:
            return Keys.CONTROL

    @property
    def text_to_search(self):
        return self.search_field.get_attribute("value")

    def open(self):
        self.__web_driver.get("https://www.bing.com/")

        return self

    def input_search_statement(self, statement: str):
        self.search_field.send_keys(statement)

        return self

    def clear_search_field(self):
        self.search_field.clear()
        return self

    def click_on_search_button(self):
        self.search_button.click()

        return self

    def start_search_by_enter_key(self):
        self.__action.key_down(
            Keys.ENTER).key_up(Keys.ENTER).perform()

        return self

    def select_all_on_the_page_and_copy_to_clipboard(self):
        self.__action.key_down(self.command_key)\
            .send_keys('a')\
            .key_up(self.command_key)\
            .key_down(self.command_key)\
             .send_keys('c').perform()

        return self

    def insert_into_search_field_from_the_clipboard(self):
        self.__action.click(on_element=self.search_field).key_down(self.command_key).send_keys('v').perform()
        return self