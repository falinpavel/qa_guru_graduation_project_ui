import pytest

from helpers.application_manager.application_manager import cm_store
from utils.allure.allure_custom_labels import allure_high_level_marks, allure_mid_level_marks


@allure_high_level_marks(
    epic="Главная страница",
    feature="Политика обработки cookies"
)
class TestCookiesMayBeAccepted:
    @allure_mid_level_marks(
        story="Политика обработки соглашения cookies",
        testcase_id="5",
        title="Пользователь при первом посещении (session) имеет пустую корзину",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    @pytest.mark.usefixtures("full_opening_home_page")
    def test_user_may_accept_cookies_politics(self):
        cm_store.header_bottom_menu.click_cart_button()
        cm_store.cart_page \
            .is_opened() \
            .check_cart_is_empty()
