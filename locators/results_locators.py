class ResultsLocators:
    NEXT_PAGE = "//span[contains(text(),'Następna')]"

    """Nie Jest to najbardziej optymalne rozwiązanie znalezienia linku w
    Wynikach wyszukiwania google. Konstrukcja strony niestety nie pozwala
    na lepsze zlokalizowanie wymaganego linku. W tym momencie znajduję wszystkie
    linki na stronie, nawet paginacje i górną belkę"""
    LINK = "//a"