# Create a function that takes 2 arguments of type list and returns a result of type
# list . The function is to combine the passed lists into one, remove
# duplicates, raise each element to the power of 3, and then return the
# the resulting list.

def combine_two_lists(l1: list, l2: list):
    new_list = set(l1 + l2)
    new_list = [e ** 3 for e in new_list]
    return new_list


result = combine_two_lists([1, 2, 3, 4], [1, 4, 5])
print("New list : ", result)
