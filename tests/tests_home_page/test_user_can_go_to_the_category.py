import pytest

from helpers.application_manager.application_manager import cm_store
from utils.allure.allure_custom_labels import allure_high_level_marks, allure_mid_level_marks


@allure_high_level_marks(
    epic="Главная страница",
    feature="Категории"
)
class TestUserCanGoToTheCategory:
    @allure_mid_level_marks(
        story="Пользователь может перейти в категорию",
        testcase_id="2",
        title="Пользователь может перейти в категорию через главную страницу",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    @pytest.mark.parametrize(
        "category_name", [
            "Смартфоны", "Планшеты", "Ноутбуки и компьютеры", "Умные часы и фитнес-браслеты", "Наушники и колонки",
            "Продукция Dyson", "Гейминг", "Гаджеты", "Аксессуары", "Услуги и софт"
        ],
        ids=[
            "Smartphones", "Tablets", "Laptops and Computers", "Smartwatches and Fitness bracelets",
            "Headphones and Speakers", "Dyson Products", "Gaming", "Gadgets", "Accessories", "Services and Software"
        ]
    )
    def test_user_can_go_to_the_category_from_home_page(self, category_name):
        cm_store.home_page \
            .open() \
            .is_opened() \
            .accept_cookie() \
            .close_location_box() \
            .check_section_categories_is_displayed() \
            .click_category_by(category_name=category_name)
