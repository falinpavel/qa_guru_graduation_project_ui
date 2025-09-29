import pytest

from helpers.application_manager.application_manager import cm_store
from utils.allure.allure_custom_labels import allure_high_level_marks, allure_mid_level_marks


@allure_high_level_marks(
    epic="Каталог",
    feature="Каталог товаров"
)
class TestAllManufacturerSmartphonesIsPresent:
    @allure_mid_level_marks(
        story="Все бренды смартфонов должны быть представлены на странице",
        testcase_id="9",
        title="Пользователь видит все бренды смартфонов",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    @pytest.mark.usefixtures("full_opening_home_page")
    @pytest.mark.regression
    @pytest.mark.ui
    @pytest.mark.parametrize(
        "expected_manufacturer", [
            'Apple iPhone', 'Samsung',
            'Xiaomi', 'Google',
            'Honor', 'OnePlus',
            'Realme', 'Nothing',
            'Asus', 'Nubia',
            'Huawei', 'Motorola',
        ]
    )
    def test_all_manufacturer_smartphones_is_present(self, expected_manufacturer):
        cm_store.header_bottom_menu.click_catalog_button()
        cm_store.home_page_catalog_menu.hover_smartphones_group_button(need_click=True)
        cm_store.smartphones_page \
            .is_opened() \
            .check_that_brand_is_present(brand_name=expected_manufacturer)
