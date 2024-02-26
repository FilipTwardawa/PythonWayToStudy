# Stworzyć funkcję, która przyjmie 3 argumenty typu int i sprawdzi czy suma
# dwóch pierwszych liczb jest większa lub równa trzeciej, a następnie zwróci tę
# informację jako typ logiczny bool

def is_sum_greater_or_equal_third(number1: int, number2: int, number3: int) -> bool:
    sum_of_first_two_numbers = number1 + number2
    if sum_of_first_two_numbers >= number3:
        return True
    return False


print(is_sum_greater_or_equal_third(1, 1, 3))
