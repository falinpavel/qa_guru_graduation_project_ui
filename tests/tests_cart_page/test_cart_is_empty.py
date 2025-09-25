from helpers.application_manager.application_manager import cm_store
from utils.allure.allure_custom_labels import allure_high_level_marks, allure_mid_level_marks


@allure_high_level_marks(
    epic="Корзина пользователя",
    feature="Корзина неавторизованного пользователя"
)
class TestCartIsEmpty:
    @allure_mid_level_marks(
        story="Корзина пользователя по умолчанию пуста",
        testcase_id="1",
        title="Проверяем что корзина пуста",
        label="UI",
        owner="Falin Pavel (AQA)"
    )
    def test_cart_is_empty(self):
        cm_store.cart_page.open().check_cart_is_empty()
