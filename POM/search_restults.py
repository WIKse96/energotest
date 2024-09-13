import time

from playwright.sync_api import Page, expect
from locators.results_locators import ResultsLocators

class SearchResultsPage:
    def __init__(self, page: Page):
        self.page = page
        self.links_locator = page.locator(ResultsLocators.LINK)
        self.next_btn = page.locator(ResultsLocators.NEXT_PAGE)

    def verify_results(self):
        time.sleep(2)
        self.page.wait_for_selector(ResultsLocators.LINK)

        while True:
            # Stworzenie listy wraz z filtrami
            hrefs = [link.get_attribute('href') for link in self.links_locator.all() if
                     link.get_attribute('href') is not None]
            # Sprawdzam czy jakiś element w liście zawiera szukany tekst
            if any("spie-energotest.pl" in href for href in hrefs):
                assert True
            else:
                self.next_btn.click()
            if self.page.locator("//a[aria-label]"):
                pass