from helpers.application_manager.application_manager import sokolov_app
from utils.allure.allure_custom_labels import allure_high_level_marks


@allure_high_level_marks(epic="Главная страница", feature="Проверка наличия сторис")
class TestStoriesIsPresent:
    def test_stories_is_present(self):
        sokolov_app.home_page \
            .open() \
            .is_opened() \
            .check_len_of_stories()
