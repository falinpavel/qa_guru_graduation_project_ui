import pytest
import allure_commons
import os

from allure import step
from dotenv import load_dotenv
from selene import browser, support
from selenium import webdriver

from config import options_management
from utils.allure import allure_attachments


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        default="chrome_local",
        choices=[
            "chrome_local",
            "firefox_local",
            "chrome_selenoid",
            "firefox_selenoid"
        ],
        help="Choose where to run the test"
    )


@pytest.fixture(scope="session", autouse=True)
def load_environment():
    load_dotenv()


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope="function", autouse=True)
def browser_settings(context) -> browser:
    options = options_management(context=context)
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )
    with step("Set browser settings"):
        if context == "chrome_selenoid" or context == "firefox_selenoid":
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
    allure_attachments.add_video_from_selenoid(browser) \
        if context == "chrome_selenoid" or context == "firefox_selenoid" else None

    with step("Closing browser"):
        browser.quit()
