#!/usr/bin/python3
# Types Of Method In Python

"""
>>>> Type of methods in python.
        Instance method
        Class method
        Static method
>>>>
>>>>
>>>>
>>>>
>>>>
"""


class Student:
    # Class variable.
    school = "Telusko"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # Instance method.
    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    # Class method.
    # This decorator is compulsory before a class method.
    @classmethod
    def get_school_name(cls):
        return cls.school

    # Static method.
    @staticmethod
    def info():
        print("This a school class in abc module")


s1 = Student(12, 54, 65)
s2 = Student(123, 435, 767)

print(s1.avg())
print(s2.avg())

# Calling class method.
print(Student.get_school_name())

# Calling static method.
Student.info()