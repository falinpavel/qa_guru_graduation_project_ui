import pytest

from helpers.application_manager.application_manager import cm_store


@pytest.fixture(scope="function")
def full_opening_home_page():
    return cm_store.home_page.open().is_opened().accept_cookie().close_location_box()
