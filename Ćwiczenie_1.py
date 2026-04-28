def czy_palindrom(slowo):
    """
    Sprawdza, czy podany wyraz jest palindromem.
    Argument: slowo (string)
    Zwraca: boolean (True/False)
    """
    return slowo == slowo[::-1]

slowa = ["kajak", "butelka", "długopis", "anna", "woda"]
wyniki = [czy_palindrom(s) for s in slowa]

print(wyniki)