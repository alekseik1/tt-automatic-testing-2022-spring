import os

import pytest

from tests.ui.locators.start import StartPageLocators
from tests.ui.pages.base import MainPage, StartPage


@pytest.fixture(scope="session")
def creds():
    return os.environ.get("MY_TARGET_USER"), os.environ.get("MY_TARGET_PASSWORD")


@pytest.fixture()
def start_page(driver):
    return StartPage(driver=driver)


@pytest.fixture()
def main_page(driver):
    return MainPage(driver=driver)


@pytest.mark.UI
@pytest.mark.skip()
def test_can_click_login_button(start_page: StartPage):
    # GIVEN page
    # WHEN user attempts to find "login" button
    # THEN: no error raised
    button = start_page.find(StartPageLocators.LOGIN_BUTTON)
    # THEN: button can be clicked without errors
    button.click()


@pytest.mark.UI
@pytest.mark.skip()
def test_full_login(start_page: StartPage, creds):
    # GIVEN: valid creds
    username, password = creds
    # WHEN: user asks to login
    # WHEN: user gives correct login and password
    start_page.full_login(username, password)
    # THEN: login succeeds


@pytest.mark.UI
def test_full_login_logout(start_page: StartPage, main_page: MainPage, creds):
    # GIVEN: valid creds
    username, password = creds
    # WHEN: user asks to login
    # WHEN: user gives correct login and password
    start_page.full_login(username, password)
    # WHEN: user pressed "log out"
    main_page.logout()
    # THEN: no error is raised
