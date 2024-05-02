import datetime
import os


class Logger():

    """Класс записи логирования тестов в файл"""

    # Проверка существования директории для записи логов
    if not os.path.exists("logs"):
        os.makedirs("logs")

    # Создание имени файла с текущим временем и датой
    file_name = fr"logs\log_{
        str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))}.log"

    # Создание файла с расширением .log и последующая до запись в него логов
    @classmethod
    def write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf=8') as logger_file:
            logger_file.write(data)

    # Получение логов при старте тестовой функции
    @classmethod
    def add_start_step(cls, method: str):

        # Получение наименования текущего теста из переменной окружения
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f"\n{'=' * 50}\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Start time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Start name method: {method}\n"

        cls.write_log_to_file(data_to_add)

    # Получение логов при завершении работы тестовой функции
    @classmethod
    def add_end_step(cls, url: str, method: str):

        data_to_add = f"End time: {str(datetime.datetime.now())}\n"
        data_to_add += f"End name method: {method}\n"
        data_to_add += f"URL: {url}"
        data_to_add += f"\n{'=' * 50}\n"

        cls.write_log_to_file(data_to_add)
