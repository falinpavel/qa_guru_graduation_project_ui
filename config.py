from pydantic import BaseModel, Field, field_validator
from typing import Literal
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

ContextType = Literal[
    "chrome_local",
    "firefox_local",
    "chrome_selenoid",
    "firefox_selenoid"
]


class BrowserConfig(BaseModel):
    context: ContextType = Field(..., description="Тип контекста запуска")
    browser_name: str
    browser_version: str
    enable_vnc: bool = False
    enable_video: bool = False
    enable_log: bool = False
    window_size: str = "1920,1080"

    @field_validator('browser_name')
    def validate_browser_name(cls, v, values):
        context = values.get('context', '')
        if context.startswith('chrome') and v != 'chrome':
            raise ValueError(f'Для контекста {context} browser_name должен быть "chrome"')
        if context.startswith('firefox') and v != 'firefox':
            raise ValueError(f'Для контекста {context} browser_name должен быть "firefox"')
        return v

    @field_validator('browser_version')
    def validate_browser_version(cls, v):
        if not v.replace('.', '').isdigit():
            raise ValueError('Версия браузера должна содержать только цифры и точки')
        return v


class ConfigValidator:

    @staticmethod
    def get_validated_config(context: str) -> BrowserConfig:
        configs = {
            "chrome_local": BrowserConfig(
                context="chrome_local",
                browser_name="chrome",
                browser_version="128.0",
                enable_vnc=False,
                enable_video=False,
                enable_log=False
            ),
            "firefox_local": BrowserConfig(
                context="firefox_local",
                browser_name="firefox",
                browser_version="125.0",
                enable_vnc=False,
                enable_video=False,
                enable_log=False
            ),
            "chrome_selenoid": BrowserConfig(
                context="chrome_selenoid",
                browser_name="chrome",
                browser_version="128.0",
                enable_vnc=True,
                enable_video=True,
                enable_log=True
            ),
            "firefox_selenoid": BrowserConfig(
                context="firefox_selenoid",
                browser_name="firefox",
                browser_version="125.0",
                enable_vnc=True,
                enable_video=True,
                enable_log=True
            )
        }

        if context not in configs:
            raise ValueError(
                f"Неверное значение context: '{context}'. "
                f"Допустимые значения: {list(configs.keys())}"
            )

        return configs[context]


def options_management(context: str):
    config = ConfigValidator.get_validated_config(context)

    if config.context.startswith("chrome"):
        options = ChromeOptions()
        options.page_load_strategy = 'eager'
        options.add_argument("--disable-gpu")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument(f"--window-size={config.window_size}")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")

        if config.context.endswith("selenoid"):
            options.capabilities.update({
                "browserName": config.browser_name,
                "browserVersion": config.browser_version,
                "selenoid:options": {
                    "enableVNC": config.enable_vnc,
                    "enableVideo": config.enable_video,
                    "enableLog": config.enable_log
                }
            })
        return options

    elif config.context.startswith("firefox"):
        options = FirefoxOptions()
        options.page_load_strategy = 'eager'
        options.add_argument(f"--width={config.window_size.split(',')[0]}")
        options.add_argument(f"--height={config.window_size.split(',')[1]}")
        options.add_argument("--disable-web-security")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--purgecaches")
        options.add_argument("--disable-gpu")

        options.set_preference(name="browser.download.folderList", value=2)
        options.set_preference(name="browser.download.manager.showWhenStarting", value=False)
        options.set_preference(name="browser.helperApps.neverAsk.saveToDisk", value="application/octet-stream")
        options.set_preference(name="browser.download.manager.useWindow", value=False)
        options.set_preference(name="browser.download.manager.focusWhenStarting", value=False)
        options.set_preference(name="browser.download.manager.showAlertOnComplete", value=False)
        options.set_preference(name="browser.download.manager.closeWhenDone", value=True)
        options.set_preference(name="permissions.default.desktop-notification", value=2)
        options.set_preference(name="browser.safebrowsing.malware.enabled", value=True)
        options.set_preference(name="browser.safebrowsing.phishing.enabled", value=True)

        if config.context.endswith("selenoid"):
            options.capabilities.update({
                "browserName": config.browser_name,
                "browserVersion": config.browser_version,
                "selenoid:options": {
                    "enableVNC": config.enable_vnc,
                    "enableVideo": config.enable_video,
                    "enableLog": config.enable_log
                }
            })
        return options
