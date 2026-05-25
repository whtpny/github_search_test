class SearchPage:
    def __init__(self, page):
        self.page = page

    def click_repo_by_name(self, repo_name: str):
        repo_link = self.page.locator(
            f"//a[contains(@href, '/CopilotKit') "
            f"and .//*[contains(normalize-space(text()), '{repo_name}')] "
            f"or contains(normalize-space(text()), '{repo_name}')]"
            f"[ancestor::*[contains(@class, 'search-title') "
            f"or contains(@class, 'Title')]]"
        ).first
        repo_link.wait_for(state="visible")
        repo_link.click()