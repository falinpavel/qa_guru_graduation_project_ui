import pytest

from helpers.application_manager.application_manager import cm_store
from utils.allure.allure_custom_labels import allure_high_level_marks, allure_mid_level_marks


@allure_high_level_marks(
    epic="Корзина пользователя",
    feature="Корзина неавторизованного пользователя"
)
class TestCartIsEmpty:
    @allure_mid_level_marks(
        story="Корзина пользователя по умолчанию пуста",
        testcase_id="5",
        title="Проверяем что корзина пуста",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    @pytest.mark.usefixtures("full_opening_home_page")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.ui
    def test_cart_is_empty_by_default(self):
        cm_store.header_bottom_menu.click_cart_button()
        cm_store.cart_page \
            .is_opened() \
            .check_cart_is_empty()
