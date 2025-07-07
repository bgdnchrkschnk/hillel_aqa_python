from playwright.sync_api import Page
from playwright.sync_api import expect

from lesson_28_bonus.page_objects.index_page import IndexPage


class TestPlaywright:

    # def test_example_playwright(self, page: Page):
    #     page.goto("https://demo.automationtesting.in")
    #     skip_registration_button = page.locator("#btn2")  # find element
    #     skip_registration_button.click()
    #     check_box_movies = page.locator("#checkbox2")
    #     check_box_movies.check()
    #     page.wait_for_timeout(1000)
    #     check_box_movies.uncheck()
    #     page.wait_for_timeout(1000)
    #     phone_input = page.locator("input[type=tel]")
    #     phone_input.type("8723893798643", delay=50)  # type something in text zone
    #     phone_input.clear()  # cleat text zone
    #     page.wait_for_selector(".fa-facebook-square", state="visible")  # customized expected timeout or state
    #     page.locator("a[href='Interactions.html']").hover()
    #     page.wait_for_timeout(1000)
    #     checkboxes = page.locator("[type=checkbox]")
    #     skills_dropdown = page.locator("select[ng-model=Skill]")
    #     skills_dropdown.select_option(index=5)
    #     # skip_registration_button.text_content()  # увесь текст що міститься в елементі
    #     # skills_dropdown.inner_text()  # увесь ВИДИМИй текст для користувача

    def test_register(self, page_custom):
        page_custom.email_signup_input.type("dbjksbchjnjks@gmail.com")
        page_custom.driver_page.wait_for_timeout(3000)
        page_custom.driver_page.wait_for_url(IndexPage.ENDPOINT+"Register.html")
        assert page_custom.driver_page.title() == "Register"