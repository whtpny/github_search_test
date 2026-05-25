class RepoPage:
    def __init__(self, page):
        self.page = page
        self.readme = self.page.locator(
            "//div[@id='readme']//article"
            " | //div[@id='readme']//*[contains(@class, 'markdown-body')]"
            " | //*[contains(@class, 'markdown-body')]"
        )

    def readme_contains(self, text: str) -> bool:
        self.readme.first.wait_for(state="visible", timeout=15000)
        content = self.readme.first.inner_text()
        return text in content