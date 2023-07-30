from selene import browser
from selenium import webdriver
import pytest

options = webdriver.ChromeOptions()


@pytest.fixture(scope='function', autouse=True)
def browser_opt():
    options.add_argument('--window-size=1920,1080')
    browser.config.driver_options = options
    browser.config.base_url = 'https://startpage.com/'
