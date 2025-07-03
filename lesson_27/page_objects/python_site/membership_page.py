from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from page_objects.python_site.base_page import BasePage
from page_objects.python_site.signup_page import SignupPage


class MembershipPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def signup_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button[href$='signup/']")))

    def click_signup_button(self):

        self.signup_button.click()

        return SignupPage(self.driver)