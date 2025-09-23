from selene import browser
from allure import step

from helpers.data_source.links.links import Links


class HomePage:
    def __init__(self):
        self.base_url = Links().base_url

    def open(self):
        browser.open(self.base_url)
        return self
