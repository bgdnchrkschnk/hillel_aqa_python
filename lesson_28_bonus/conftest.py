import pytest
from playwright.sync_api import Browser, Page

from lesson_28_bonus.page_objects.index_page import IndexPage


@pytest.fixture
def page_custom(browser: Browser):
   page: Page = browser.new_page()
   index_page = IndexPage(driver_page=page)
   index_page.driver_page.goto(url=IndexPage.ENDPOINT)
   yield index_page
   browser.close()