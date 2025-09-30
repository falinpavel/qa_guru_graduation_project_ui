from selene import be, have
from selene.core.conditions import Condition as EC
from selene.support.shared.jquery_style import s
from allure import step


class HeaderBottomMenu:
    def __init__(self):
        self.logo_button: str = '.header__logo'
        self.catalog_button: str = '.header__bhead-left > a[href="/catalog/"]'
        self.stocks_button: str = '.header__bhead-left > a[href="/stocks/"]'
        self.input_search_field: str = '.header__search-input'
        self.search_button: str = '.header__search-button'
        self.compare_button: str = '.header__controll_compare'
        self.favorites_button: str = '.header__controll_favorites'
        self.cart_button: str = '.header__controll_basket'
        self.profile_button: str = 'div[cmstore_ajax_id="HeaderProfileContent"]'

    @step("Нажимаем на логотип для перехода на главную страницу")
    def click_logo_button(self) -> 'HeaderBottomMenu':
        s(self.logo_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Нажимаем на кнопку 'Каталог' и перейходим на страницу каталога")
    def click_catalog_button(self) -> 'HeaderBottomMenu':
        s(self.catalog_button).should(EC.by_and(be.clickable, have.text("Каталог"))).click()
        return self

    @step("Нажимаем на кнопку 'Акции' и переходим на страницу акций")
    def click_stocks_button(self) -> 'HeaderBottomMenu':
        s(self.stocks_button).should(EC.by_and(be.clickable, have.text("Акции"))).click()
        return self

    @step("Нажимаем на поле ввода поиска по каталогу и вводим свое значение")
    def type_value_in_search_field(self, search_value: str) -> 'HeaderBottomMenu':
        s(self.input_search_field).should(EC.by_and(be.clickable)).click().type(search_value)
        return self

    @step("Нажимаем на кнопку поиска (лупа)")
    def click_search_button(self) -> 'HeaderBottomMenu':
        s(self.search_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Нажимаем на кнопку 'Сравнение'")
    def click_compare_button(self) -> 'HeaderBottomMenu':
        s(self.compare_button).should(EC.by_and(be.clickable))
        return self

    @step("Нажимаем на кнопку 'Избранное'")
    def click_favorites_button(self) -> 'HeaderBottomMenu':
        s(self.favorites_button).should(EC.by_and(be.clickable, have.text("Избранное"))).click()
        return self

    @step("Нажимаем на кнопку 'Корзина'")
    def click_cart_button(self) -> 'HeaderBottomMenu':
        s(self.cart_button).should(EC.by_and(be.clickable, have.text("Корзина"))).click()
        return self

    @step("Нажимаем на кнопку 'Профиль'")
    def click_profile_button(self) -> 'HeaderBottomMenu':
        s(self.profile_button).should(EC.by_and(be.clickable, have.text("Профиль"))).click()
        return self
