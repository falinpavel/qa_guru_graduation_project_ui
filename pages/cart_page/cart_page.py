from selene import browser, be, have, command
from selene.core.conditions import Condition as EC
from selene.support.shared.jquery_style import s
from allure import step

from helpers.links.links import Links


class CartPage:
    def __init__(self):
        self.cart_page_url: str = Links().cart_page_url
        # locators
        self.return_to_home_page_button: str = 'a[class="header-small__back"] span'
        self.cart_is_empty_message_text: str = '.basket-empty__title'

    @step("Открываем страницу корзины")
    def open(self) -> 'CartPage':
        browser.open(self.cart_page_url)
        return self

    @step("Проверяем что страница корзины открылась")
    def is_opened(self) -> 'CartPage':
        s(self.return_to_home_page_button).should(EC.by_and(be.visible))
        return self

    @step("Возвращаемся на главную страницу по кнопке 'Вернуться к покупкам'")
    def return_to_home_page(self) -> None:
        s(self.return_to_home_page_button).should(EC.by_and(be.clickable)).click()

    @step("Проверяем что корзина пуста")
    def check_cart_is_empty(self) -> 'CartPage':
        s(self.cart_is_empty_message_text).should(EC.by_and(be.visible, have.text("Ваша корзина пуста")))
        return self
