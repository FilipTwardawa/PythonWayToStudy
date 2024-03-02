# Stworzyć następujące klasy:
# Library (klasa opisująca bibliotekę), posiadająca pola:
# city
# street
# zip_code
# open_hours (str)
# phone
# Employee (klasa opisująca pracownika biblioteki), posiadająca pola:
# first_name
# last_name
# hire_date
# birth_date
# city
# street
#
# Obiektowość (OOP) 5
#
# zip_code
# phone
# Book (klasa opisująca książkę), posiadająca pola
# library
# publication_date
# author_name
# author_surname
# number_of_pages
# Order (klasa opisująca zamówienie), posiadająca pola:
# employee
# student
# books (lista obiektów klasy Book)
# order_date
# Dodatkowo:
# Każda klasa ma mieć zaimplementowaną metodę __str__ , która będzie
# opisywała obiekt oraz ewentualne obiekty znajdujące się w tym obiekcie
# (np. obiekt Library w obiekcie Book).
# Pola w klasie mają być zdefiniowane jako atrybuty ustawiane podczas
# tworzenia instancji klasy za pośrednictwem konstruktora.
# Stworzyć 2 biblioteki (2 instancje klasy), 5 książek, 3 pracowników, 3
# studentów, oraz 2 zamówienia.
# Wyświetlić oba zamówienia ( print )

class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Biblioteka: {self.city}, ul. {self.street}, {self.zip_code}\nGodziny otwarcia: {self.open_hours}\nTelefon: {self.phone}"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street

    def __str__(self):
        return f"Pracownik: {self.first_name} {self.last_name}\nData zatrudnienia: {self.hire_date}\nData urodzenia: {self.birth_date}\nAdres: {self.city}, ul. {self.street}"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Książka: {self.author_name} {self.author_surname}\nData publikacji: {self.publication_date}\nLiczba stron: {self.number_of_pages}\nBiblioteka: {self.library}"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_list = "\n".join([f"- {book}" for book in self.books])
        return f"Zamówienie:\nData zamówienia: {self.order_date}\n{self.employee}\n{self.student}\nKsiążki:\n{book_list}"


# Tworzenie instancji
biblioteka1 = Library("Kraków", "Długa 15", "30-001", "Pon-Pt: 9:00-17:00", "123-456-789")
biblioteka2 = Library("Warszawa", "Krótka 5", "00-001", "Pon-Pt: 8:00-16:00", "987-654-321")

pracownik1 = Employee("Jan", "Kowalski", "2023-01-15", "1990-05-10", "Kraków", "Krótka 3")
pracownik2 = Employee("Anna", "Nowak", "2022-11-20", "1985-12-25", "Warszawa", "Długa 10")
pracownik3 = Employee("Michał", "Wiśniewski", "2023-03-05", "1995-08-15", "Kraków", "Szeroka 8")

ksiazka1 = Book(biblioteka1, "2022-10-01", "Adam", "Mickiewicz", 300)
ksiazka2 = Book(biblioteka1, "2021-05-15", "Henryk", "Sienkiewicz", 450)
ksiazka3 = Book(biblioteka2, "2023-02-28", "Juliusz", "Słowacki", 250)
ksiazka4 = Book(biblioteka2, "2023-01-10", "Bolesław", "Prus", 380)
ksiazka5 = Book(biblioteka2, "2023-04-20", "Stanisław", "Lem", 200)

zamowienie1 = Order(pracownik1, "Karolina Nowak", [ksiazka1, ksiazka3, ksiazka5], "2024-02-28")
zamowienie2 = Order(pracownik2, "Piotr Kowalczyk", [ksiazka2, ksiazka4], "2024-03-01")

# Wyświetlanie zamówień
print("Zamówienie 1:")
print(zamowienie1)
print("\nZamówienie 2:")
print(zamowienie2)
