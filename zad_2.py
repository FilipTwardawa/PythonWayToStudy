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

# #############################  c)  #########################################
def show_even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)


print("\nZadanie 2 c)"
      "\nUtwórz funkcję, która otrzyma w parametrze listę 10 liczb(rekomendowane wykorzystanie funkcji range ),"
      "a następnie wyświetli jedynie parzyste elementy.")
show_even_numbers(range(10))


# #############################  c)  #########################################

# #############################  d)  #########################################
def show_every_second_number(numbers):
    for idx in range(0, len(numbers), 2):
        print(numbers[idx])

print("\nZadanie 2 d)"
      "\nUtwórz funkcję, która otrzyma w parametrze listę 10 liczb(rekomendowane wykorzystanie funkcji range ),"
      "a następnie wyświetli co drugi element.")
show_every_second_number(range(10))

# #############################  d)  #########################################


# ------------------------------------Zadanie 2 ----------------------------------------------------------------------
