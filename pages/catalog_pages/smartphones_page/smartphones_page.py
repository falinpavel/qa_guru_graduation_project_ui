from selene import browser, be, have, command
from selene.core.conditions import Condition as EC
from selene.support.shared.jquery_style import s
from allure import step

from helpers.links.links import Links


class SmartphonesPage:
    def __init__(self):
        self.smartphones_page_url: str = Links().smartphones_page_url
        self.manufacturer_values_list: list = [
            'Apple iPhone', 'Samsung',
            'Xiaomi', 'Google',
            'Honor', 'OnePlus',
            'Realme', 'Nothing',
            'Asus', 'Nubia',
            'Huawei', 'Motorola',
        ]
        # locators
        self.smartphones_page_title: str = '//h1[text()="Смартфоны"]'
        self.manufacturer_filter: str = '.receipts-block'
        self.manufacturer_one_item: str = '.receipts__item'  # 12 items

    @step("Открываем страницу 'Смартфоны'")
    def open(self) -> 'SmartphonesPage':
        browser.open(self.smartphones_page_url)
        return self

    @step("Проверяем что страница 'Смартфоны' открылась")
    def is_opened(self) -> 'SmartphonesPage':
        s(self.smartphones_page_title).should(EC.by_and(be.visible, have.text("Смартфоны")))
        return self

    @step("Проверяем что бренд отображается в фильтре")
    def check_manufacturer_is_present(self, manufacturer_name: str) -> 'SmartphonesPage':
        s(self.manufacturer_filter).should(EC.by_and(be.visible, have.text(manufacturer_name)))
        return self
