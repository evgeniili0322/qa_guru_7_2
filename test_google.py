from selene.support.shared import browser
from selene import be, have


def test_search_result():
    browser.open('')
    browser.element('[name=q]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('#search').should(have.text('yashaka/selene: User-oriented Web UI browser tests in'))


def test_blank_search_result():
    browser.open('')
    browser.element('[name=q]').should(be.blank).type('0x000001DB9AA6C690').press_enter()
    browser.element('#search').should(be.hidden)
    browser.element('.card-section [aria-level="3"]').should(
        have.text('Your search - 0x000001DB9AA6C690 - did not match any documents.'))
