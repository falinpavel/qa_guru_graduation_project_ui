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
        title="Пользователь может добавить товар в корзину",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    @pytest.mark.usefixtures("full_opening_home_page")
    @pytest.mark.end_to_end
    @pytest.mark.ui
    def test_add_smartphone_of_brand_apple_iphone_to_user_cart(self):
        cm_store.header_bottom_menu.click_catalog_button()
        cm_store.home_page_catalog_menu.hover_smartphones_group_button(need_click=True)
        cm_store.smartphones_page \
            .is_opened() \
            .click_brand_by(brand_name="Apple iPhone")
        cm_store.smartphones_page \
            .open_card_smartphone_by(smartphone_name="Apple iPhone 17 Pro Max 256 ГБ тёмно-синий") \
            .click_buy_button_on_one_smartphone_page()
