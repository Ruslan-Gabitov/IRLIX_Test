from base.BaseApp import Base


class locators:
    """Класс идентификаторов DOM элементов с использованием XPATH"""
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
    """Класс описывающий главную страницу сайта"""
    def __init__(self, driver):
        super().__init__(driver)

    def click_initializing_value(self, locators):
        """Для инициализации значения в поле ввода"""
        self.find_element_clickable(locators=locators).click()

    """Actions"""

    def click_link_become_customer_header(self) -> None:
        """Функция ожидает WebElement в течении 10 сек и возвращает его 
                    в случаи если он кликабелен и делает клик по этому элементу"""
        self.find_element_clickable(
            locators=locators.link_become_customer_header).click()
        print("> Клик по ссылке \"Стать клиентом\"")

    def input_name(self, name: str) -> None:
        """Функция ожидает WebElement поля ИМЯ в течении 10 сек и возвращает его 
                    в случаи если он кликабелен и добавляет в него значение"""
        self.find_element_clickable(
            locators=locators.input_name).send_keys(name)
        print("> Добавлено имя в поле ИМЯ")

    def input_company(self, company_name: str) -> None:
        """Функция ожидает WebElement поля КОМПАНИЯ в течении 10 сек и возвращает его 
                    в случаи если он кликабелен и добавляет в него значение"""
        self.find_element_clickable(
            locators=locators.input_company).send_keys(company_name)
        print("> Добавлено название компании в поле КОМПАНИЯ")

    def input_email(self, email: str) -> None:
        """Функция ожидает WebElement поля ПОЧТА в течении 10 сек и возвращает его 
                    в случаи если он кликабелен и добавляет в него значение"""
        self.find_element_clickable(
            locators=locators.input_email).send_keys(email)
        print("> Добавлен email в поле ПОЧТА")

    def input_phone(self, phone) -> None:
        """Функция ожидает WebElement поля ТЕЛЕФОН в течении 10 сек и возвращает его 
                    в случаи если он кликабелен и добавляет в него значение"""
        self.find_element_clickable(
            locators=locators.input_phone).send_keys(phone)
        print("> Добавлен телефон в поле ТЕЛЕФОН")

    def input_telegram(self, telegram_user) -> None:
        """Функция ожидает WebElement поля ТЕЛЕГРАМ в течении 10 сек и возвращает его 
                    в случаи если он кликабелен и добавляет в него значение"""
        self.find_element_clickable(
            locators=locators.input_telegram).send_keys(telegram_user)
        print("> Добавлен телеграм в поле ТЕЛЕГРАМ")

    def click_checkbox_qa(self) -> None:
        """Функция ожидает WebElement (чек-бокс QA) в течении 10 сек и возвращает его 
                    в случаи если он присутствует в DOM и делает клик по чек-боксу"""
        self.find_element(locators=locators.input_checkbox_qa).click()
        print("> Клик по чек-боксу \"QA\"")

    def click_policy_checkbox(self) -> None:
        """Функция ожидает WebElement (чек-бокс "Согласие на обработку данных") в течении 10 сек и возвращает его 
                    в случаи если он присутствует в DOM и делает клик по чек-боксу"""
        self.find_element(locators=locators.policy_checkbox).click()
        print("> Клик по чек-боксу \"Согласие на обработку данных\"")

    def click_button_go_to_telegram(self):
        """Функция ожидает WebElement (кнопку "Написать") в течении 10 сек и делает scroll до 
                    элемента в случаи если он кликабелен"""
        self.move_to_clickable_element(locators=locators.button_go_to_telegram).click()
        print("> Клик по кнопке \"Написать\"")


if __name__ == "__main__":
    pass
