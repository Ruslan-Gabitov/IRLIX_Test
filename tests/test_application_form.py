from typing import Type
from utilities.logger import Logger
from pages.main_page import MainPage, locators
import allure


@allure.description("TestApplicationForm (Функциональное тестирование формы заявки на возможность ввода текста в поля)")
class TestApplicationForm:

    """Класс для функционального тестирования формы заявки на основной странице сайта"""

    name = "TestName"
    name_company = "TestNameCompany"
    email = "test@company.com"
    phone = "+7(999)-999-99-99"
    telegram_user = "@test_user"

    def test_click_link_become_customer_header(self, browser: Type[MainPage]) -> None:

        """Функция тестирования Кнопки "Стать клиентом" """

        # Шаг сбора отчета Allure
        with allure.step("[test_click_link_become_customer_header] Клик по кнопке 'Стать клиентом'"):

            # Начало сбора логов данной функции
            Logger.add_start_step(
                method="test_click_link_become_customer_header")

            # Клик по кнопке "Стать клиентом"
            browser.click_link_become_customer_header()

            # Проверка что после нажатия нас портировало к якорю #contact
            assert browser.current_url() == "https://irlix.com/#contact"

            # Конец записи логирования данной функции
            Logger.add_end_step(
                method="test_click_link_become_customer_header", url=browser.current_url())

    def test_input_name(self, browser: Type[MainPage]) -> None:

        """Функция тестирования поля ввода имени"""

        # Шаг сбора отчета Allure
        with allure.step("[test_input_name] Тестирование поля ввода ИМЯ"):

            # Начало сбора логов данной функции
            Logger.add_start_step(method="test_input_name")

            # Добавление значения в поле ИМЯ
            browser.input_name(name=self.name)

            # Инициализация значения в поле кликом по соседнему полю
            browser.click_initializing_value(locators=locators.input_company)

            # Проверка, что в данный момент в поле действительно находится какоето значение
            assert browser.find_element_clickable(locators=locators.input_name).get_attribute(
                "data-gtm-form-interact-field-id") == "0"

            # Конец записи логирования данной функции
            Logger.add_end_step(method="test_input_name",
                                url=browser.current_url())

    def test_input_company(self, browser: Type[MainPage]) -> None:

        """Функция тестирования поля ввода имени компании"""

        # Шаг сбора отчета Allure
        with allure.step("[test_input_company] Тестирование поля ввода КОМПАНИЯ"):

            # Начало сбора логов данной функции
            Logger.add_start_step(method="test_input_company")

            # Добавление значения в поле КОМПАНИЯ
            browser.input_company(company_name=self.name_company)

            # Инициализация значения в поле кликом по соседнему полю
            browser.click_initializing_value(locators=locators.input_name)

            # Проверка, что в данный момент в поле действительно находится какое-то значение
            assert browser.find_element_clickable(locators=locators.input_company).get_attribute(
                "data-gtm-form-interact-field-id") == "1"

            # Конец записи логирования данной функции
            Logger.add_end_step(method="test_input_company",
                                url=browser.current_url())

    def test_input_email(self, browser: Type[MainPage]) -> None:

        """Функция тестирования поля ввода почты """

        # Шаг сбора отчета Allure
        with allure.step("[test_input_email] Тестирование поля ввода ПОЧТА"):

            # Начало сбора логов данной функции
            Logger.add_start_step(method="test_input_email")

            # Добавление значения в поле ПОЧТА
            browser.input_email(email=self.email)

            # Инициализация значения в поле кликом по соседнему полю
            browser.click_initializing_value(locators=locators.input_name)

            # Проверка, что в данный момент в поле действительно находится какое-то значение
            assert browser.find_element_clickable(locators=locators.input_email).get_attribute(
                "data-gtm-form-interact-field-id") == "2"

            # Конец записи логирования данной функции
            Logger.add_end_step(method="test_input_email",
                                url=browser.current_url())

    def test_input_phone(self, browser: Type[MainPage]) -> None:

        """Функция тестирования поля ввода номера телефона"""

        # Шаг сбора отчета Allure
        with allure.step("[test_input_phone] Тестирование поля ввода ТЕЛЕФОН"):

            # Начало сбора логов данной функции
            Logger.add_start_step(method="test_input_phone")

            # Добавление значения в поле ТЕЛЕФОН
            browser.input_phone(phone=self.phone)

            # Инициализация значения в поле кликом по соседнему полю
            browser.click_initializing_value(locators=locators.input_name)

            # Проверка, что в данный момент в поле действительно находится какое-то значение
            assert browser.find_element_clickable(locators=locators.input_phone).get_attribute(
                "data-gtm-form-interact-field-id") == "3"

            # Конец записи логирования данной функции
            Logger.add_end_step(method="test_input_phone",
                                url=browser.current_url())

    def test_input_telegram(self, browser: Type[MainPage]) -> None:

        """Функция тестирования поля ввода имени пользователя телеграм"""

        # Шаг сбора отчета Allure
        with allure.step("[test_input_telegram] Тестирование поля ввода ТЕЛЕГРАМ"):

            # Начало сбора логов данной функции
            Logger.add_start_step(method="test_input_telegram")

            # Добавление значения в поле ТЕЛЕГРАМ
            browser.input_telegram(telegram_user=self.telegram_user)

            # Инициализация значения в поле кликом по соседнему полю
            browser.click_initializing_value(locators=locators.input_name)

            # Проверка, что в данный момент в поле действительно находится какое-то значение
            assert browser.find_element_clickable(locators=locators.input_telegram).get_attribute(
                "data-gtm-form-interact-field-id") == "4"

            # Конец записи логирования данной функции
            Logger.add_end_step(method="test_input_telegram",
                                url=browser.current_url())

    def test_click_checkbox_qa(self, browser: Type[MainPage]) -> None:

        """Функция тестирования клика по чек-боксу QA"""

        # Шаг сбора отчета Allure
        with allure.step("[test_click_checkbox_qa] Инициализация чек-бокса QA"):

            # Начало сбора логов данной функции
            Logger.add_start_step(method="test_click_checkbox_qa")

            # Клик по чек_боксу "QA"
            browser.click_checkbox_qa()

            # Проверка, что в данный момент чек-бокс активирован
            assert browser.find_element(locators=locators.input_checkbox_qa).get_attribute(
                "data-gtm-form-interact-field-id") == "5"

            # Конец записи логирования данной функции
            Logger.add_end_step(
                method="test_click_checkbox_qa", url=browser.current_url())

    def test_click_policy_checkbox(self, browser: Type[MainPage]) -> None:

        """Функция тестирования клика по чек-боксу "Согласие на обработку персональных данных" """

        # Шаг сбора отчета Allure
        with allure.step("[test_click_policy_checkbox] Инициализация чек-бокса 'Согласие на обработку персональных данных'"):

            # Начало сбора логов данной функции
            Logger.add_start_step(method="test_click_policy_checkbox")

            # Клик по чек_боксу "Согласие на обработку персональных данных"
            browser.click_policy_checkbox()

            # Проверка, что в данный момент чек-бокс активирован
            assert browser.find_element(locators=locators.policy_checkbox_assert).get_attribute(
                "data-gtm-form-interact-field-id") == "6"

            # Конец записи логирования данной функции
            Logger.add_end_step(
                method="test_click_policy_checkbox", url=browser.current_url())

            # Создание и сохранение скриншота
            browser.save_screenshot(
                path=r"TestApplicationForm")
