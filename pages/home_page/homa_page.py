from selene import browser, be, have
from selene.core.conditions import Condition as EC
from selene.support.shared.jquery_style import s, ss
from allure import step

from helpers.data_source.links.links import Links


class HomePage:
    def __init__(self):
        self.base_url = Links().base_url

        self.logo_home_page = ".HeaderTop_header-top-logo__zO0BT"

    @step("Открыть главную страницу")
    def open(self):
        browser.open(self.base_url)
        return self

    @step("Проверить открытие главной страницы")
    def is_opened(self):
        s(self.logo_home_page).should(EC.by_and(be.visible))



