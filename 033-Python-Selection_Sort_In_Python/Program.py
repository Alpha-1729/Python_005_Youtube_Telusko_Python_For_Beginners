#!/usr/bin/python3
# Selection Sort In Python

""" Advantage of selection sort.
        We are not swapping multiple times like in bubble sort.
        We are swapping only one time after each iteration.
>>>>
>>>>
>>>>
>>>>
>>>>
>>>>
"""


def selection_sort(num_list):
    for i in range(len(num_list) - 1):
        min_pos = i
        for j in range(i, len(num_list)):
            if num_list[j] < num_list[min_pos]:
                min_pos = j
        # Swapping
        num_list[i], num_list[min_pos] = num_list[min_pos], num_list[i]
    return num_list


num_list = [4, 1, 25, 7, 8, 14, 3, 69, 5, 0]
print(selection_sort(num_list))