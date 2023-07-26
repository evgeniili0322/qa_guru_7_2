from selene.support.shared import browser
from selene import be, have
import pytest
from selenium import webdriver


def test_search_result(browser_opt):
    browser.open('')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in'))
