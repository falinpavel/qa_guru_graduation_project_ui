import pytest

from helpers.application_manager.application_manager import cm_store


@pytest.fixture(scope="function")
def full_opening_home_page():
    """
    1. Открываем главную страницу
    2. Проверяем что главная страница открылась
    3. Принимаем cookies
    4. Закрываем плашку локации нажимая на крестик
    """
    return cm_store.home_page.open().is_opened().accept_cookie().close_location_box()
