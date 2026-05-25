# GitHub Search Test

Автотест для проверки глобального поиска GitHub.
Находит репозиторий CopilotKit и проверяет наличие текста в README.md.

## Стек
- Python 3.12+
- Playwright 1.55.0
- PyTest 8.4.1

## Установка

1. Клонировать репозиторий:
   git clone https://github.com/ТВОЙ_НИК/github_search_test.git
   cd github_search_test

2. Создать виртуальное окружение:
   python -m venv venv
   venv\Scripts\activate

3. Установить зависимости:
   pip install -r requirements.txt
   playwright install chrome

## Запуск тестов

Из терминала:
   pytest tests/ -v

Из PyCharm:
   Правой кнопкой на файл test_github_search.py → Run

## Тест-кейс

Ссылка на тест-кейс в Google Docs: 