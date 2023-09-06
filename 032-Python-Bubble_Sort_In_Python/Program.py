#!/usr/bin/python3
# Bubble Sort In Python

"""
>>>> Bubble sort in python
        Basic strategy is taking the two items in the list and swap two items by comparing each value.
        After the first iteration the largest value will be at the end.
        Number of iteration will reduced after each steps.
>>>>
>>>>
>>>>
>>>>
>>>>
"""


def bubble_sort(num_list):
    for i in range(len(num_list) - 1, 0, -1):
        for j in range(i):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
    return num_list


num_list = [4, 1, 25, 7, 8, 14, 3, 69, 5, 0]
print(bubble_sort(num_list))
