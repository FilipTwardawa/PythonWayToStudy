# Stworzyć następujące klasy:
# Property (klasa opisująca posiadłość/nieruchomość), posiadająca
# pola:
# area
#
# Obiektowość (OOP) 6
#
# rooms (int)
# price
# address
# House (klasa dziedzicząca klasę Property , która opisuje dom),
# posiadająca pola:
# plot (rozmiar działki, int)
# Flat (klasa dziedzicząca klasę Property , która opisuje mieszkanie),
# posiadająca pola:
# floor
# Dodatkowo:
# Każda z klas dziedziczących ma mieć zaimplementowaną metodę
# __str__ , która będzie opisywała obiekt.
# Pola w klasie mają być zdefiniowane jako atrybuty ustawiane podczas
# tworzenia instancji klasy za pośrednictwem konstruktora.
# Stworzyć po jednym obiekcie klasy House oraz Flat, a następnie je
# wyświetlić.

class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Powierzchnia: {self.area}, Pokoje: {self.rooms}, Cena: {self.price}, Adres: {self.address}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"{super().__str__()}, Działka: {self.plot}"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"{super().__str__()}, Piętro: {self.floor}"


dom = House(area=150, rooms=5, price=300000, address="ul. Główna 123", plot=500)
mieszkanie = Flat(area=80, rooms=3, price=150000, address="ul. Lipowa 456", floor=2)

print("Dom:")
print(dom)
print("\nMieszkanie:")
print(mieszkanie)
