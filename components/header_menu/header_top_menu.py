from selene import be, have
from selene.core.conditions import Condition as EC
from selene.support.shared.jquery_style import s
from allure import step


class HeaderTopMenu:
    def __init__(self):
        self.location_button = '.header-city__link'
        self.shops_button = '.header__hhead-left > .header__url_mod1'
        self.trade_in_button = '.header__hhead-right > a[href="/trade-in/"]'
        self.payment_and_delivery_button = '.header__hhead-right > a[href="/delivery/"]'
        self.guarantee_button = '.header__hhead-right > a[href="/guarantee/"]'
        self.credit_button = '.header__hhead-right > a[href="/credit/"]'
        self.overview_button = '.header__hhead-right > a[href="/overviews/"]'
        self.service_cm_store_button = '.header__hhead-right > a[href="https://service.cmstore.ru/"]'
        self.phone_button = '.header-phone-menu'
        self.bg_phone_menu = '.header-phone-menu__bg'

    @step("Наживаем на кнопку смены локации")
    def click_location_button(self):
        s(self.location_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Нажимаем на кнопку 'Магазины'")
    def click_shops_button(self):
        s(self.shops_button).should(EC.by_and(be.clickable, have.text("Магазины"))).click()
        return self

    @step("Нажимаем на кнопку 'Trade-in'")
    def click_trade_in_button(self):
        s(self.trade_in_button).should(EC.by_and(be.clickable, have.text("Trade-in"))).click()
        return self

    @step("Нажимаем на кнопку 'Оплата и доставка'")
    def click_payment_and_delivery_button(self):
        s(self.payment_and_delivery_button).should(EC.by_and(be.clickable, have.text("Оплата и доставка"))).click()
        return self

    @step("Нажимаем на кнопку 'Гарантия и возврат'")
    def click_guarantee_button(self):
        s(self.guarantee_button).should(EC.by_and(be.clickable, have.text("Гарантия и возврат"))).click()
        return self

    @step("Нажимаем на кнопку 'Рассрочка и кредит'")
    def click_credit_button(self):
        s(self.credit_button).should(EC.by_and(be.clickable, have.text("Рассрочка и кредит"))).click()
        return self

    @step("Нажимаем на кнопку 'Новости и обзоры'")
    def click_overview_button(self):
        s(self.overview_button).should(EC.by_and(be.clickable, have.text("Новости и обзоры"))).click()
        return self

    @step("Нажимаем на кнопку 'Сервисный центр'")
    def click_service_button(self):
        s(self.service_cm_store_button).should(EC.by_and(be.clickable, have.text("Сервисный центр"))).click()
        return self

    @step("Нажимаем на иконку телефона")
    def click_phone_button(self):
        s(self.phone_button).should(EC.by_and(be.clickable)).click()
        return self
