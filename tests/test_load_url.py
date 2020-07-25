
import pytest

from pages.homePage import homePage

def test_load_url(browser):
    
    TITLE = "The Internet"

    home_page = homePage(browser)

    home_page.load()

    assert TITLE == home_page.get_title()