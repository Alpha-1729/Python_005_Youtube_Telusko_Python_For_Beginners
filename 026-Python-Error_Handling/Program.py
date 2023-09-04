#!/usr/bin/python3
# Error Handling

"""
>>>> Types of Error.
        Compile time
            Syntactical error done by the programmer.
        Logical
            Code get compiled, but gives wrong input.
        Run time
            Code get compiled, there is no logical error.
            Code don't work for specific inputs.
            Eg: Divide By Zero
>>>>
>>>>
>>>>
>>>>
>>>>
"""

a = 5
b = 2

try:
    print("Resource open")
    print(a / b)
    k = int(input("Enter a number: "))
    print(k)
except ZeroDivisionError as e:
    print("You cannot divide a number by zero")
except ValueError as e:
    print("Value error")
except Exception as e:
    print("Something Went Wrong")
finally:
    print("Resource closed")
