""" Este módulo contém homePage,
o page object para a home page do
The Internet.
"""

from selenium.webdriver.common.by import By

from locators.locators import HomePageLocators

class homePage:

    def __init__(self, browser):
        self.browser = browser
    
    def load(self):
        self.browser.get(HomePageLocators.URL)

    def get_title(self):
        return self.browser.title