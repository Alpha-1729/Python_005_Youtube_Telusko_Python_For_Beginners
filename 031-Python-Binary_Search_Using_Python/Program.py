#!/usr/bin/python3
# Binary Search Using Python

"""
>>>> Binary search using python.
        Applicable only to sorted list.
>>>>
>>>>
>>>>
>>>>
>>>>
"""
pos = -1


def binary_search(num_list, search_key):
    lower_bound = 0
    upper_bound = len(num_list) - 1
    while lower_bound <= upper_bound:
        mid_index = (lower_bound + upper_bound) // 2
        if num_list[mid_index] == search_key:
            globals()["pos"] = mid_index
            return True
        else:
            # Updating the lower and upper bound.
            if num_list[mid_index] < search_key:
                lower_bound = mid_index + 1
            else:
                upper_bound = mid_index - 1
    return False


num_list = [2, 5, 13, 56, 134, 356]
search_key = 13

if binary_search(num_list, search_key):
    print("Found at", pos + 1)
else:
    print("Not Found")
