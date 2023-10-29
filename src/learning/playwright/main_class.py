import time

from playwright.sync_api import sync_playwright


class OzonSellerParse:
    def __init__(self, keyword: str):
        self.keyword = keyword
        self.list_seller_name = []

    def parse(self):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            self.context = browser.new_context()
            self.page = self.context.new_page()
            self.page.goto("https://ozon.ru/")
            self.page.get_by_placeholder("Искать на Ozon").type(text=self.keyword, delay=0.3)
            self.page.query_selector("button[type='submit']").click()
            self.page.loca


if __name__ == "__main__":
    OzonSellerParse("вентилятор").parse()


