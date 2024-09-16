from playwright.sync_api import sync_playwright
from POM.main_page import MainPage
from POM.search_restults import SearchResultsPage


def before_all(context):
    # Uruchamiamy Playwright
    context.playwright = sync_playwright().start()


def before_scenario(context, scenario):
    # Konfiguracja dla każdej nowej sesji przeglądarki
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page(viewport={'width': 1200, 'height': 1080})

    # Dodajemy instancję MainPage do context
    context.main_page = MainPage(context.page)
    context.search_results_page = SearchResultsPage(context.page)


def after_scenario(context, scenario):
    # Zamykamy stronę i przeglądarkę po każdym scenariuszu
    context.page.close()
    context.browser.close()


def after_all(context):
    # Zamykamy Playwright na koniec
    context.playwright.stop()
