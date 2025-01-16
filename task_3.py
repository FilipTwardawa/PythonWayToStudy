# Create a function that will check if the number passed in the
# parameter is even and return this information as a bool logical type
# ( True / False ). Run the function, write the result of execution to a
# variable, and then using the logical condition display the correct
# text “Even number” / “Odd number”.


def check_for_an_even_number(number: int) -> bool:
    return number % 2 == 0


result = check_for_an_even_number(7)

if result:
    print("Even")
else:
    print("Odd")
