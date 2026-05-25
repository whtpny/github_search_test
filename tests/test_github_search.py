from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.repo_page import RepoPage


def test_search_copilotkit(page):
    """
    Сценарий: глобальный поиск GitHub находит репозиторий CopilotKit,
    пользователь переходит на его страницу и видит CopilotKit в README.
    """
    main_page = MainPage(page)
    search_page = SearchPage(page)
    repo_page = RepoPage(page)

    main_page.open()
    main_page.search("copilot")
    search_page.click_repo_by_name("CopilotKit")

    assert repo_page.readme_contains("CopilotKit"), \
        "Текст 'CopilotKit' не найден в README.md репозитория"