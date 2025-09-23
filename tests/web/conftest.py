import os
import pytest

from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from utils.allure import allure_attachments
from const import ConstPath, ConstBrowser


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default=ConstBrowser.DEFAULT_BROWSER_VERSION,
        help=f"Choose browser version (default: {ConstBrowser.DEFAULT_BROWSER_VERSION})"
    )
    parser.addoption(
        "--browser-type",
        help=f"Choose browser type (default: {ConstBrowser.DEFAULT_BROWSER_TYPE})",
        choices=["chrome", "firefox"],
        required=False,
        default=ConstBrowser.DEFAULT_BROWSER_TYPE
    )


@pytest.fixture(scope="session", autouse=True)
def load_environment():
    load_dotenv()


@pytest.fixture(scope="function", autouse=True)
def browser_options(request):

    browser_type = request.config.getoption("--browser-type")

    if browser_type == "chrome":

        driver_options = ChromeOptions()

        driver_options.page_load_strategy = 'eager'

        driver_options.add_argument("--disable-gpu")
        driver_options.add_argument("--ignore-certificate-errors")
        driver_options.add_argument("--window-size=1920,1080")
        driver_options.add_argument("--disable-extensions")
        driver_options.add_argument("--disable-popup-blocking")
        driver_options.add_argument("--disable-notifications")
        driver_options.add_argument("--disable-infobars")

        prefs = {
            "profile.default_content_settings.popups": 0,
            "profile.default_content_setting_values.notifications": 2,
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "download.default_directory": ConstPath.RESOURCES_DIR,
            "download.prompt_for_download": False,
            "safebrowsing.enabled": True
        }
        driver_options.add_experimental_option(name="prefs", value=prefs)

        browser_version = request.config.getoption("--browser_version")
        browser_version = browser_version if browser_version else ConstBrowser.DEFAULT_BROWSER_VERSION

        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": browser_version,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True,
                "enableLog": True
            }
        }

        driver_options.capabilities.update(selenoid_capabilities)

        driver = webdriver.Remote(
            command_executor=f"https://{os.getenv('LOGIN')}:{os.getenv('PASSWORD')}@selenoid.autotests.cloud/wd/hub",
            options=driver_options
        )

        browser.config.driver = driver

    if browser_type == "firefox":

        driver_options = FirefoxOptions()

        driver_options.page_load_strategy = 'eager'

        driver_options.add_argument("--width=1920")
        driver_options.add_argument("--height=1080")
        driver_options.add_argument("--disable-web-security")
        driver_options.add_argument("--allow-running-insecure-content")
        driver_options.add_argument("--purgecaches")
        driver_options.add_argument("--disable-gpu")

        driver_options.set_preference("browser.download.folderList", 2)
        driver_options.set_preference("browser.download.dir", ConstPath.RESOURCES_DIR)
        driver_options.set_preference("browser.download.manager.showWhenStarting", False)
        driver_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
        driver_options.set_preference("browser.download.manager.useWindow", False)
        driver_options.set_preference("browser.download.manager.focusWhenStarting", False)
        driver_options.set_preference("browser.download.manager.showAlertOnComplete", False)
        driver_options.set_preference("browser.download.manager.closeWhenDone", True)

        driver_options.set_preference("permissions.default.desktop-notification", 2)

        driver_options.set_preference("browser.safebrowsing.malware.enabled", True)
        driver_options.set_preference("browser.safebrowsing.phishing.enabled", True)

        selenoid_capabilities = {
            "browserName": "firefox",
            "browserVersion": request.config.getoption("--browser_version"),
            "selenoid:options": {
                "enableVideo": False
            }
        }

        driver_options.capabilities.update(selenoid_capabilities)

        driver = webdriver.Remote(
            command_executor=f"https://{os.getenv('LOGIN')}:{os.getenv('PASSWORD')}@selenoid.autotests.cloud/wd/hub",
            options=driver_options
        )

        browser.config.driver = driver

    yield

    allure_attachments.add_screenshot_page(browser=browser)
    allure_attachments.add_browser_logs(browser=browser)
    allure_attachments.add_html_page_source(browser=browser)
    allure_attachments.add_video_from_selenoid(browser=browser)

    browser.quit()

# BROWSER FOR LOCAL RUN ////////////////////////////////////////////////////////////////////////////////////////////////

# import pytest
#
# from selene import browser
# from selenium.webdriver.chrome.options import Options
#
# from utils import allure_attachments
#
#
# @pytest.fixture(scope='function', autouse=True)
# def setup_browser():
#     chrome_options = Options()
#
#     prefs = {
#         "profile.default_content_settings.popups": 0,
#         "profile.default_content_setting_values.notifications": 2,
#         "profile.default_content_setting_values.geolocation": 2,  # 2 = Block
#         "profile.managed_default_content_settings.geolocation": 2
#     }
#     chrome_options.add_experimental_option(name="prefs", value=prefs)
#
#     chrome_options.page_load_strategy = 'eager'
#
#     chrome_options.add_argument("--disable-geolocation")
#     chrome_options.add_argument("--disable-features=Geolocation")
#     chrome_options.add_argument("--ignore-certificate-errors")
#     chrome_options.add_argument("--window-size=1920,1080")
#     # chrome_options.add_argument("--start-fullscreen")
#     # chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--disable-extensions")
#     chrome_options.add_argument("--disable-popup-blocking")
#     chrome_options.add_argument("--disable-notifications")
#     chrome_options.add_argument("--disable-infobars")
#
#     browser.config.driver_options = chrome_options
#
#     yield
#
#     allure_attachments.add_screenshot(browser=browser)
#     allure_attachments.add_logs(browser=browser)
#     allure_attachments.add_html(browser=browser)
#     allure_attachments.add_video(browser=browser)
#
#     browser.quit()
