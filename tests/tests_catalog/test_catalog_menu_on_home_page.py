import pytest

from helpers.application_manager.application_manager import cm_store
from utils.allure.allure_custom_labels import allure_high_level_marks, allure_mid_level_marks


@allure_high_level_marks(
    epic="Каталог",
    feature="Каталог на главной странице",
)
class TestCatalogMenuOnHomePage:
    @allure_mid_level_marks(
        story="Каталог на главной странице отображается",
        testcase_id="6",
        title="Наведение курсора на разделы каталога и навигация по нему",
        label="UI",
        owner="Falin Pavel (AQA)",
    )
    @pytest.mark.usefixtures("full_opening_home_page")
    @pytest.mark.smoke
    def test_catalog_menu_on_home_page_is_present(self):
        cm_store.header_bottom_menu.click_catalog_button()
        cm_store.home_page_catalog_menu \
            .catalog_menu_is_opened() \
            .hover_smartphones_group_button() \
            .hover_tablets_group_button() \
            .hover_laptops_and_computers_group_button() \
            .hover_smart_watch_and_fitness_group_button() \
            .hover_headphones_group_button() \
            .hover_dyson_products_group_button() \
            .hover_gaming_group_button() \
            .hover_gadgets_group_button() \
            .hover_accessories_group_button() \
            .hover_gifts_group_button() \
            .hover_service_and_soft_group_button() \
            .hover_discounts_group_button()
