class MainPage:
    URL = "https://github.com"

    def __init__(self, page):
        self.page = page
        self.search_button = page.locator(
            "//button[contains(@class, 'search') "
            "and ancestor::header]"
        )
        self.search_input = page.locator(
            "//input[@id='query-builder-test']"
        )

    def open(self):
        self.page.goto(self.URL, wait_until="domcontentloaded", timeout=60000)

    def search(self, keyword: str):
        self.search_button.first.click()
        # Ждём пока поле станет видимым после клика
        self.page.wait_for_selector(
            "//input[@id='query-builder-test']",
            state="visible",
            timeout=10000
        )
        self.search_input.fill(keyword)
        self.search_input.press("Enter")