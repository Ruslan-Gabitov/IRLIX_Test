import os
import pytz
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchWindowException


class Base:
    """Базовый класс методов selenium от которого наследуется классы Page"""
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://irlix.com/"

    def find_element_clickable(self, locators: str, time: int = 10) -> WebElement:
        """Функция ожидает WebElement в течении 10 сек и возвращает его 
                    в случаи если он кликабелен"""

        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable((By.XPATH, locators)),
                                                      message=f"Can't find element by locator {locators}")

    def find_element(self, locators: str, time: int = 10) -> WebElement:
        """Функция ожидает WebElement в течении 10 сек и возвращает его 
                    в случаи если он присутствует в DOM"""
        
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.XPATH, locators)),
                                                      message=f"Can't find element by locator {locators}")

    def find_elements(self, locators: str, time: int = 10) -> list[WebElement]:
        """Функция ожидает WebElement в течении 10 сек и возвращает список элементов
                    в случаи если он присутствует в DOM"""
        
        return WebDriverWait(self.driver, time).until(EC.presence_of_elements_located((By.XPATH, locators)),
                                                      message=f"Can't find element by locator {locators}")

    def switch_to_window(self, number_window: int) -> None:
        """Функция для перехода на новую вкладку (работает корректно с Chrome),
                 конструкция try/except необходима потому что в браузере Firefox при открытии новой вкладки,
                она автоматически становится активной и на нее нет необходимости переключаться"""
        
        try:
            self.driver.switch_to.window(
                self.driver.window_handles[number_window])
        except NoSuchWindowException:
            pass

    def move_to_clickable_element(self, locators: str):
        """Функция проверяет присутствие кликабельного элемента на странице
            и делает scroll до него. Использование execute_script необходимо
            для корректной работы в двух браузерах Firefox и Chrome"""
        
        element = self.find_element_clickable(locators)
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", element)
        return element

    def save_screenshot(self, path: str) -> None:
        """Функция сначала проверяет существует ли директория, 
        если нет то создает ее и сохраняет скриншот в нее, с указанием даты и времени. """

        if not os.path.exists("screen"):
            os.makedirs("screen")
        utc_tz = pytz.timezone('Europe/Moscow')
        utc_now = datetime.now(utc_tz)
        formatted_string = utc_now.strftime(r'%Y_%m_%d_%H_%M_%S')
        self.driver.save_screenshot(
            f"screen\{path}_{formatted_string}.png")

    def current_url(self) -> str:
        """Функция получает URL текущей, активной страницы"""

        return self.driver.current_url

    def go_to_site(self):
        """Функция открытия вкладки с базовым URL"""

        return self.driver.get(self.base_url)

    def close(self):
        """Функция закрытия текущей активной вкладки"""

        self.driver.close()

    def refresh(self):
        """Функция перезагрузки текущей активной вкладки"""

        self.driver.refresh()
