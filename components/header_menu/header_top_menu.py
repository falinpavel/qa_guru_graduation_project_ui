from selene import browser, be, have
from selene.core.conditions import Condition as EC
from selene.support.shared.jquery_style import s, ss
from allure import step


class HeaderTopMenu:
    def __init__(self):
        self.close_promo_button = ".TopLine_promo-topline__close__NxqbX"
        self.logo_home_page = ".HeaderTop_header-top-logo__zO0BT"
        self.location_button = ".HeaderTop_header-country__DY_Tl"
        self.stores_button = ".HeaderTop_header-top_left-stores__Kx_de"
        self.payment_delivery_button = ".HeaderTop_header-top_left-delivery-link__FoJTX"
        self.favorites_button = "button[data-qa='header_favorites_btn']"
        self.basket_button = "button[data-qa='header_to_basket_btn']"
        self.user_login_button = "button[data-qa='header_user_login_btn']"

    @step("Закрыть в хедере плашку с промо")
    def close_promo_top_line(self):
        s(self.close_promo_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Кликнуть на логотип для возврата на главную страницу")
    def click_logo_for_return_to_home_page(self):
        s(self.logo_home_page).should(EC.by_and(be.clickable)).click()
        return self

    @step("Кликнуть на кнопку выбора локации")
    def click_location_button(self):
        s(self.location_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Кликнуть на кнопку 'Магазины'")
    def click_stores_button(self):
        s(self.stores_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Кликнуть на кнопку 'Доставка и оплата'")
    def click_payment_and_delivery_button(self):
        s(self.payment_delivery_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Кликнуть на кнопку 'Избранное'")
    def click_favorites_button(self):
        s(self.favorites_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Кликнуть на кнопку 'Корзина'")
    def click_basket_button(self):
        s(self.basket_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Кликнуть на кнопку 'Войти'")
    def click_user_login_button(self):
        s(self.user_login_button).should(EC.by_and(be.clickable)).click()
        return self
