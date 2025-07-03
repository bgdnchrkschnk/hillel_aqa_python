from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from page_objects.python_site.base_page import BasePage
from page_objects.python_site.membership_page import MembershipPage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def membership_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button[href$='membership/']")))

    def click_membership_button(self):

        self.membership_button.click()

        return MembershipPage(self.driver)