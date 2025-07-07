from playwright.sync_api import Page

from lesson_28.page_objects.base_page import BasePage


class RegistrationPage:

    ENDPOINT : str

    def __init__(self, driver):
        self.driver: Page = driver
        self.driver.wait_for_url(self.ENDPOINT)