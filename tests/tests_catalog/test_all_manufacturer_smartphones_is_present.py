import pytest

from helpers.application_manager.application_manager import cm_store
from utils.allure.allure_custom_labels import allure_high_level_marks, allure_mid_level_marks


@allure_high_level_marks(
    epic="Каталог",
    feature="Каталог товаров"
)
class TestAllManufacturerSmartphonesIsPresent:
    @allure_mid_level_marks(
        story="Проверка наличия всех брендов смартфонов",
        testcase_id="9",
        title="Пользователь видит все бренды смартфонов",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    @pytest.mark.usefixtures("full_opening_home_page")
    def test_all_manufacturer_smartphones_is_present(self):
        cm_store.header_bottom_menu.click_catalog_button()
        cm_store.home_page_catalog_menu.hover_smartphones_group_button(need_click=True)
