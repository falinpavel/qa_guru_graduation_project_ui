from selene import be, have
from selene.core.conditions import Condition as EC
from selene.support.shared.jquery_style import s
from allure import step


class AuthModal:
    def __init__(self):
        self.auth_modal_sign_in_title: str = '.modal__sign-in-title'
        self.field_phone_number: str = '.input-text_type-3'
        self.sign_in_button: str = '.modal__sign-in-btn'

    @step("Проверяем что модальное окно авторизации отображается")
    def is_opened(self) -> 'AuthModal':
        s(self.auth_modal_sign_in_title).should(EC.by_and(be.visible))
        return self

    @step("Вводим номер телефона")
    def input_phone_number(self, phone_number: str) -> 'AuthModal':
        s(self.field_phone_number).should(EC.by_and(be.clickable)).type(phone_number)
        return self

    @step("Нажимаем кнопку 'Получить код'")
    def click_sign_in_button(self) -> 'AuthModal':
        s(self.sign_in_button).should(EC.by_and(be.clickable, have.value("Получить код"))).click()
        return self
