# Create the following classes:
# Property (a class describing property/real estate), having.
# fields:
# area
#
# Objectivity (OOP) 6
#
# rooms (int)
# price
# address
# House (class inheriting Property class , which describes a house),
# having fields:
# plot (plot size, int)
# Flat (class inheriting the Property class , which describes an apartment),
# having fields:
# floor
# In addition:
# Each inheriting class is to have implemented a method
# __str__ , which will describe the object.
# The fields in the class are to be defined as attributes that are set during the
# creation of an instance of the class via the constructor.
# Create one object each of the House and Flat classes, and then display them.
# display.

class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Area: {self.area}, Rooms: {self.rooms}, Price: {self.price}, Address: {self.address}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"{super().__str__()}, Plot: {self.plot}"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"{super().__str__()}, Floor: {self.floor}"


home = House(area=150, rooms=5, price=300000, address="ul. Główna 123", plot=500)
apartment = Flat(area=80, rooms=3, price=150000, address="ul. Lipowa 456", floor=2)

print("Home:")
print(home)
print("\nApartment:")
print(apartment)
