from typing import Type
from utilities.logger import Logger
from pages.main_page import MainPage, locators
import allure


@allure.description("TestApplicationForm (Функциональное тестирование формы заявки на возможность ввода текста в поля)")
class TestApplicationForm:

    name = "TestName"
    name_company = "TestNameCompany"
    email = "test@company.com"
    phone = "+7(999)-999-99-99"
    telegram_user = "@test_user"

    def test_click_link_become_customer_header(self, browser: Type[MainPage]) -> None:
        with allure.step("[test_click_link_become_customer_header] Клик по кнопке 'Стать клиентом'"):
            Logger.add_start_step(method="test_click_link_become_customer_header")
            browser.click_link_become_customer_header()
            assert browser.current_url() == "https://irlix.com/#contact"
            Logger.add_end_step(method="test_click_link_become_customer_header", url=browser.current_url())

    def test_input_name(self, browser: Type[MainPage]) -> None:
        with allure.step("[test_input_name] Тестирование поля ввода ИМЯ"):
            Logger.add_start_step(method="test_input_name")
            browser.input_name(name=self.name)
            browser.click_initializing_value(locators=locators.input_company)
            assert browser.find_element_clickable(locators=locators.input_name).get_attribute(
                "data-gtm-form-interact-field-id") == "0"
            Logger.add_end_step(method="test_input_name", url=browser.current_url())

    def test_input_company(self, browser: Type[MainPage]) -> None:
        with allure.step("[test_input_company] Тестирование поля ввода КОМПАНИЯ"):
            Logger.add_start_step(method="test_input_company")
            browser.input_company(company_name=self.name_company)
            browser.click_initializing_value(locators=locators.input_name)
            assert browser.find_element_clickable(locators=locators.input_company).get_attribute(
                "data-gtm-form-interact-field-id") == "1"
            Logger.add_end_step(method="test_input_company", url=browser.current_url())

    def test_input_email(self, browser: Type[MainPage]) -> None:
        with allure.step("[test_input_email] Тестирование поля ввода ПОЧТА"):
            Logger.add_start_step(method="test_input_email")
            browser.input_email(email=self.email)
            browser.click_initializing_value(locators=locators.input_name)
            assert browser.find_element_clickable(locators=locators.input_email).get_attribute(
                "data-gtm-form-interact-field-id") == "2"
            Logger.add_end_step(method="test_input_email", url=browser.current_url())

    def test_input_phone(self, browser: Type[MainPage]) -> None:
        with allure.step("[test_input_phone] Тестирование поля ввода ТЕЛЕФОН"):
            Logger.add_start_step(method="test_input_phone")
            browser.input_phone(phone=self.phone)
            browser.click_initializing_value(locators=locators.input_name)
            assert browser.find_element_clickable(locators=locators.input_phone).get_attribute(
                "data-gtm-form-interact-field-id") == "3"
            Logger.add_end_step(method="test_input_phone", url=browser.current_url())

    def test_input_telegram(self, browser: Type[MainPage]) -> None:
        with allure.step("[test_input_telegram] Тестирование поля ввода ТЕЛЕГРАМ"):
            Logger.add_start_step(method="test_input_telegram")
            browser.input_telegram(telegram_user=self.telegram_user)
            browser.click_initializing_value(locators=locators.input_name)
            assert browser.find_element_clickable(locators=locators.input_telegram).get_attribute(
                "data-gtm-form-interact-field-id") == "4"
            Logger.add_end_step(method="test_input_telegram", url=browser.current_url())

    def test_click_checkbox_qa(self, browser: Type[MainPage]) -> None:
        with allure.step("[test_click_checkbox_qa] Инициализация чек-бокса QA"):
            Logger.add_start_step(method="test_click_checkbox_qa")
            browser.click_checkbox_qa()
            assert browser.find_element(locators=locators.input_checkbox_qa).get_attribute(
                "data-gtm-form-interact-field-id") == "5"
            Logger.add_end_step(method="test_click_checkbox_qa", url=browser.current_url())

    def test_click_policy_checkbox(self, browser: Type[MainPage]) -> None:
        with allure.step("[test_click_policy_checkbox] Инициализация чек-бокса 'Cогласие на обработку персональных данных'"):
            Logger.add_start_step(method="test_click_policy_checkbox")
            browser.click_policy_checkbox()
            assert browser.find_element(locators=locators.policy_checkbox_assert).get_attribute(
                "data-gtm-form-interact-field-id") == "6"
            Logger.add_end_step(method="test_click_policy_checkbox", url=browser.current_url())
            browser.save_screenshot(
                path=r"forms")
