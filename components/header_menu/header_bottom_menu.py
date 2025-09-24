from selene import be, have
from selene.core.conditions import Condition as EC
from selene.support.shared.jquery_style import s
from allure import step


class HeaderBottomMenu:
    def __init__(self):
        self.logo_button = '.header__logo'
        self.catalog_button = '.header__bhead-left > a[href="/catalog/"]'
        self.stocks_button = '.header__bhead-left > a[href="/stocks/"]'
        self.input_search_field = '.header__search-input'
        self.search_button = '.header__search-button'
        self.compare_button = '.header__controll_compare'
        self.favorites_button = '.header__controll_favorites'
        self.cart_button = '.header__controll_basket'
        self.profile_button = 'div[cmstore_ajax_id="HeaderProfileContent"]'

    @step("Нажать на логотип и перейти на главную страницу")
    def click_logo_button(self):
        s(self.logo_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Нажать на кнопку 'Каталог' и перейти на страницу каталога")
    def click_catalog_button(self):
        s(self.catalog_button).should(EC.by_and(be.clickable, have.text("Каталог"))).click()
        return self

    @step("Нажать на кнопку 'Акции' и перейти на страницу акций")
    def click_stocks_button(self):
        s(self.stocks_button).should(EC.by_and(be.clickable, have.text("Акции"))).click()
        return self

    @step("Нажать на поле ввода поиска и ввести значение")
    def input_search_field(self, search_value):
        s(self.input_search_field).should(EC.by_and(be.clickable)).click().type(search_value)
        return self

    @step("Нажать на кнопку поиска")
    def click_search_button(self):
        s(self.search_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Нажать на кнопку 'Сравнение'")
    def click_compare_button(self):
        s(self.compare_button).should(EC.by_and(be.clickable))
        return self

    @step("Нажать на кнопку 'Избранное'")
    def click_favorites_button(self):
        s(self.favorites_button).should(EC.by_and(be.clickable, have.text("Избранное"))).click()
        return self

    @step("Нажать на кнопку корзины")
    def click_cart_button(self):
        s(self.cart_button).should(EC.by_and(be.clickable, have.text("Корзина"))).click()
        return self

    @step("Нажать на кнопку 'Профиль'")
    def click_profile_button(self):
        s(self.profile_button).should(EC.by_and(be.clickable, have.text("Профиль"))).click()
        return self
