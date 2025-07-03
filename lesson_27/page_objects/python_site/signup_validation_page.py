from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from page_objects.python_site.base_page import BasePage


class SignupValidationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def verification_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(((By.CSS_SELECTOR, "div.user-feedback>p[role=general]")))).text