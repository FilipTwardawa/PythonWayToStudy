# Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu
# list . Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć
# duplikaty, każdy element podnieść do potęgi 3 stopnia, a następnie zwrócić
# powstałą listę.

def type_hinting(l1: list, l2: list):
    new_list = set(l1 + l2)
    new_list = [e ** 3 for e in new_list]
    return new_list


result = type_hinting([1, 2, 3, 4], [1, 4, 5])
print("Nowa lista : ", result)
