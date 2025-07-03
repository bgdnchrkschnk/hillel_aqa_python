from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # WRAPPER FUNCTION
    def get_menu_item(self, item):
        txt = item.lower().replace(' ', '-')
        return self.driver.find_element_by_css_selector(f"[href='/{txt}/']")

    @property
    def about_link(self):
        return self.get_menu_item("About")

    @property
    def download_link(self):
        return self.get_menu_item("Downloads")

    @property
    def community_link(self):
        return self.get_menu_item("Community")

    @property
    def success_stories_link(self):
        return self.get_menu_item("Success Stories")

    def go_to_about_page(self):

        self.about_link.click()

        from page_objects.python_site.about_page import AboutPage

        return AboutPage(self.driver)