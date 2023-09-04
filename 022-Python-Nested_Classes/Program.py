#!/usr/bin/python3
# Nested Classes

"""
>>>>
>>>>
>>>>
>>>>
>>>>
>>>>
"""


class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.roll_no)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = "Hp"
            self.ram = 8
            self.cpu = "i5"

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student("Navin", 2)
s2 = Student("Hari", 3)
lap1 = s1.lap
lap2 = s2.lap

print(lap1.brand)
print(s1.lap.brand)

# Calling the show method inside the student class.
print(s1.show())

# Calling the inside class directly.
laptop1 = Student.Laptop()
print(laptop1.brand)

# Calling the show method inside the laptop class.
laptop1.show()
