# Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list , a drugi
# typu int . Funkcja ma sprawdzić (zwracając typ logiczny bool ), czy lista z
# parametru pierwszego zawiera taką wartość jaką przekazano w parametrze
# drugim.

def check_that_the_same_values(numbers: list, number: int) -> bool:
    return number in numbers


result = check_that_the_same_values([12, 23, 444, 3, 2], 12)

print("Czy ta sama wartość w liście co parametr dwa : ", result)
