class MainPage:
    URL = "https://github.com"

    def __init__(self, page):
        self.page = page
        # Иконка лупы в шапке сайта
        self.search_button = page.locator(
            "//button[contains(@class, 'search') or @aria-label='Search' "
            "or descendant::*[local-name()='svg' and contains(@aria-label, 'search')]]"
            "[not(contains(@class, 'btn-primary'))]"
        )
        self.search_input = page.locator(
            "//input[@type='text' and ("
            "@id='query-builder-test' "
            "or contains(@class, 'search-input') "
            "or @name='q'"
            ")]"
        )


    def open(self):
            self.page.goto(self.URL, wait_until="domcontentloaded", timeout=60000)

    def search(self, keyword: str):
        self.search_button.first.click()
        self.search_input.wait_for(state="visible", timeout=10000)
        self.search_input.fill(keyword)
        self.search_input.press("Enter")