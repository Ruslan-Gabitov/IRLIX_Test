from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
import pytz


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://irlix.com/"

    def find_element_clickable(self, locators: str, time: int = 10) -> WebElement:
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable((By.XPATH, locators)),
                                                      message=f"Can't find element by locator {locators}")

    def find_element(self, locators: str, time: int = 10) -> WebElement:
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.XPATH, locators)),
                                                      message=f"Can't find element by locator {locators}")

    def find_elements(self, locators: str, time: int = 10) -> list[WebElement]:
        return WebDriverWait(self.driver, time).until(EC.presence_of_elements_located((By.XPATH, locators)),
                                                      message=f"Can't find element by locator {locators}")

    def save_screenshot(self, path: str) -> None:
        utc_tz = pytz.timezone('Europe/Moscow')
        utc_now = datetime.now(utc_tz)
        formatted_string = utc_now.strftime(r'%Y_%m_%d_%H_%M_%S')
        self.driver.save_screenshot(
            f"{path}_{formatted_string}.png")

    def current_url(self) -> str:
        return self.driver.current_url

    def go_to_site(self):
        return self.driver.get(self.base_url)
