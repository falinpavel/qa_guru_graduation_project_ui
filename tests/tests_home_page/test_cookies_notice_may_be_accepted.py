from helpers.application_manager.application_manager import cm_store
from utils.allure.allure_custom_labels import allure_high_level_marks, allure_mid_level_marks


@allure_high_level_marks(
    epic="Главная страница",
    feature="Необходимо отображать плашку с политикой обработки куки"
)
class TestCookiesMayBeAccepted:
    @allure_mid_level_marks(
        story="Пользователь может закрыть плашку с политикой обработки кук, приняв соглашение",
        testcase_id="1",
        title="Пользователь при первом посещении может принять соглашение об обработке кук",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    def test_user_may_accept_cookies_politics(self):
        cm_store.home_page \
            .open() \
            .is_opened() \
            .accept_cookie()
