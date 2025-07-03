import time

import pytest

from page_objects.bing_page_object import BingPageObject


class TestPageObjects:
    @pytest.mark.explicit_wait_agains_stale_element_exception
    def test_explicit_wait_agains_stale_element_exception(self, bing_page: BingPageObject):

        bing_page.open()

        time.sleep(1)

        bing_page.input_search_statement("python + selenium")

        time.sleep(1)

        bing_page.start_search_by_enter_key()

        time.sleep(1)

        bing_page.clear_search_field()

        time.sleep(1)

        bing_page.select_all_on_the_page_and_copy_to_clipboard()

        time.sleep(1)

        bing_page.insert_into_search_field_from_the_clipboard()

        time.sleep(1)

        assert len(bing_page.text_to_search), "No text from found results is inserted into the search field"