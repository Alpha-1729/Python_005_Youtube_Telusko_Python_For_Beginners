#!/usr/bin/python3
# Inheritance In Oop

"""
>>>> Inheritance in object oriented programming.
        Single level inheritance.
        Multi-Level Inheritance.
        Multiple Inheritance.
>>>>
>>>>
>>>>
>>>>
>>>>
"""


# Single level inheitance.
class A:
    pass


# Multi-Level inheritance.
# Hera B can access the functions of the A.
class B(A):
    pass


# Here C can access the functions of the A and B
class C(B):
    pass


class D:
    pass


# Multiple inheritance
# Here E can access the feature of the A and D.
class E(A, D):
    pass
