from selene import browser, be, have, command
from selene.core.conditions import Condition as EC
from selene.support.shared.jquery_style import s, ss
from allure import step

from helpers.links.links import Links


class SmartphonesPage:
    def __init__(self):
        self.smartphones_page_url: str = Links().smartphones_page_url
        self.brand_values_list: list = [
            'Apple iPhone', 'Samsung',
            'Xiaomi', 'Google',
            'Honor', 'OnePlus',
            'Realme', 'Nothing',
            'Asus', 'Nubia',
            'Huawei', 'Motorola',
        ]
        # locators
        self.smartphones_page_title: str = '//h1[text()="Смартфоны"]'
        self.brand_filter: str = '.receipts-block'
        self.brand_one_smartphone_by_name: str = '//div/a[text()="{brand_name}"]'
        self.card_list_of_smartphones: str = '//div[@class="catalog-body__inner"]'
        self.card_smartphone_by_name: str = '//a[contains(text(),"{smartphone_name}")]'
        self.card_smartphone_price: str = '.catalog-body__price'
        self.card_buy_button: str = '.catalog-body__basket'
        self.one_smartphone_page_bye_button = '.cart-purchase__buy-button'

    @step("Открываем страницу 'Смартфоны'")
    def open(self) -> 'SmartphonesPage':
        browser.open(self.smartphones_page_url)
        return self

    @step("Проверяем что страница 'Смартфоны' открылась")
    def is_opened(self) -> 'SmartphonesPage':
        s(self.smartphones_page_title).should(EC.by_and(be.visible, have.text("Смартфоны")))
        return self

    @step("Проверяем что бренд отображается в фильтре")
    def check_that_brand_is_present(self, brand_name: str) -> 'SmartphonesPage':
        s(self.brand_filter).should(EC.by_and(be.visible, have.text(brand_name)))
        return self

    @step("Кликаем на наименование бренда")
    def click_brand_by(self, brand_name: str) -> 'SmartphonesPage':
        s(self.brand_one_smartphone_by_name.format(brand_name=brand_name)).should(
            EC.by_and(be.clickable, have.text(brand_name))).click()
        return self

    @step("Кликаем на кнопку 'В корзину'")
    def click_buy_button(self) -> 'SmartphonesPage':
        s(self.card_buy_button).with_(timeout=browser.config.timeout * 2).should(EC.by_and(be.clickable, have.text("В корзину"))).click()
        return self

    @step("Проверяем что все товары имеют цену и она не равна нулю")
    def check_prices_all_smartphone_cards(self) -> 'SmartphonesPage':
        for smartphone in ss(self.card_list_of_smartphones):
            smartphone.perform(command.js.scroll_into_view).s(self.card_smartphone_price).should(
                EC.by_and(be.visible, be.not_.blank)
            )
        return self

    @step("Открываем карточку определенного товара по его наименованию")
    def open_card_smartphone_by(self, smartphone_name) -> 'SmartphonesPage':
        s(self.card_smartphone_by_name.format(smartphone_name=smartphone_name)).should(
            EC.by_and(be.clickable, have.text(smartphone_name))).click()
        return self

    @step("Кликаем на кнопку 'Добавить в корзину' на странице карточки товара")
    def click_buy_button_on_one_smartphone_page(self) -> 'SmartphonesPage':
        ss(self.one_smartphone_page_bye_button).first.should(EC.by_and(be.present, be.clickable)).hover().click()
        return self
