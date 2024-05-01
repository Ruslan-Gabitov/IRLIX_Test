import os
import pytz
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchWindowException


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

    def switch_to_window(self, number_window: int) -> None:
        try:
            self.driver.switch_to.window(
                self.driver.window_handles[number_window])
        except NoSuchWindowException:
            pass

    def move_to_clickable_element(self, locators: str):
        element = self.find_element_clickable(locators)
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", element)
        return element

    def save_screenshot(self, path: str) -> None:
        if not os.path.exists("screen"):
            os.makedirs("screen")
        utc_tz = pytz.timezone('Europe/Moscow')
        utc_now = datetime.now(utc_tz)
        formatted_string = utc_now.strftime(r'%Y_%m_%d_%H_%M_%S')
        self.driver.save_screenshot(
            f"screen\{path}_{formatted_string}.png")

    def current_url(self) -> str:
        return self.driver.current_url

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def close(self):
        self.driver.close()

    def refresh(self):
        self.driver.refresh()
