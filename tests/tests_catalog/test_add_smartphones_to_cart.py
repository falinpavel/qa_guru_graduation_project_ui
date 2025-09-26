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
class TestAddSmartphonesToCart:
    @allure_mid_level_marks(
        story="Добавление товара в корзину",
        testcase_id="8",
        title="Пользователь добавляет сматрфоны марки Apple iPhone в корзину",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    def test_add_smartphones_by_apple_to_cart(self):
        cm_store.smartphones_page \
            .click_brand_by(brand_name="Apple iPhone") \
            .check_prices_all_smartphones()

    @allure_mid_level_marks(
        story="Добавление товара в корзину",
        testcase_id="10",
        title="Пользователь добавляет сматрфоны марки Samsung в корзину",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    def test_add_smartphones_by_samsung_to_cart(self):
        cm_store.smartphones_page \
            .click_brand_by(brand_name="Samsung") \
            .check_prices_all_smartphones()

    @allure_mid_level_marks(
        story="Добавление товара в корзину",
        testcase_id="11",
        title="Пользователь добавляет сматрфоны марки Xiaomi в корзину",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    def test_add_smartphones_by_xiaomi_to_cart(self):
        cm_store.smartphones_page \
            .click_brand_by(brand_name="Xiaomi") \
            .check_prices_all_smartphones()

    @allure_mid_level_marks(
        story="Добавление товара в корзину",
        testcase_id="12",
        title="Пользователь добавляет сматрфоны марки Google в корзину",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    def test_add_smartphones_by_google_to_cart(self):
        cm_store.smartphones_page \
            .click_brand_by(brand_name="Google") \
            .check_prices_all_smartphones()

    @allure_mid_level_marks(
        story="Добавление товара в корзину",
        testcase_id="13",
        title="Пользователь добавляет сматрфоны марки Honor в корзину",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    def test_add_smartphones_by_honor_to_cart(self):
        cm_store.smartphones_page \
            .click_brand_by(brand_name="Honor") \
            .check_prices_all_smartphones()

    @allure_mid_level_marks(
        story="Добавление товара в корзину",
        testcase_id="14",
        title="Пользователь добавляет сматрфоны марки OnePlus в корзину",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    def test_add_smartphones_by_oneplus_to_cart(self):
        cm_store.smartphones_page \
            .click_brand_by(brand_name="OnePlus") \
            .check_prices_all_smartphones()

    @allure_mid_level_marks(
        story="Добавление товара в корзину",
        testcase_id="15",
        title="Пользователь добавляет сматрфоны марки Nothing в корзину",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    def test_add_smartphones_by_nothing_to_cart(self):
        cm_store.smartphones_page \
            .click_brand_by(brand_name="Nothing") \
            .check_prices_all_smartphones()

    @allure_mid_level_marks(
        story="Добавление товара в корзину",
        testcase_id="16",
        title="Пользователь добавляет сматрфоны марки Asus в корзину",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    def test_add_smartphones_by_asus_to_cart(self):
        cm_store.smartphones_page \
            .click_brand_by(brand_name="Asus") \
            .check_prices_all_smartphones()

    @allure_mid_level_marks(
        story="Добавление товара в корзину",
        testcase_id="17",
        title="Пользователь добавляет сматрфоны марки Nubia в корзину",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    def test_add_smartphones_by_nubia_to_cart(self):
        cm_store.smartphones_page \
            .click_brand_by(brand_name="Nubia") \
            .check_prices_all_smartphones()

    @allure_mid_level_marks(
        story="Добавление товара в корзину",
        testcase_id="18",
        title="Пользователь добавляет сматрфоны марки Huawei в корзину",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    def test_add_smartphones_by_huawei_to_cart(self):
        cm_store.smartphones_page \
            .click_brand_by(brand_name="Huawei") \
            .check_prices_all_smartphones()

    @allure_mid_level_marks(
        story="Добавление товара в корзину",
        testcase_id="19",
        title="Пользователь добавляет сматрфоны марки Motorola в корзину",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    def test_add_smartphones_by_motorola_to_cart(self):
        cm_store.smartphones_page \
            .click_brand_by(brand_name="Motorola") \
            .check_prices_all_smartphones()
