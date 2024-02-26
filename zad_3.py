# Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w
# parametrze jest parzysta i zwróci tą informację jako typ logiczny bool
# ( True / False ). Należy uruchomić funkcję, wynik wykonania zapisać do
# zmiennej, a następnie wykorzystując warunek logiczny wyświetlić prawidłowy
# tekst "Liczba parzysta" / "Liczba nieparzysta"


def check_for_an_even_number(number: int) -> bool:
    if number % 2 == 0:
        return True
    return False


result = check_for_an_even_number(7)

if result:
    print("Parzysta")
else:
    print("Nieparzysta")
