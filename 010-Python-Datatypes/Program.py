#!/usr/bin/python3
# Datatypes

"""
>>>> Datatypes in python.
        Main datatypes in python are:
        None
        Numeric
        Sequence:
            List
            Tuple
            Set
            String
            Range
        Dictionary
>>>>
>>>>
>>>>
>>>>
>>>>
"""

# None
# A variable that is not assigned a value will be assigned None.

# Complex.
complex_num = complex(2, 5)
print(complex_num)  # The output will be 2 + 5j

# Boolean
# In python, True is always 1 and False is always 0.

# Range
type(range(1, 10))

# Dictionary
dic_1 = {"a": 1, "b": 2, "c": 3}
# View all keys in the dictionary.
dic_1.keys()
# View all values in the dictionary.
dic_1.values()
# To get value of a key in the dictionary.
dic_1["a"]
dic_1.get("a")

# Unary operator in python.
#  - for negation
# a = 2
# -a means -2

# Bitwise inversion.
# ~ for bitwise inversion.
# The bit-wise inversion of x is defined as -(x + 1).
# ~2 = -3