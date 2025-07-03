from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from page_objects.python_site.base_page import BasePage


class AboutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def about_banner(self):
        return self.wait.until(EC.visibility_of_element_located(((By.CSS_SELECTOR, ".about-banner"))))