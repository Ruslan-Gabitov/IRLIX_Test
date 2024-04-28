import pytest
from selenium import webdriver
from pages.main_page import MainPage
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromiumService


@pytest.fixture(scope="session")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1980,1080")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--headless")

    print("Открытие браузера")
    driver = webdriver.Chrome(service=ChromiumService(
        ChromeDriverManager().install()), options=chrome_options)
    mp = MainPage(driver)
    mp.go_to_site()

    yield mp

    driver.quit()
    print("Закрытие браузера")


def pytest_addoption(parser):
    """Command line arguments"""
    parser.addoption('--firefox', action='store', default=False, help='Параметр --firefox=True, что бы запустить тесты в браузере Firefox, по умалчанию False')
