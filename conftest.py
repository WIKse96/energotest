import pytest
from playwright.sync_api import Page

from POM.main_page import MainPage
from POM.search_restults import SearchResultsPage


# Fixture dla podstawowych ustawień playwright
@pytest.fixture()
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        'viewport': {
            'width': 1200,
            'height': 1080,
        },

    }

# Zwracamy kontekst. Każdy test powinien być w nowym "czystym" kontekście.
@pytest.fixture()
def main_page(page: Page) -> MainPage:
    return MainPage(page)

@pytest.fixture()
def search_results_page(page: Page) -> SearchResultsPage:
    return SearchResultsPage(page)