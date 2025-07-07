from playwright.sync_api import Page
from playwright.sync_api._generated import Locator


class IndexPage:

    ENDPOINT = "https://demo.automationtesting.in/"

    def __init__(self, driver_page):
        self.driver_page: Page = driver_page

    @property
    def email_signup_input(self) -> Locator:
        return self.driver_page.locator("input#email")

    @property
    def register_button(self) -> Locator:
        return self.driver_page.locator("div.col-xs-7 a[href='Register.html']")


    def enter_email_and_submit(self, email: str):
        from lesson_28_bonus.page_objects.registration_page import RegistrationPage
        self.email_signup_input.type(email)
        self.register_button.click()
        return RegistrationPage(self.driver_page)

