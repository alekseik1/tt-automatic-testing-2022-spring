import pytest

from tests.hw1.base import BaseCase
from tests.ui.locators import basic_locators


class TestExample(BaseCase):
    @pytest.mark.parametrize("query", [pytest.param("pycon"), pytest.param("python")])
    def test_search(self, query):
        self.search(query)
        assert "No results found" not in self.driver.page_source

    @pytest.mark.xfail(reason="some failure")
    def test_negative_search(self):
        self.search("adasdasdasdasdasda")
        assert "No results found" not in self.driver.page_source

    @pytest.mark.UI
    def test_page_change(self):
        self.click(basic_locators.GO_BUTTON_LOCATOR)
