#!/usr/bin/python3
# Classes And Object

"""
>>>>
>>>>
>>>>
>>>>
>>>>
>>>>
"""


class Computer:
    def config(self):
        print("i5, 16GB, 1TB")


com_1 = Computer()
com_2 = Computer()

# Calling methods inside class.
com_1.config()
Computer.config(com_1)

com_2.config()
Computer.config(com_2)
