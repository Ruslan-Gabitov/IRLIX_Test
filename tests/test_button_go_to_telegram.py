from typing import Type
from utilities.logger import Logger
from pages.main_page import MainPage, locators
import allure


@allure.description("TestApplicationForm (Функциональное тестирование кнопки \"Написать\")")
class TestButtonGoToTelegram:
    """Класс функционального тестирования кнопки написать, что она кликабельна и ведет на сайт Telegram"""

    def test_click_button_go_to_telegram(self, page_main: Type[MainPage]):
        """Функция тестирования кнопки "Написать" """

        # Шаг сбора отчета Allure
        with allure.step("[test_click_button_go_to_telegram] Тест кнопки \"Написать\" и переход в Телеграм"):

            # Начало сбора логов данной функции
            Logger.add_start_step(
                method="test_click_link_become_customer_header")

            # Ожидание кликабельного WebElement-а и scroll до него и клик
            page_main.move_to_clickable_element(
                locators=locators.button_go_to_telegram).click()

            # Переход на вновь открывшеюся вкладку (в случаи с Chrome). В случаи FairFox
            # происходит перехват исключения NoSuchWindowException
            page_main.switch_to_window(1)

            # Создание и сохранение скриншота
            page_main.save_screenshot(path=r"TestButtonGoToTelegram")

            # Проверка, что перешли на новую вкладку и там есть текст @irlix_it
            assert page_main.find_element(
                ".//div[@class='tgme_page_extra']").text.strip() == "@irlix_it"

            # Закрытие текущей вкладки браузера
            page_main.close()

            # Возврат на начальную вкладку браузера
            page_main.switch_to_window(0)

            # Перезагрузка начально вкладки браузера для последующих тестов
            page_main.refresh()

            # Конец записи логирования данной функции
            Logger.add_end_step(
                method="test_click_link_become_customer_header", url=page_main.current_url())
