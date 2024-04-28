import pytest
from selenium import webdriver
from pages.main_page import MainPage
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as Options_chrome
from selenium.webdriver.firefox.options import Options as Options_firefox
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture(scope="session")
def browser(request):
    if request.config.getoption("--firefox"):
        firefox_options = Options_firefox()
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--width=1980")
        firefox_options.add_argument("--height=1080")

        print("Открытие браузера Firefox")
        driver = webdriver.Firefox(service=FirefoxService(
            GeckoDriverManager().install()), options=firefox_options)
        mp = MainPage(driver)
        mp.go_to_site()

        yield mp

        driver.quit()
        print("Закрытие браузера Firefox")
    else:
        chrome_options = Options_chrome()
        chrome_options.add_argument("--window-size=1980,1080")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--headless")

        print("Открытие браузера Chrome")
        driver = webdriver.Chrome(service=ChromiumService(
            ChromeDriverManager().install()), options=chrome_options)
        mp = MainPage(driver)
        mp.go_to_site()

        yield mp

        driver.quit()
        print("Закрытие браузера Chrome")


def pytest_addoption(parser):
    """Command line arguments"""
    parser.addoption('--firefox', action='store_true', default=False,
                     help='Параметр --firefox позваляет запустить тесты в браузере Firefox, по умолчанию браузер Chrome')
