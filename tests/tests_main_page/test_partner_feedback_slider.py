from typing import Type
from utilities.logger import Logger
from pages.main_page import MainPage, locators
import allure


@allure.description("TestPartnerFeedbackSlider (Функциональное тестирование слайдера отзывов партнеров")
class TestPartnerFeedbackSlider:
    """Класс функционального тестирования слайдера отзывов партнеров"""

    def test_partner_feedback_slider_click(self, page_main: Type[MainPage]) -> None:
        with allure.step("[test_partner_feedback_slider] Тест прокрутки слайдера отзывов партнеров кликом по кнопке next"):

            # Начало сбора логов данной функции
            Logger.add_start_step(
                method="test_click_link_become_customer_header")

            # Портируемся к кликабельному элементу
            page_main.move_to_clickable_element(locator=locators.img_logo_locator)

            # Получаем названия брендов из атрибута alt
            value_img_alts = [img_tag.get_attribute("alt")
                              for img_tag in page_main.find_elements(locator=locators.img_logo_locator)]

            # Используем длину списка value_img_alts
            for index in range(0, len(value_img_alts)):

                # Формируем локатор для проверки видимости элемента на странице
                locator = f".//img[@alt='{value_img_alts[index]}']"

                # Проверка видимости элемента на странице
                assert page_main.is_displayed(locator) is True

                # Проверяем что текущий элемент не равен последнему элементу в списке,
                # что бы избежать исключения TimeoutException которое возникает
                # так как кнопка  button_swiper_next становится не кликабельной
                if value_img_alts[index] != value_img_alts[-1]:

                    # Кликаем по кнопке button_swiper_next для свайпа в право слайдера комментариев
                    page_main.find_element_clickable(
                        locators.button_swiper_next_locator).click()

            # Конец записи логирования данной функции
            Logger.add_end_step(
                method="test_click_link_become_customer_header", url=page_main.current_url())
