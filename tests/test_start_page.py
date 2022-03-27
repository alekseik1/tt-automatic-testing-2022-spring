from tests.ui.locators.start import StartPageLocators
from tests.ui.pages.base import BasePage


def test_can_find_button(driver):
    page = BasePage(driver)
    page.click(StartPageLocators.LOGIN_BUTTON)
