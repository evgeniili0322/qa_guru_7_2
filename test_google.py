from selene import browser
from selene import be, have


def test_search_result():
    browser.open('')
    browser.element('#q').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('.mainline-results__web').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_blank_search_result():
    browser.open('')
    browser.element('#q').should(be.blank).type('0x000001DB9AA6C690').press_enter()
    browser.element('#main .mainline-results').should(have.text('Uh-oh, there are no results for this search.'))
