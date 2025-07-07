from playwright.sync_api import sync_playwright



def playwright_run():
    with (sync_playwright() as playwright):
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("https://demo.automationtesting.in")
        skip_registration_button = page.locator("#btn2") # find element
        breakpoint()
        skip_registration_button.click()
        check_box_movies = page.locator("#checkbox2")
        check_box_movies.check()
        page.wait_for_timeout(1000)
        check_box_movies.uncheck()
        page.wait_for_timeout(1000)
        phone_input = page.locator("input[type=tel]")
        phone_input.type("8723893798643", delay=50) # type something in text zone
        phone_input.clear() # cleat text zone
        page.wait_for_selector(".fa-facebook-square", state="visible") # customized expected timeout or state
        page.locator("a[href='Interactions.html']").hover()
        page.wait_for_timeout(1000)
        checkboxes = page.locator("[type=checkbox]")
        skills_dropdown = page.locator("select[ng-model=Skill]")
        skills_dropdown.select_option(index=5)
        skip_registration_button.text_content() # увесь текст що міститься в елементі
        skills_dropdown.inner_text() # увесь ВИДИМИй текст для користувача
        browser.close()


if __name__ == "__main__":
    playwright_run()