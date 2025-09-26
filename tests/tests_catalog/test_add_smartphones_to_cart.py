from helpers.application_manager.application_manager import cm_store
from utils.allure.allure_custom_labels import allure_high_level_marks, allure_mid_level_marks


@allure_high_level_marks(
    epic="Каталог",
    feature="Корзина пользователя"
)
class TestAddSmartphonesToCart:
    @allure_mid_level_marks(
        story="Добавление товара в корзину",
        testcase_id="8",
        title="Пользователь добавляет сматрфоны марки Apple в корзину",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    def test_add_smartphones_by_apple_to_cart(self):
        pass
