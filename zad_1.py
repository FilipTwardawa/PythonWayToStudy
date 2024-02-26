# Stworzyć funkcję, która przyjmuje 2 argumenty (typu string ) name i surname , a
# następnie zwróci stringa zgodnie ze wzorem Cześć {name} {surname}! Należy
# uruchomić funkcję, wynik wykonania funkcji zapisać do zmiennej, a następnie
# go wyświetlić ( print )

def show_personal_information(name: str, surname: str) -> str:
    return f"Cześć {name} {surname} !"


result = show_personal_information("Adam", "Bodnar")

print(result)
