# Stworzyć klasę Student , która posiada 2 parametry (name i marks) oraz jedną
# metodę is_passed, która zwraca wartość logiczną, pozytywną gdy średnia
# ocen jest > 50 w przeciwnym przypadku negatywną. Następnie należy
# stworzyć 2 przykładowe obiekty klasy, tak aby dla pierwszego obiektu metoda
# zwracała true , a dla drugiego false .

from statistics import mean


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return mean(self.marks) > 2.5


student1 = Student("Edward Kaminski", [4, 5, 4, 5, 5])
student2 = Student("Alicja Przybylska", [2, 2, 3])

# Sprawdzenie, czy studenci zaliczyli
print(student1.name, "zaliczył/a:", student1.is_passed())
print(student2.name, "zaliczył/a:", student2.is_passed())
