from typing import Type
from utilities.logger import Logger
from pages.main_page import MainPage, locators


class TestApplicationForm:

    name = "TestName"
    name_company = "TestNameCompany"
    email = "test@company.com"
    phone = "+7(999)-999-99-99"
    telegram_user = "@test_user"

    def test_click_link_become_customer_header(self, browser: Type[MainPage]) -> None:
        browser.click_link_become_customer_header()
        assert browser.current_url() == "https://irlix.com/#contact"

    def test_input_name(self, browser: Type[MainPage]) -> None:
        browser.input_name(name=self.name)
        browser.click_initializing_value(locators=locators.input_company)
        assert browser.find_element_clickable(locators=locators.input_name).get_attribute(
            "data-gtm-form-interact-field-id") == "0"

    def test_input_company(self, browser: Type[MainPage]) -> None:
        browser.input_company(company_name=self.name_company)
        browser.click_initializing_value(locators=locators.input_name)
        assert browser.find_element_clickable(locators=locators.input_company).get_attribute(
            "data-gtm-form-interact-field-id") == "1"

    def test_input_email(self, browser: Type[MainPage]) -> None:
        browser.input_email(email=self.email)
        browser.click_initializing_value(locators=locators.input_name)
        assert browser.find_element_clickable(locators=locators.input_email).get_attribute(
            "data-gtm-form-interact-field-id") == "2"

    def test_input_phone(self, browser: Type[MainPage]) -> None:
        browser.input_phone(phone=self.phone)
        browser.click_initializing_value(locators=locators.input_name)
        assert browser.find_element_clickable(locators=locators.input_phone).get_attribute(
            "data-gtm-form-interact-field-id") == "3"

    def test_input_telegram(self, browser: Type[MainPage]) -> None:
        browser.input_telegram(telegram_user=self.telegram_user)
        browser.click_initializing_value(locators=locators.input_name)
        assert browser.find_element_clickable(locators=locators.input_telegram).get_attribute(
            "data-gtm-form-interact-field-id") == "4"

    def test_click_checkbox_qa(self, browser: Type[MainPage]) -> None:
        browser.click_checkbox_qa()
        assert browser.find_element(locators=locators.input_checkbox_qa).get_attribute(
            "data-gtm-form-interact-field-id") == "5"

    def test_click_policy_checkbox(self, browser: Type[MainPage]) -> None:
        browser.click_policy_checkbox()
        assert browser.find_element(locators=locators.policy_checkbox_assert).get_attribute(
            "data-gtm-form-interact-field-id") == "6"
        browser.save_screenshot(
            path=r"forms")
