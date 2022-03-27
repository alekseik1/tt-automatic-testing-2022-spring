from selenium.webdriver.common.by import By


class StartPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//div[contains(@class, 'responseHead-module-button')]")
    USERNAME_INPUT = (
        By.XPATH,
        "//input[contains(@class, 'authForm-module-input') and @name='email']",
    )
    PASSWORD_INPUT = (
        By.XPATH,
        "//input[contains(@class, 'authForm-module-inputPassword') and @name='password']",
    )
    LOGIN_SUBMIT_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'authForm-module-actions')]"
        "//div[contains(@class, 'authForm-module-button')]",
    )


class MainPageLocators:
    LOGOUT_BAR = (
        By.XPATH,
        "//div[contains(@class, 'right-module-rightButton') and "
        "contains(@class, 'right-module-mail')]",
    )
    LOGOUT_BUTTON = (
        By.XPATH,
        "//ul[contains(@class, 'rightMenu-module-rightMenu')]//a[@href='/logout']",
    )
