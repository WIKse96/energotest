from playwright.sync_api import Page


class MainPageLocators:
    # Lokator dla przycisku wyszukiwania na stronie wyszukiwarki w formie xpath
    SEARCH_BTN = "//input[@name='btnK']"

    # Użyłem tu drugiego sposobu lokalizowania elemntów w DOM. Staticmethod nie przyjmuje self, co oznacza,
    # że nie ma dostępu do instancji klasy.
    @staticmethod
    def search_input(page: Page):
        return page.get_by_label("Szukaj", exact=True)
