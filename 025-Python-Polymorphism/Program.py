#!/usr/bin/python3
# Polymorphism

"""
>>>> Types of Polymorphism.
        Duck Typing
        Operator OverLoading
        Method OverLoading
        Method Overriding
>>>>
>>>>
>>>>
>>>>
>>>>
"""

# Duck Typing
# If anything that walk like a duck, then its is a duck.


class Pycharm:
    def execute(self):
        print("compiling")
        print("exiting")


class MyEditor:
    def execute(self):
        print("spell check")
        print("compiling")
        print("normal check")
        print("exiting")


class Laptop:
    def code(self, ide):
        ide.execute()


ide = MyEditor()
lap1 = Laptop()
lap1.code(ide)

# Operator Overloading.
a = 5
b = 6
print(a + b)

# This method is calling behind the scene.
# + means calling the add method.
print(int.__add__(a, b))


class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    # Override the existing implementation for the add method.
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3


s1 = Student(20, 30)
s2 = Student(34, 44)
s3 = s1 + s2
print(s3.m1)


# Method Overloading.
# It means method with same name and different signature.
# We cannot create same method with 2 parameter and 3 parameter in python.
# Other way is to use default value to all the parameter in the method.


class Summation:
    def add(self, a=None, b=None, c=None):
        s = 0
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a
        return s


p = Summation()
print(p.add(1, 2, 7))


# Method Overriding.
# If a child class is inheriting from the parent class, then the child can override the existing implementation in the parent class.


class A:
    def show(self):
        print("Show in A")


class B(A):
    def show(self):
        print("Show in B")


a1 = B()
a1.show()
