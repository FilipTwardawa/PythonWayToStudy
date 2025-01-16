# Create a function that takes 2 arguments (string type ) name and surname , a
# then returns a string according to the formula Hi {name} {surname}! You should
# run the function, write the result of the function execution to a variable, and then
# display it ( print )

def show_personal_information(name: str, surname: str) -> str:
    return f"Hello {name} {surname} !"


result = show_personal_information("Adam", "Bodnar")

print(result)
