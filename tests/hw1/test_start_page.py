import pytest

from tests.ui.locators.start import StartPageLocators
from tests.ui.pages.base import BasePage


@pytest.mark.UI
def test_can_find_button(driver):
    page = BasePage(driver)
    page.click(StartPageLocators.LOGIN_BUTTON, timeout=120)
