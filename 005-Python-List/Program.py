#!/usr/bin/python3
# List

"""
>>>> List is mutable.
>>>>
>>>>
>>>>
>>>>
>>>>
"""

num = [1, 2, 3, 4]
name = ['naveen', 'raj', 'arch']

# Nested list.
content = [num, name]
print(content)

# It will remove the first instance of the object.
num.remove(1)

# It will clear the list.
num.clear()
print(num)

# First parameter is the position and second is the object.
num.insert(2, 10)
print(num)

# It will the remove object in a index.
# It will remove the first object in the list.
num.pop(0)

# pop method without the parameter.
# It will remove the last element in the list.
num.pop()

# It is used to remove multiple values from the list.
# It will remove the all element after the second element from the list.
del num[2:]

# extends method.
# Parameter of  the extends function is a list.
num.extend([10, 11, 21, 33])

# Sort in descending order
num.sort(reverse=True)

# Sort in ascending order.
num.sort() 

