import time
from POM.main_page import MainPage
import pytest

from POM.search_restults import SearchResultsPage


 def test_main_page(main_page: MainPage) -> None:
     # Otwarcie strony do testów
     main_page.goto_link()
     # Wymagane asercje
     main_page.assertions()


def test_search(main_page: MainPage, search_results_page: SearchResultsPage) -> None:
    # Tekst, który wyszukujemy. W Oficjalnych testach webowych można użyć dekoratora pytest.mark.parametrize
    text_to_search = "energotest"
    # Otwarcie strony do testów
    main_page.goto_link()
    main_page.search_text(text_to_search)
    # Asercje wyników
    search_results_page.verify_results()
