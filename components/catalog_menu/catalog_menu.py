from selene import be, have
from selene.core.conditions import Condition as EC
from selene.support.shared.jquery_style import s
from allure import step


class CatalogMenu:
    def __init__(self):
        self.catalog_menu_element = '.menu__wrapper'
        self.smartphones_group_button = 'a[data-link="category-2017"]'
        self.tablets_group_button = 'a[data-link="category-2104"]'
        self.laptops_and_computers_group_button = 'a[data-link="category-2123"]'
        self.smart_watch_and_fitness_group_button = 'a[data-link="category-2146"]'
        self.headphones_group_button = 'a[data-link="category-2169"]'
        self.dyson_products_group_button = 'a[data-link="category-2235"]'
        self.gaming_group_button = 'a[data-link="category-2258"]'
        self.gadgets_group_button = 'a[data-link="category-2281"]'
        self.accessories_group_button = 'a[data-link="category-2350"]'
        self.gifts_group_button = 'a[data-link="category-2741"]'
        self.service_and_support_group_button = 'a[data-link="category-2440"]'
        self.discounts_group_button = 'a[data-link="category-2880"]'

    @step("Наводим курсор на раздел 'Смартфоны'")
    def hover_smartphones_group_button(self) -> 'CatalogMenu':
        s(self.smartphones_group_button).should(EC.by_and(be.clickable, have.text("Смартфоны"))).hover()
        return self

    @step("Наводим курсор на раздел 'Планшеты'")
    def hover_tablets_group_button(self) -> 'CatalogMenu':
        s(self.tablets_group_button).should(EC.by_and(be.clickable, have.text("Планшеты"))).hover()
        return self

    @step("Наводим курсор на раздел 'Ноутбуки и компьютеры'")
    def hover_laptops_and_computers_group_button(self) -> 'CatalogMenu':
        s(self.laptops_and_computers_group_button).should(EC.by_and(
            be.clickable, have.text("Ноутбуки и компьютеры"))).hover()
        return self

    @step("Наводим курсор на раздел 'Умные часы и фитнес-браслеты'")
    def hover_smart_watch_and_fitness_group_button(self) -> 'CatalogMenu':
        s(self.smart_watch_and_fitness_group_button).should(EC.by_and(
            be.clickable, have.text("Умные часы и фитнес-браслеты"))).hover()
        return self

    @step("Наводим курсор на раздел 'Наушники и колонки'")
    def hover_headphones_group_button(self) -> 'CatalogMenu':
        s(self.headphones_group_button).should(EC.by_and(
            be.clickable, have.text("Наушники и колонки"))).hover()
        return self
