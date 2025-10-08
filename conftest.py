"""
Этот модуль предоставляет фикстуры и конфигурацию pytest для автоматизированного
тестирования с использованием Selene и Selenium WebDriver. Включает настройку
окружения, конфигурацию браузера и интеграцию с Allure отчетностью с поддержкой
нескольких контекстов выполнения.

Модуль поддерживает четыре контекста выполнения:
- chrome_local: Локальный запуск Chrome браузера
- firefox_local: Локальный запуск Firefox браузера
- chrome_selenoid: Удаленный запуск Chrome через Selenoid
- firefox_selenoid: Удаленный запуск Firefox через Selenoid

Ключевые возможности:
- Динамическая конфигурация браузера на основе параметров командной строки
- Управление переменными окружения через dotenv
- Автоматическая генерация Allure отчетов со скриншотами, HTML исходниками, логами и видео
- Полное управление жизненным циклом браузера
- Валидация параметров запуска с использованием Pydantic моделей

Зависимости:
- pytest: Фреймворк для тестирования
- selene: Библиотека для автоматизации браузеров
- selenium: WebDriver
- allure-pytest: Генерация отчетов
- python-dotenv: Управление переменными окружения

Пример использования:
    pytest tests/ --context=chrome_selenoid --alluredir=reports
    pytest tests/ --context=firefox_local -v
"""

import pytest
import allure_commons
import os

from allure import step
from dotenv import load_dotenv
from selene import browser, support
from selenium import webdriver

from config import options_management, ConfigValidator
from utils.allure import allure_attachments


def pytest_addoption(parser: pytest.Parser) -> None:
    """
        Добавляет пользовательские параметры командной строки в конфигурацию pytest.

        Эта функция-хук расширяет pytest параметром --context, который позволяет
        указать среду выполнения браузера. Параметр используется для определения
        того, будут ли тесты запускаться локально или удаленно, и какой браузер использовать.

        Args:
            parser (pytest.Parser): Экземпляр парсера аргументов pytest.

        Добавляемые параметры:
            --context: Определяет контекст выполнения браузера с четырьмя возможными значениями:
                - chrome_local: Локальный браузер Chrome
                - firefox_local: Локальный браузер Firefox
                - chrome_selenoid: Удаленный Chrome через Selenoid
                - firefox_selenoid: Удаленный Firefox через Selenoid
        """
    parser.addoption(
        "--context",
        default="chrome_local",
        help=(
            "Выбор среды выполнения тестов: "
            "chrome_local, firefox_local, chrome_selenoid, firefox_selenoid. "
            "Определяет тип браузера и среду выполнения (локальная/удаленная)."
        )
    )


@pytest.fixture(scope="session", autouse=True)
def load_environment() -> None:
    """
    Фикстура уровня сессии для автоматической загрузки переменных окружения.

    Загружает переменные окружения из .env файлов с использованием python-dotenv. Она гарантирует,
    что все необходимые переменные окружения (такие как учетные данные Selenoid)
    доступны на протяжении всего выполнения тестов.

    Scope:
        session: Выполняется один раз за тестовую сессию

    Autouse:
        True: Автоматически используется всеми тестами без явного объявления

    Загружаемые файлы:
        - .env: Основной файл переменных окружения

    Пример переменных окружения:
        LOGIN_SELENOID=user@example.com
        PASSWORD_SELENOID=secret_password
        BROWSER_VERSION=128.
    """
    load_dotenv()


@pytest.fixture
def context(request: pytest.FixtureRequest) -> str:
    """
    Фикстура для получения и валидации параметра --context.

    Эта фикстура извлекает значение параметра --context из командной строки,
    валидирует его с использованием ConfigValidator и возвращает валидированный
    контекст. В случае невалидного значения тест завершается с ошибкой.

    Args:
        request (pytest.FixtureRequest): Объект запроса фикстуры, предоставляющий
            доступ к конфигурации теста и параметрам командной строки.

    Returns:
        str: Валидированное значение контекста выполнения.

    Raises:
        pytest.fail: Если значение контекста не прошло валидацию.

    Пример использования в тесте:
        def test_example(context):
            # context будет содержать валидированное значение, например "chrome_selenoid"
            if context.endswith("selenoid"):
                # Логика для удаленного выполнения
                pass
    """
    context_value = request.config.getoption("--context")

    try:
        # Валидируем контекст через ConfigValidator
        config = ConfigValidator.get_validated_config(context_value)
        return config.context
    except ValueError as e:
        # Завершаем тест с понятным сообщением об ошибке
        pytest.fail(f"Ошибка валидации параметра --context: {e}")


@pytest.fixture(scope="function", autouse=True)
def browser_settings(context) -> browser:
    """
    Основная фикстура для настройки и управления браузером.

    Эта фикстура автоматически настраивает браузер перед каждым тестом и выполняет
    очистку после завершения теста. Она обеспечивает:
    - Инициализацию браузера с правильными настройками
    - Интеграцию с Allure для красивого логирования шагов
    - Автоматическое создание скриншотов и артефактов
    - Корректное завершение сессии браузера

    Args:
        context (str): Валидированный контекст выполнения, полученный из фикстуры context.

    Yields:
        browser: Настроенный экземпляр браузера Selene для использования в тестах.

    Фикстура выполняет следующие этапы:
    1. Настройка браузера перед тестом
    2. Передача управления тесту (yield)
    3. Сбор артефактов после теста
    4. Завершение сессии браузера

    Логика настройки браузера:
        - Для локальных контекстов: настройка локального WebDriver
        - Для Selenoid контекстов: инициализация удаленного WebDriver

    Сбор артефактов после теста:
        - Скриншот текущей страницы
        - Исходный HTML код страницы
        - Логи браузера
        - Видео записи (только для Selenoid)
    """
    # Получаем настройки браузера на основе валидированного контекста
    options = options_management(context=context)

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    with step("Настройка параметров браузера"):
        if context.endswith("selenoid"):
            driver = webdriver.Remote(
                command_executor=(
                    f"https://{os.getenv('LOGIN_SELENOID')}:"
                    f"{os.getenv('PASSWORD_SELENOID')}@"
                    f"selenoid.autotests.cloud/wd/hub"
                ),
                options=options
            )
            browser.config.driver = driver
        else:
            # Настройка локального WebDriver
            browser.config.driver_options = options

    yield

    allure_attachments.add_screenshot_page(browser)
    allure_attachments.add_html_page_source(browser)
    allure_attachments.add_browser_logs(browser)

    if context.endswith("selenoid"):
        allure_attachments.add_video_from_selenoid(browser)

    with step("Закрытие браузера"):
        browser.quit()
