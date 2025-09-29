import pytest

from helpers.application_manager.application_manager import cm_store
from utils.allure.allure_custom_labels import allure_high_level_marks, allure_mid_level_marks


@pytest.fixture(scope="function", autouse=True)
def open_smartphones_page(full_opening_home_page):
    cm_store.header_bottom_menu.click_catalog_button()
    cm_store.home_page_catalog_menu.hover_smartphones_group_button(need_click=True)
    cm_store.smartphones_page.open().is_opened()


@allure_high_level_marks(
    epic="Каталог",
    feature="Корзина пользователя"
)
class TestSmartphoneCardsHavePrices:
    @allure_mid_level_marks(
        story="Добавление товара в корзину",
        testcase_id="8",
        title="Пользователь видит цены на смартфоны марки Apple iPhone",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    def test_check_all_card_prices_brand_apple(self):
        cm_store.smartphones_page \
            .click_brand_by(brand_name="Apple iPhone") \
            .check_prices_all_smartphone_cards()

    @allure_mid_level_marks(
        story="Добавление товара в корзину",
        testcase_id="10",
        title="Пользователь видит цены на смартфоны марки Samsung",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    def test_check_all_card_prices_brand_samsung(self):
        cm_store.smartphones_page \
            .click_brand_by(brand_name="Samsung") \
            .check_prices_all_smartphone_cards()

    @allure_mid_level_marks(
        story="Добавление товара в корзину",
        testcase_id="11",
        title="Пользователь видит цены на смартфоны марки Xiaomi",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    def test_check_all_card_prices_brand_xiaomi(self):
        cm_store.smartphones_page \
            .click_brand_by(brand_name="Xiaomi") \
            .check_prices_all_smartphone_cards()

    @allure_mid_level_marks(
        story="Добавление товара в корзину",
        testcase_id="12",
        title="Пользователь видит цены на смартфоны марки Google",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    def test_check_all_card_prices_brand_google(self):
        cm_store.smartphones_page \
            .click_brand_by(brand_name="Google") \
            .check_prices_all_smartphone_cards()

    @allure_mid_level_marks(
        story="Добавление товара в корзину",
        testcase_id="13",
        title="Пользователь видит цены на смартфоны марки Honor",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    def test_check_all_card_prices_brand_honor(self):
        cm_store.smartphones_page \
            .click_brand_by(brand_name="Honor") \
            .check_prices_all_smartphone_cards()

    @allure_mid_level_marks(
        story="Добавление товара в корзину",
        testcase_id="14",
        title="Пользователь видит цены на смартфоны марки OnePlus",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    def test_check_all_card_prices_brand_oneplus(self):
        cm_store.smartphones_page \
            .click_brand_by(brand_name="OnePlus") \
            .check_prices_all_smartphone_cards()

    @allure_mid_level_marks(
        story="Добавление товара в корзину",
        testcase_id="15",
        title="Пользователь видит цены на смартфоны марки Nothing",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    def test_check_all_card_prices_brand_nothing(self):
        cm_store.smartphones_page \
            .click_brand_by(brand_name="Nothing") \
            .check_prices_all_smartphone_cards()

    @allure_mid_level_marks(
        story="Добавление товара в корзину",
        testcase_id="16",
        title="Пользователь видит цены на смартфоны марки Asus",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    def test_check_all_card_prices_brand_asus(self):
        cm_store.smartphones_page \
            .click_brand_by(brand_name="Asus") \
            .check_prices_all_smartphone_cards()

    @allure_mid_level_marks(
        story="Добавление товара в корзину",
        testcase_id="17",
        title="Пользователь видит цены на смартфоны марки Nubia",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    def test_check_all_card_prices_brand_nubia(self):
        cm_store.smartphones_page \
            .click_brand_by(brand_name="Nubia") \
            .check_prices_all_smartphone_cards()

    @allure_mid_level_marks(
        story="Добавление товара в корзину",
        testcase_id="18",
        title="Пользователь видит цены на смартфоны марки Huawei",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    def test_check_all_card_prices_brand_huawei(self):
        cm_store.smartphones_page \
            .click_brand_by(brand_name="Huawei") \
            .check_prices_all_smartphone_cards()

    @allure_mid_level_marks(
        story="Добавление товара в корзину",
        testcase_id="19",
        title="Пользователь видит цены на смартфоны марки Motorola",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    def test_check_all_card_prices_brand_motorola(self):
        cm_store.smartphones_page \
            .click_brand_by(brand_name="Motorola") \
            .check_prices_all_smartphone_cards()
