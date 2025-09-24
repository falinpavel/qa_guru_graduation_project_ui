from selene import browser, be, have
from selene.core.conditions import Condition as EC
from selene.support.shared.jquery_style import s, ss
from allure import step

from helpers.data_source.links.links import Links


class HomePage:
    def __init__(self):
        self.base_url = Links().base_url
        self.logo_home_page = ".HeaderTop_header-top-logo__zO0BT"
        self.swipe_left_button = ".NavigationButton_sklv__swiper-btn_prev__Rurka"
        self.swipe_right_button = ".NavigationButton_sklv__swiper-btn_next__kxotX"
        self.list_stories = ".MainStory_story__BsnKc"

    @step("Открыть главную страницу")
    def open(self):
        browser.open(self.base_url)
        return self

    @step("Проверить открытие главной страницы")
    def is_opened(self):
        s(self.logo_home_page).should(EC.by_and(be.visible))
        return self

    @step("Проверить наличие сторисов на главной странице")
    def check_len_of_stories(self):
        for story in ss(self.list_stories):
            story.should(EC.by_and(be.clickable))
        return self
