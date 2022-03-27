from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.ui.locators.start import MainPageLocators, StartPageLocators


class BasePage:
    def __init__(self, driver, timeout: int = 120):
        self.driver = driver
        self.timeout = timeout

    def wait(self, timeout=None):
        if timeout is None:
            timeout = self.timeout
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None) -> WebElement:
        return self.wait(timeout).until(EC.presence_of_element_located(locator))


class StartPage(BasePage):
    def full_login(self, username: str, password: str):
        login_button = self.find(StartPageLocators.LOGIN_BUTTON)
        login_button.click()
        username_field = self.find(StartPageLocators.USERNAME_INPUT)
        username_field.send_keys(username)
        password_field = self.find(StartPageLocators.PASSWORD_INPUT)
        password_field.send_keys(password)
        login_submit_btn = self.find(StartPageLocators.LOGIN_SUBMIT_BUTTON)
        login_submit_btn.click()


class MainPage(BasePage):
    def logout(self):
        logout_btn = self.find(MainPageLocators)
        logout_btn.click()
