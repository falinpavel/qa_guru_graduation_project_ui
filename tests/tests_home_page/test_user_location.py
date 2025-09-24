import pytest

from helpers.application_manager.application_manager import cm_store
from utils.allure.allure_custom_labels import allure_high_level_marks, allure_mid_level_marks


@allure_high_level_marks(
    epic="Главная страница",
    feature="Локация пользователя"
)
class TestUserLocation:
    @allure_mid_level_marks(
        story="Москва является предопределенной локацией пользователя и выставляется по умолчанию",
        testcase_id="3",
        title="Пользователю по умолчанию присваивается локация Москва",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    @pytest.mark.usefixtures("full_opening_home_page")
    def test_default_user_location_is_moscow(self):
        cm_store.home_page \
            .check_location_name()

    @allure_mid_level_marks(
        story="Пользователь может изменить предопределенную локацию",
        testcase_id="4",
        title="Пользователь может изменить локацию из предложенного списка в модальном окне",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    @pytest.mark.parametrize(
        "new_location", [
            "Краснодар", "Сочи", "Анапа", "Екатеринбург", "Ханты-Мансийск", "Воронеж"
        ],
        ids=[
            "Krasnodar", "Sochi", "Anapa", "Ekaterinburg", "Chanty-Mansiysk", "Voronedj"
        ]
    )
    @pytest.mark.usefixtures("full_opening_home_page")
    def test_user_can_change_new_location_from_present_list(self, new_location):
        cm_store.home_page.check_location_name()
        cm_store.header_top_menu.click_location_button()
        cm_store.home_page.change_location_from_present_list(location_name=new_location)
        cm_store.home_page.check_location_name(location_name=new_location)
