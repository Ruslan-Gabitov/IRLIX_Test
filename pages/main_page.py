from base.BaseApp import Base
import allure


class locators:
    """Класс идентификаторов DOM элементов с использованием XPATH"""

    input_name_locator = ".//input[@id='name_input']"
    input_company_locator = ".//input[@id='company_input']"
    input_email_locator = ".//input[@id='email_input']"
    input_phone_locator = ".//input[@id='phone_input']"
    input_telegram_locator = ".//input[@id='telegram_input']"
    input_checkbox_qa_locator = ".//input[@value='QA']"
    policy_checkbox_locator = ".//label[@for='policy_checkbox']"
    policy_checkbox_assert_locator = ".//input[@id='policy_checkbox']"
    button_go_to_telegram_locator = ".//div[@class='i-process__card']/div/a"
    button_form_submission_locator = ".//button[@id='send_button']"
    button_go_back_site_locator = "(.//button[@class='modal__close'])[2]"
    button_swiper_next_locator = ".//div[@class='swiper-button-next']"
    link_become_customer_header_locator = ".//a[@class='i-header__action-button i-header__action-button--white']"
    modal_message_error_locator = ".//p[text()='The email must be a valid email address.']"
    img_logo_locator = ".//img[@class='i-feedbacks__header-logo-img']"


class MainPage(Base):
    """Класс описывающий главную страницу сайта"""

    def __init__(self, driver):
        super().__init__(driver)

    def click_initializing_value(self, locator):
        """Для инициализации значения в поле ввода"""
        with allure.step("[click_initializing_value] Инициализация значения в поле ввода (клик по соседнему полю ввода)"):
            self.find_element_clickable(locator=locator).click()

    """Actions"""

    def click_link_become_customer_header(self) -> None:
        """Функция ожидает WebElement в течении 10 сек и возвращает его
                    в случаи если он кликабелен и делает клик по этому элементу"""

        with allure.step("[click_link_become_customer_header] Клик по ссылке \"Стать клиентом\""):
            self.find_element_clickable(
                locator=locators.link_become_customer_header_locator).click()
            print("> Клик по ссылке \"Стать клиентом\"")

    def input_name(self, name: str) -> None:
        """Функция ожидает WebElement поля ИМЯ в течении 10 сек и возвращает его
                    в случаи если он кликабелен и добавляет в него значение"""

        with allure.step("[input_name] Добавление имени в поле ИМЯ"):
            self.find_element_clickable(
                locator=locators.input_name_locator).send_keys(name)
            print("> Добавлено имя в поле ИМЯ")

    def input_company(self, company_name: str) -> None:
        """Функция ожидает WebElement поля КОМПАНИЯ в течении 10 сек и возвращает его
                    в случаи если он кликабелен и добавляет в него значение"""

        with allure.step("[input_company] Добавление названия компании в поле КОМПАНИЯ"):
            self.find_element_clickable(
                locator=locators.input_company_locator).send_keys(company_name)
            print("> Добавлено название компании в поле КОМПАНИЯ")

    def input_email(self, email: str) -> None:
        """Функция ожидает WebElement поля ПОЧТА в течении 10 сек и возвращает его
                    в случаи если он кликабелен и добавляет в него значение"""

        with allure.step("[input_email] Добавление email в поле ПОЧТА"):
            self.find_element_clickable(
                locator=locators.input_email_locator).send_keys(email)
            print("> Добавлен email в поле ПОЧТА")

    def input_phone(self, phone) -> None:
        """Функция ожидает WebElement поля ТЕЛЕФОН в течении 10 сек и возвращает его
                    в случаи если он кликабелен и добавляет в него значение"""

        with allure.step("[input_phone] Добавление номера телефона в поле ТЕЛЕФОН"):
            self.find_element_clickable(
                locator=locators.input_phone_locator).send_keys(phone)
            print("> Добавлен телефон в поле ТЕЛЕФОН")

    def input_telegram(self, telegram_user) -> None:
        """Функция ожидает WebElement поля ТЕЛЕГРАМ в течении 10 сек и возвращает его
                    в случаи если он кликабелен и добавляет в него значение"""

        with allure.step("[input_telegram] Добавление имени пользователя Telegram в поле ТЕЛЕГРАМ"):
            self.find_element_clickable(
                locator=locators.input_telegram_locator).send_keys(telegram_user)
            print("> Добавлен телеграм в поле ТЕЛЕГРАМ")

    def click_checkbox_qa(self) -> None:
        """Функция ожидает WebElement (чек-бокс QA) в течении 10 сек и возвращает его
                    в случаи если он присутствует в DOM и делает клик по чек-боксу"""

        with allure.step("[click_checkbox_qa] Клик по чек-боксу \"QA\""):
            self.find_element(locator=locators.input_checkbox_qa_locator).click()
            print("> Клик по чек-боксу \"QA\"")

    def click_policy_checkbox(self) -> None:
        """Функция ожидает WebElement (чек-бокс "Согласие на обработку данных") в течении 10 сек и возвращает его
                    в случаи если он присутствует в DOM и делает клик по чек-боксу"""

        with allure.step("[click_policy_checkbox] Клик по чек-боксу \"Согласие на обработку данных\""):
            self.find_element(locator=locators.policy_checkbox_locator).click()
            print("> Клик по чек-боксу \"Согласие на обработку данных\"")

    def click_button_go_to_telegram(self):
        """Функция ожидает WebElement (кнопку "Написать") в течении 10 сек и делает scroll до
                    элемента в случаи если он кликабелен"""

        with allure.step("[click_button_go_to_telegram] Клик по кнопке \"Написать\""):
            self.move_to_clickable_element(
                locators=locators.button_go_to_telegram_locator).click()
            print("> Клик по кнопке \"Написать\"")

    def click_button_form_submission(self):
        """Функция ожидает WebElement (кнопку "Стать клиентом в низу формы) в течении 10 сек и если
            элемент кликабелен делает клик по нему"""

        with allure.step("[click_button_form_submission] Клик по ссылке \"Стать клиентом\" внизу формы"):
            self.find_element_clickable(
                locator=locators.button_form_submission_locator).click()
            print("> Клик по ссылке \"Стать клиентом\" внизу формы")


if __name__ == "__main__":
    pass
