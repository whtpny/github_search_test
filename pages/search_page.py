class SearchPage:
    def __init__(self, page):
        self.page = page

    def click_repo_by_name(self, repo_name: str):
        # Ищем ссылку через ancestor — поднимаемся к контейнеру результата
        # и проверяем наличие текста в дочерних элементах
        repo_link = self.page.locator(
            f"//a["
            f"contains(@href, '/CopilotKit') "
            f"and ancestor::*["
            f"contains(@class, 'search') "
            f"or contains(@data-testid, 'result')"
            f"] "
            f"and .//*[contains(normalize-space(.), '{repo_name}')] "
            f"or .//*[contains(normalize-space(text()), '{repo_name}')] "
            f"and not(contains(@href, 'issues')) "
            f"and not(contains(@href, 'pulls'))"
            f"]"
        ).first
        repo_link.wait_for(state="visible", timeout=15000)
        repo_link.click()