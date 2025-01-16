# Create a function that takes 3 arguments of type int and checks whether the sum of the
# of the first two numbers is greater than or equal to the third, and then returns this
# information as a bool logical type

def is_sum_greater_or_equal_third(number1: int, number2: int, number3: int) -> bool:
    return number1 + number2 >= number3


print(is_sum_greater_or_equal_third(1, 1, 3))
