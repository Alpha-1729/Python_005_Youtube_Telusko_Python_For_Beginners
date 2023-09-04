#!/usr/bin/python3
# Types Of Variables In Class

"""
>>>> Types of variables in class.
        Instance variable.
        Class (Static) variable.
>>>>
>>>>
>>>>
>>>>
>>>>
"""


class Car:
    # This is a class variable.
    # This will be constant for all the objects.
    wheels = 4

    def __init__(self):
        # These are instance variables.
        self.mileage = 10
        self.brand = "BMW"


c1 = Car()
c2 = Car()

# Changing the value of the class variable.
Car.wheels = 5

# Printing the class variable.
print(Car.wheels)

print(c1.mileage, c1.brand, c1.wheels)
print(c2.mileage, c2.brand, c2.wheels)
