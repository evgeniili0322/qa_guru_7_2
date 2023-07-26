from selene.support.shared import browser
from selenium import webdriver
import pytest

options = webdriver.FirefoxOptions()


@pytest.fixture(scope='function', autouse=True)
def browser_opt():
    options.add_argument("-width=1920")
    options.add_argument("-height=1080")
    browser.config.driver_name = 'firefox'
    browser.config.driver_options = options
    browser.config.base_url = 'https://google.com/ncr'
