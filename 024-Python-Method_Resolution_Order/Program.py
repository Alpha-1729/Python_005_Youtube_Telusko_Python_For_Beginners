#!/usr/bin/python3
# Method Resolution Order

"""
>>>> MRO
        Method Resolution Order
>>>> We can use the super method to call constructor and other methods in parent class.
>>>>
>>>>
>>>>
>>>>
"""


class A:
    def __init__(self):
        print("Class A Initialised")


class B(A):
    def __init__(self):
        print("Class B Initilised")
        super().__init__()  # Calling the constructor of the parent class.


# If an object of the class is created.
# It will try to call the __init__ method(constructor) in the class.
# If it is not there, it will call the __init__ method in the parent class.
# If class has multiple parents, It will run the __init__ method of the first parent.
# This is called Method Resolution Order.
b = B()
