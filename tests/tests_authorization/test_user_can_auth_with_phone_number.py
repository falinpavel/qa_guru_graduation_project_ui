import os
import pytest

from helpers.application_manager.application_manager import cm_store
from utils.allure.allure_custom_labels import allure_high_level_marks, allure_mid_level_marks


@allure_high_level_marks(
    epic="Авторизация",
    feature="Авторизация по номеру телефона",
)
class TestUserCanAuthWithPhoneNumber:
    @allure_mid_level_marks(
        story="Авторизация по номеру телефона",
        testcase_id="7",
        title="Проверяем что пользователь может авторизоваться по номеру телефона",
        label="UI",
        owner="Falin Pavel (AQA)",
    )
    @pytest.mark.usefixtures("full_opening_home_page")
    @pytest.mark.smoke
    def test_user_can_auth_with_phone_number(self):
        cm_store.header_bottom_menu.click_profile_button()
        cm_store.auth_modal \
            .is_opened() \
            .input_phone_number(phone_number=os.getenv("PHONE_NUMBER")) \
            .click_sign_in_button()
