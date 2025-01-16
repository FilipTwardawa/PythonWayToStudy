# Create a function that takes 2 arguments. The first of type list , and the second
# of type int . The function is to check (returning a Boolean type bool ) whether the list from the
# parameter one contains such a value as passed in the parameter
# the second one.

def check_that_the_same_values(numbers: list, number: int) -> bool:
    return number in numbers


result = check_that_the_same_values([12, 23, 444, 3, 2], 12)

print("Is the same value in the list as parameter two : ", result)
