class RepoPage:
    def __init__(self, page):
        self.page = page
        # README секция — через ancestor поднимаемся к div#readme
        self.readme = self.page.locator(
            "//*["
            "contains(@class, 'markdown-body') "
            "and ancestor::*[@id='readme' "
            "or contains(@class, 'repository-content')]"
            "]"
        )

    def readme_contains(self, text: str) -> bool:
        self.readme.first.wait_for(state="visible", timeout=15000)
        content = self.readme.first.inner_text()
        return text in content