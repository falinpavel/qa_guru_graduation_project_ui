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
        testcase_id="1",
        title="Пользователь при первом посещении (session) может принять соглашение об обработке кук",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_user_may_accept_cookies_politics(self):
        cm_store.home_page \
            .open() \
            .is_opened() \
            .accept_cookie() \
            .check_cookie_is_disappeared()
