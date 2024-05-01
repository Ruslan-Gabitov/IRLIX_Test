from base.BaseApp import Base


class locators:
    link_become_customer_header = ".//a[@class='i-header__action-button i-header__action-button--white']"
    button_form_submission = ".//button[@id='send_button']"
    input_name = ".//input[@id='name_input']"
    input_company = ".//input[@id='company_input']"
    input_email = ".//input[@id='email_input']"
    input_phone = ".//input[@id='phone_input']"
    input_telegram = ".//input[@id='telegram_input']"
    input_checkbox_qa = ".//input[@value='QA']"
    policy_checkbox = ".//label[@for='policy_checkbox']"
    policy_checkbox_assert = ".//input[@id='policy_checkbox']"
    button_go_to_telegram = ".//div[@class='i-process__card']/div/a"


class MainPage(Base):
    def __inint__(self, driver):
        super().__init__(driver)

    def click_initializing_value(self, locators):
        """Для инициализации значения в поле ввода"""
        self.find_element_clickable(locators=locators).click()

    """Actions"""

    def click_link_become_customer_header(self) -> None:
        self.find_element_clickable(
            locators=locators.link_become_customer_header).click()
        print("> Клик по ссылке \"Стать клиентом\"")

    def input_name(self, name: str) -> None:
        self.find_element_clickable(
            locators=locators.input_name).send_keys(name)
        print("> Добавленно имя в поле ИМЯ")

    def input_company(self, company_name: str) -> None:
        self.find_element_clickable(
            locators=locators.input_company).send_keys(company_name)
        print("> Добавленно название компании в поле КОМПАНИЯ")

    def input_email(self, email: str) -> None:
        self.find_element_clickable(
            locators=locators.input_email).send_keys(email)
        print("> Добавлен email в поле ПОЧТА")

    def input_phone(self, phone) -> None:
        self.find_element_clickable(
            locators=locators.input_phone).send_keys(phone)
        print("> Добавлен телефон в поле ТЕЛЕФОН")

    def input_telegram(self, telegram_user) -> None:
        self.find_element_clickable(
            locators=locators.input_telegram).send_keys(telegram_user)
        print("> Добавлен телеграм в поле ТЕЛЕГРАМ")

    def click_checkbox_qa(self) -> None:
        self.find_element(locators=locators.input_checkbox_qa).click()
        print("> Клик по чек-боксу \"QA\"")

    def click_policy_checkbox(self) -> None:
        self.find_element(locators=locators.policy_checkbox).click()
        print("> Клик по чек-боксу \"Согласие на обработку данных\"")

    def click_button_go_to_telegram(self):
        self.move_to_clickable_element(locators=locators.button_go_to_telegram).click()
        print("> Клик по кнопке \"Написать\"")


if __name__ == "__main__":
    pass
