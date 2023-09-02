#!/usr/bin/python3
# Id Function

"""
>>>> id function.
        id() returns the memory address of the variable.
>>>>
>>>>
>>>>
>>>>
>>>>
"""

# When both variables have same data.
# They point to same memory address.
# This is why python is memory efficient.
num_1 = 5
print(id(num_1))

# We can also use id function for a string variable also.
print(id("tiger"))