import pytest
from selenium import webdriver
from pages.main_page import MainPage
from .confdrivers import ConfDrivers
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture(scope="module")
def browser(request):
    """Фикстура для создания объектов webdrivers Chrome или Firefox
                в зависимости от предаваемого аргумента командной строки"""

    # Проверка присутствует ли аргумент --firefox в команде из cmd
    if request.config.getoption("--firefox"):

        print("Открытие браузера Firefox")
        driver = webdriver.Firefox(service=FirefoxService(
            GeckoDriverManager().install()), options=ConfDrivers.options_firefox())
        mp = MainPage(driver)
        mp.go_to_site()

        yield mp

        driver.quit()
        print("Закрытие браузера Firefox")
    else:

        # Если аргумент --firefox отсутствует создается объект вебдрайвера Chrome
        print("Открытие браузера Chrome")
        driver = webdriver.Chrome(service=ChromiumService(
            ChromeDriverManager().install()), options=ConfDrivers.options_chrome())
        mp = MainPage(driver)
        mp.go_to_site()

        yield mp

        driver.quit()
        print("Закрытие браузера Chrome")


def pytest_addoption(parser):
    """Функция для перехвата аргументов командной строки"""

    parser.addoption('--firefox', action='store_true', default=False,
                     help='Параметр --firefox позволяет запустить тесты в браузере Firefox, по умолчанию браузер Chrome')
