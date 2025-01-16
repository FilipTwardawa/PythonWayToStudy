# Create a class Student , which has 2 parameters (name and marks) and one
# method is_passed, which returns a logical value, positive when the average
# marks is > 50 otherwise negative. Next, you need to
# create 2 sample objects of the class, so that for the first object the method
# returns true , and for the second false .

from statistics import mean


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return mean(self.marks) > 2.5


student1 = Student("Edward Kaminski", [4, 5, 4, 5, 5])
student2 = Student("Alicja Przybylska", [2, 2, 3])

# Checking whether students have passed
print(student1.name, "passed:", student1.is_passed())
print(student2.name, "passed:", student2.is_passed())
