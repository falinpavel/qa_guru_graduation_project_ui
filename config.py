from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Literal, ClassVar
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Определяем допустимые значения для context
ContextType = Literal[
    "chrome_local",
    "firefox_local",
    "chrome_selenoid",
    "firefox_selenoid"
]


class BrowserConfig(BaseModel):
    """Модель для валидации конфигурации браузера"""
    context: ContextType = Field(..., description="Тип контекста запуска")
    browser_name: str
    browser_version: str
    enable_vnc: bool = False
    enable_video: bool = False
    enable_log: bool = False
    window_size: str = "1920,1080"

    @classmethod
    @field_validator('browser_name')
    def validate_browser_name(cls, v: str) -> str:
        """Валидирует имя браузера"""
        if v not in ['chrome', 'firefox']:
            raise ValueError('browser_name должен быть "chrome" или "firefox"')
        return v

    @classmethod
    @field_validator('browser_version')
    def validate_browser_version(cls, v: str) -> str:
        """Валидирует формат версии браузера"""
        if not v.replace(__old='.', __new='').isdigit():
            raise ValueError('Версия браузера должна содержать только цифры и точки')
        return v

    @classmethod
    @field_validator('window_size')
    def validate_window_size(cls, v: str) -> str:
        """Валидирует формат размера окна"""
        parts = v.split(',')
        if len(parts) != 2 or not all(part.isdigit() for part in parts):
            raise ValueError('Размер окна должен быть в формате "width,height" (например, "1920,1080")')
        return v


class BrowserConfigAdvanced(BaseModel):
    """Расширенная модель с межполевой валидацией"""
    context: ContextType = Field(..., description="Тип контекста запуска")
    browser_name: str
    browser_version: str
    enable_vnc: bool = False
    enable_video: bool = False
    enable_log: bool = False
    window_size: str = "1920,1080"

    @classmethod
    @field_validator('browser_name')
    def validate_browser_name(cls, v: str) -> str:
        """Валидирует имя браузера"""
        if v not in ['chrome', 'firefox']:
            raise ValueError('browser_name должен быть "chrome" или "firefox"')
        return v

    @model_validator(mode='after')
    def validate_context_consistency(self) -> 'BrowserConfigAdvanced':
        """Валидирует согласованность context и browser_name"""
        context = self.context
        browser_name = self.browser_name

        if context.startswith('chrome') and browser_name != 'chrome':
            raise ValueError(f'Для контекста {context} browser_name должен быть "chrome"')

        if context.startswith('firefox') and browser_name != 'firefox':
            raise ValueError(f'Для контекста {context} browser_name должен быть "firefox"')

        # Дополнительная логика для selenoid
        if context.endswith('selenoid'):
            if not self.enable_vnc:
                raise ValueError('Для Selenoid контекста enable_vnc должен быть True')

        return self


class ConfigValidator:
    """Класс для валидации конфигурации"""

    # Базовые настройки для каждого типа контекста
    CONFIG_MAP: ClassVar[dict] = {
        "chrome_local": {
            "context": "chrome_local",
            "browser_name": "chrome",
            "browser_version": "128.0",
            "enable_vnc": False,
            "enable_video": False,
            "enable_log": False
        },
        "firefox_local": {
            "context": "firefox_local",
            "browser_name": "firefox",
            "browser_version": "125.0",
            "enable_vnc": False,
            "enable_video": False,
            "enable_log": False
        },
        "chrome_selenoid": {
            "context": "chrome_selenoid",
            "browser_name": "chrome",
            "browser_version": "128.0",
            "enable_vnc": True,
            "enable_video": True,
            "enable_log": True
        },
        "firefox_selenoid": {
            "context": "firefox_selenoid",
            "browser_name": "firefox",
            "browser_version": "125.0",
            "enable_vnc": True,
            "enable_video": True,
            "enable_log": True
        }
    }

    @classmethod
    def get_validated_config(cls, context: str) -> BrowserConfig:
        """Валидирует context и возвращает конфигурацию"""

        if context not in cls.CONFIG_MAP:
            raise ValueError(
                f"Неверное значение context: '{context}'. "
                f"Допустимые значения: {list(cls.CONFIG_MAP.keys())}"
            )

        config_data = cls.CONFIG_MAP[context]
        return BrowserConfig(**config_data)


def options_management(context: str):
    """Создает опции браузера с валидацией параметров"""

    # Валидируем конфигурацию
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
        width, height = config.window_size.split(',')
        options.add_argument(f"--width={width}")
        options.add_argument(f"--height={height}")
        options.add_argument("--disable-web-security")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--purgecaches")
        options.add_argument("--disable-gpu")

        # Настройки для Firefox
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
