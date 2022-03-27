import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--url", default="https://www.python.org")


@pytest.fixture()
def config(request):
    return {
        key: request.config.getoption(f"--{key}")
        for key in ("browser", "headless", "url")
    }


@pytest.fixture()
def driver(config):
    browser = config["browser"]
    url = config["url"]
    if browser == "chrome":
        opts = Options()
        if config["headless"]:
            opts.add_argument("--headless")
        driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install(), options=opts
        )
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.get(url)
    driver.maximize_window()
    # browser.set_window_size(1400, 1000)
    # browser.set_network_conditions(
    #     latency=5,
    #     download_throughput=100 * 1024,
    #     upload_throughput=100 * 1024,
    # )
    yield driver
    driver.quit()
