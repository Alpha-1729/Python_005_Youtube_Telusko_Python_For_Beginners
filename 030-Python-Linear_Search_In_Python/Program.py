#!/usr/bin/python3
# Linear Search In Python

"""
>>>>
>>>>
>>>>
>>>>
>>>>
>>>>
"""

pos = -1


def search(num_list, search_key):
    for i in range(len(num_list)):
        if list[i] == search_key:
            globals()["pos"] = i
            return True
    return False


num_list = [5, 7, 4, 9, 6, 3]
search_key = 3
if search(num_list, search_key):
    print("Found at", pos + 1)
else:
    print("Not Found")