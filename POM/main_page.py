from locators.main_page_locators import MainPageLocators
from playwright.sync_api import Page, expect


class MainPage:
    # Instancja klasy. Definiuję tu eementy, które używam w testach
    path = "https://www.google.com/"
    def __init__(self, page: Page):
        self.page = page
        self.search_btn = page.locator(MainPageLocators.SEARCH_BTN).first
        # search_input jest metodą, więc musimy ją wywołać aby zwróciła odpowiedni element
        self.search_input = MainPageLocators.search_input(page)
    #Asercja według instrukcji
    def assertions(self) -> None:
        expect(self.search_btn, "Inna wartość na przycisku niż podana w instrukcji").to_have_value("Szukaj w google")

    def search_text(self, text_to_search: any) -> None:
        expect(self.search_input).to_be_empty()
        self.search_input.fill(text_to_search)
        self.search_btn.click()

    '''Nie jest to najlepsze rozwiązanie otwierania linków. W typowych testach używam klasy nadrzędnej
    w której zdefinowana jest ta metoda a w plikach POM definiuję tylko zmienną path, którą przyjmuje metoda
    W klasie podrzędnej'''

    def goto_link(self) -> None:
        self.page.goto(MainPage.path)
        # Obsługa popup z cookies
        self.reject_cookies()

    '''Dla prostoty testu po prostu stworzyłem metodę, która odrzuca cookie poprzez przycisk.
    W rozbudowanym teście można
    Skorzystać z session storages https://playwright.dev/python/docs/auth#session-storage i stan przechowywać w pliku .json
    następnie odczytywać dany stan. Niniejsze rozwiązanie też jest poprawne i ogólnie akceptowane'''
    def reject_cookies(self) -> None:
        self.page.get_by_role("button", name="Odrzuć wszystko").click()
