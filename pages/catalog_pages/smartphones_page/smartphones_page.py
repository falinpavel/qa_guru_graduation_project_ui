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
        self.card_smartphone_price: str = '.catalog-body__price'

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

    @step("Проверяем что все товары имеют цену и она не равна нулю")
    def check_prices_all_smartphones(self) -> 'SmartphonesPage':
        for smartphone in ss(self.card_list_of_smartphones):
            smartphone.perform(command.js.scroll_into_view).s(self.card_smartphone_price).should(
                EC.by_and(be.visible, be.not_.blank))
        return self
