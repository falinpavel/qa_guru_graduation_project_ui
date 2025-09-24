from selene import browser, be, have
from selene.core.conditions import Condition as EC
from selene.support.shared.jquery_style import s, ss
from allure import step

from helpers.data_source.links.links import Links


class HomePage:
    def __init__(self):
        self.base_url = Links().base_url
        # locators
        self.close_widget_button = '.closeIcon__TO5Xx'
        self.accept_cookie_button = '.cookie-notice__content > .button'
        self.slider = '.home-hero__slider'
        self.slider_swipe_left_button = '.home-hero__nav_prev'
        self.slider_swipe_right_button = '.home-hero__nav_next'

    @step("Открыть главную страницу")
    def open(self):
        browser.open(self.base_url)
        return self

    @step("Проверить открытие главной страницы")
    def is_opened(self):
        s(self.slider).should(EC.by_and(be.visible))
        return self

    @step("Закрыть виджет 'Напишите нам...'")
    def close_widget(self):
        s(self.close_widget_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Принять куки")
    def accept_cookie(self):
        s(self.accept_cookie_button).should(EC.by_and(be.clickable)).click()
        return self
