# Установка зависимостей:

**Установка Allure через Scoop (для Windows):**

Убедитесь, что [Scoop](https://scoop.sh/) установлен

Убедитесь, что установлен Java версии 8 или выше, и его директория указана в переменной среды JAVA_HOME.

В терминале PowerShell выполните следующую команду: `scoop install allure`

**Установка Python библиотек:**

В проекте установите виртуальное окружение: `py -m venv venv`

Активируйте виртуальное окружение: `./venv/Scripts/activate`

Установите необходимые библиотеки: `pip install -r .\requirements.txt`

# Запуск тестов:

**Запуск с отчетом Allure:**

В браузере Chrome: `python -m pytest -s -v --alluredir allure-results`

В браузере Firefox: `python -m pytest -s -v --firefox --alluredir allure-results`

Затем: `allure serve allure-results`

**Запуск простых тестов:**

Выполните команду: `pytest -s -v` она запустит тесты в браузере Chrome

Или выполните команду: `pytest -s -v --firefox` она запустит тесты в браузере Firefox
