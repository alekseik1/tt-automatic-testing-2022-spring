import pytest

from tests.hw1.base import BaseCase


@pytest.mark.skip(reason="Broken after refactoring, used as a template")
class TestExample(BaseCase):
    @pytest.mark.parametrize("query", [pytest.param("pycon"), pytest.param("python")])
    def test_search(self, query):
        self.search(query)
        assert "No results found" not in self.driver.page_source

    @pytest.mark.xfail(reason="some failure")
    def test_negative_search(self):
        self.search("adasdasdasdasdasda")
        assert "No results found" not in self.driver.page_source
