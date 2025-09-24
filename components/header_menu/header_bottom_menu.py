from selene import browser, be, have
from selene.core.conditions import Condition as EC
from selene.support.shared.jquery_style import s, ss
from allure import step


class HeaderBottomMenu:
    def __init__(self):
        self.catalog_button = "button[data-qa='header_catalog_nav_open_btn']"
        self.collections_button = ".HeaderBottom_header-bottom-custom_btn-sklv__idrXS"
        self.search_catalog_button = "input[data-qa='header_search_input']"
        self.premium_button = ".HeaderBottom_header-bottom-custom-premium__WCy3w"
        self.promotions_button = ".TopLine_promo-topline__close__NxqbX"
        self.gift_card_button = "a[class='HeaderBottom_header-bottom_right-btn__dxGhi'][href='/gift-card/']"

    @step("Кликнуть на кнопку 'Каталог'")
    def click_catalog_button(self):
        s(self.catalog_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Кликнуть на кнопку 'Коллекции'")
    def click_collections_button(self):
        s(self.collections_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Кликнуть на поле поиска в каталоге")
    def click_search_catalog_button(self):
        s(self.search_catalog_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Кликнуть на кнопку 'Премиум'")
    def click_premium_button(self):
        s(self.premium_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Кликнуть на кнопку 'Промо'")
    def click_promotions_button(self):
        s(self.promotions_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Кликнуть на кнопку 'Подарочная карта'")
    def click_gift_card_button(self):
        s(self.gift_card_button).should(EC.by_and(be.clickable)).click()
        return self
