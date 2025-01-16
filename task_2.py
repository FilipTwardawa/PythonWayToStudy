# Create the following classes:
# Library (class describing a library), having fields:
# city
# street
# zip_code
# open_hours (str)
# phone
# employee (a class describing a library employee), having fields:
# first_name
# last_name
# hire_date
# birth_date
# city
# street
#
# objectivity (OOP) 5
#
# zip_code
# phone
# book (a class describing a book), having fields
# library
# publication_date
# author_name
# author_surname
# number_of_pages
# order (class describing an order), having fields:
# employee
# student
# books (list of objects of class Book)
# order_date
# In addition:
# Each class is to have a __str__ method implemented, which will
# describe the object and any objects contained in that object
# (e.g. the Library object in the Book object).
# The fields in the class are to be defined as attributes that are set during the
# creating an instance of the class via the constructor.
# Create 2 libraries (2 instances of the class), 5 books, 3 employees, 3
# students, and 2 orders.
# Display both orders ( print )

class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library: {self.city}, ul. {self.street}, {self.zip_code}\nOpening Hours:: {self.open_hours}\nPhone Number: {self.phone}"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}\nDate of hire: {self.hire_date}\nDate of birth: {self.birth_date}\nAddress: {self.city}, {self.street}  street"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book: {self.author_name} {self.author_surname}\nPublication date: {self.publication_date}\nNumber of pages: {self.number_of_pages}\nLibrary: {self.library}"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_list = "\n".join([f"- {book}" for book in self.books])
        return f"Order:\nOrder date: {self.order_date}\n{self.employee}\n{self.student}\nBooks:\n{book_list}"


# Tworzenie instancji
library1 = Library("Kraków", "Długa 15", "30-001", "Pon-Pt: 9:00-17:00", "123-456-789")
library2 = Library("Warszawa", "Krótka 5", "00-001", "Pon-Pt: 8:00-16:00", "987-654-321")

employee1 = Employee("Jan", "Kowalski", "2023-01-15", "1990-05-10", "Kraków", "Krótka 3")
employee2 = Employee("Anna", "Nowak", "2022-11-20", "1985-12-25", "Warszawa", "Długa 10")
employee3 = Employee("Michał", "Wiśniewski", "2023-03-05", "1995-08-15", "Kraków", "Szeroka 8")

book1 = Book(library1, "2022-10-01", "Adam", "Mickiewicz", 300)
book2 = Book(library1, "2021-05-15", "Henryk", "Sienkiewicz", 450)
book3 = Book(library2, "2023-02-28", "Juliusz", "Słowacki", 250)
book4 = Book(library2, "2023-01-10", "Bolesław", "Prus", 380)
book5 = Book(library2, "2023-04-20", "Stanisław", "Lem", 200)

order1 = Order(employee1, "Karolina Nowak", [book1, book3, book5], "2024-02-28")
order2 = Order(employee2, "Piotr Kowalczyk", [book2, book4], "2024-03-01")

# Displaying orders
print("Order 1:")
print(order1)
print("\nOrder 2:")
print(order2)
