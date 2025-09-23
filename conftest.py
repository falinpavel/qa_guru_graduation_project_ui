import pytest
import allure_commons
import os

from allure import step
from dotenv import load_dotenv
from selene import browser, support
from selenium import webdriver

from config import options_management, ConfigValidator
from utils.allure import allure_attachments


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        default="chrome_local",
        help="Choose where to run the test: chrome_local, firefox_local, chrome_selenoid, firefox_selenoid"
    )


@pytest.fixture(scope="session", autouse=True)
def load_environment():
    load_dotenv()


@pytest.fixture
def context(request) -> str:
    """Возвращает валидированный context"""
    context_value = request.config.getoption("--context")

    try:
        # Валидируем context
        config = ConfigValidator.get_validated_config(context_value)
        return config.context
    except ValueError as e:
        pytest.fail(f"Ошибка валидации параметра --context: {e}")


@pytest.fixture(scope="function", autouse=True)
def browser_settings(context) -> browser:
    # options_management теперь использует валидированный context
    options = options_management(context=context)

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    with step("Set browser settings"):
        if context.endswith("selenoid"):
            driver = webdriver.Remote(
                command_executor=f"https://{os.getenv('LOGIN_SELENOID')}:{os.getenv('PASSWORD_SELENOID')}@selenoid.autotests.cloud/wd/hub",
                options=options
            )
            browser.config.driver = driver
        else:
            browser.config.driver_options = options

    yield

    allure_attachments.add_screenshot_page(browser)
    allure_attachments.add_html_page_source(browser)
    allure_attachments.add_browser_logs(browser)

    if context.endswith("selenoid"):
        allure_attachments.add_video_from_selenoid(browser)

    with step("Closing browser"):
        browser.quit()