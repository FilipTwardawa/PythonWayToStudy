# ------------------------------------Task 2 ----------------------------------------------------------------------
# #############################  a)  #########################################

def show_first_names(names):
    for name in names:
        print(name)


print("\nTask 2. a) Create a function that receives a list of 5 names in a parameter and then displays each name.")
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
    "\nTask 2 b)\n"
    "Create a function that receives a list containing 5 arbitrary numbers as a parameter, multiplies each element of it "
    "by 2, and finally return it.\n Use the function          Use the collapsible list\n",
    result_of_multiplication_by_2_loop, result_of_multiply_numbers_by_two_folding_list)


# #############################  b)  #########################################

# #############################  c)  #########################################
def show_even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)


print("\nTask 2 c)"
      "\nCreate a function that receives a list of 10 numbers in a parameter(recommended use of the range function),"
      "and then displays only even elements.")
show_even_numbers(range(10))


# #############################  c)  #########################################

# #############################  d)  #########################################
def show_every_second_number(numbers):
    for idx in range(0, len(numbers), 2):
        print(numbers[idx])

print("\nTask 2 d)"
      "\nCreate a function that receives a list of 10 numbers in a parameter(recommended use of the range function ),"
      "and then displays every second element.")
show_every_second_number(range(10))

# #############################  d)  #########################################


# ------------------------------------Task 2 ----------------------------------------------------------------------
