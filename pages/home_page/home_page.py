from selene import browser, be, have, command
from selene.core.conditions import Condition as EC
from selene.support.shared.jquery_style import s
from allure import step

from helpers.links.links import Links


class HomePage:
    def __init__(self):
        self.base_url = Links().base_url
        # locators
        self.close_widget_button = '.closeIcon__TO5Xx'
        self.accept_cookie_button = '.cookie-notice__content > .button'
        self.slider = '.home-hero__slider'
        self.slider_swipe_left_button = '.home-hero__nav_prev'
        self.slider_swipe_right_button = '.home-hero__nav_next'
        self.section_categories = '.category-section__inner'
        self.category_button_by_name = '//div[@class="category-section__inner"]//span[text()="{category_name}"]'
        self.section_sales = '.sales-container'
        self.view_all_stocks_button = '.promotions'
        self.close_location_button = '.header-city__question-button-close'
        self.location_name_button = '.header-city__link'
        self.modal_location_name_button = '//div[@class="city-search__content"]//a[contains(text(), "{location_name}")]'

    @step("Открываем главную страницу")
    def open(self) -> 'HomePage':
        browser.open(self.base_url)
        return self

    @step("Проверяем что главная страница открылась")
    def is_opened(self) -> 'HomePage':
        s(self.slider).should(EC.by_and(be.visible))
        return self

    @step("Закрываем плашку локации нажимая на крестик")
    def close_location_box(self) -> 'HomePage':
        s(self.close_location_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Проверяем наименование локации (по умолчанию Москва)")
    def check_location_name(self, location_name: str = "Москва") -> 'HomePage':
        s(self.location_name_button).should(EC.by_and(be.visible, have.text(location_name)))
        return self

    @step("Открываем модальное окно и выбираем новую локацию из списка")
    def change_location_from_present_list(self, location_name: str) -> 'HomePage':
        s(self.modal_location_name_button.format(location_name=location_name)).should(EC.by_and(be.clickable)).click()
        return self

    @step("Закрываем виджет 'Напишите нам...'")
    def close_widget(self) -> 'HomePage':
        s(self.close_widget_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Принимаем cookies")
    def accept_cookie(self) -> 'HomePage':
        s(self.accept_cookie_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Проверяем что плашка cookies исчезла")
    def check_cookie_is_disappeared(self) -> 'HomePage':
        s(self.accept_cookie_button).should(EC.by_and(be.not_.visible))
        return self

    @step("Проверяем что раздел 'Категории' отображается")
    def check_section_categories_is_displayed(self) -> 'HomePage':
        s(self.section_categories).should(EC.by_and(be.visible))
        return self

    @step("Переходим на главном меню в категорию, нажав на ее наименование")
    def click_category_by(self, category_name: str) -> 'HomePage':
        s(self.category_button_by_name.format(category_name=category_name)).should(
            EC.by_and(be.clickable)).click()
        return self
