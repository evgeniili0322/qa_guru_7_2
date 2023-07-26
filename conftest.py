from selene.support.shared import browser
from selenium import webdriver
import pytest

options = webdriver.ChromeOptions()


@pytest.fixture
def browser_opt():
    options.add_argument("--window-size=1920,1080")
    browser.config.driver_options = options
    browser.open('https://google.com/ncr')