# ------------------------------------Zadanie 2 ----------------------------------------------------------------------
# #############################  a)  #########################################

def show_first_names(names):
    for name in names:
        print(name)


print("\nZadanie 2. a) Utwórz funkcję, która otrzyma w parametrze listę 5 imion, a następnie wyświetli każde z nich.")
show_first_names(["Magda", "Bartek", "Cecylia", "Romek", "Ewelina"])


# #############################  a)  #########################################

# #############################  b)  #########################################
def multiply_numbers_by_two_loop(numbers):
    result_of_multiplying = []
    for number in numbers:
        result_of_multiplying.append(number * 2)
    return result_of_multiplying


result_of_multiplication_by_2_loop = multiply_numbers_by_two_loop([4, 23, 33, 14, 28])


def multiply_numbers_by_two_folding_list(numbers):
    return [number * 2 for number in numbers]


result_of_multiply_numbers_by_two_folding_list = multiply_numbers_by_two_folding_list([4, 23, 33, 14, 28])

print(
    "\nZadanie 2 b)\n"
    "Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5 dowolnych liczb, każdy jej element pomnoży "
    "przez 2, a na końcu ją zwróci.\n Użyj funkcji        Użyj listę składaną\n",
    result_of_multiplication_by_2_loop, result_of_multiply_numbers_by_two_folding_list)

# #############################  b)  #########################################

# ------------------------------------Zadanie 2 ----------------------------------------------------------------------
