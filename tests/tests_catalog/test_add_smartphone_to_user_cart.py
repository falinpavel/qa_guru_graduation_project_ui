import pytest

from helpers.application_manager.application_manager import cm_store
from utils.allure.allure_custom_labels import allure_high_level_marks, allure_mid_level_marks


@allure_high_level_marks(
    epic="Каталог/Корзина",
    feature="Добавление товаров в корзину"
)
class TestAddSmartphoneToUserCart:
    @allure_mid_level_marks(
        story="Добавление товара в корзину",
        testcase_id="10",
        title="Пользователь может добавить смартфоны марки Apple iPhone в корзину",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    @pytest.mark.usefixtures("full_opening_home_page")
    @pytest.mark.end_to_end
    @pytest.mark.ui
    @pytest.mark.parametrize(
        "expected_smartphone_name", [
            "Apple iPhone 17 Pro Max 256 ГБ тёмно-синий (1sim + eSim)",
            'Apple iPhone 16 Pro Max 256 ГБ "чёрный титан"',
            'Apple iPhone 16 Pro Max 256 ГБ "пустынный титан"',
            'Apple iPhone 15 128 ГБ чёрный'
        ],
        ids=[
            "Apple iPhone 17 Pro Max 256 GB dark blue",
            'Apple iPhone 16 Pro Max 256 GB black titanium',
            'Apple iPhone 16 Pro Max 256 GB eagle titanium',
            'Apple iPhone 15 128 GB black'
        ]
    )
    @pytest.mark.xfail(reason="JIRA-TASK-123: Флаки тест, кнопка 'Добавить в корзину' срабатывает с большой задержкой")
    def test_add_smartphone_of_brand_apple_iphone_to_user_cart(self, expected_smartphone_name):
        cm_store.header_bottom_menu.click_cart_button()
        cm_store.cart_page \
            .is_opened() \
            .check_cart_is_empty() \
            .return_to_home_page()
        cm_store.header_bottom_menu.click_catalog_button()
        cm_store.home_page_catalog_menu.hover_smartphones_group_button(need_click=True)
        cm_store.smartphones_page \
            .is_opened() \
            .click_brand_by(brand_name="Apple iPhone")
        cm_store.header_bottom_menu \
            .type_value_in_search_field(search_value=expected_smartphone_name) \
            .click_search_button()
        cm_store.smartphones_page \
            .open_card_smartphone_by(smartphone_name=expected_smartphone_name) \
            .click_buy_button_on_one_smartphone_page()
        cm_store.header_bottom_menu \
            .click_logo_button() \
            .click_cart_button()
        cm_store.cart_page \
            .is_opened() \
            .check_product_is_present(product_name=expected_smartphone_name)
