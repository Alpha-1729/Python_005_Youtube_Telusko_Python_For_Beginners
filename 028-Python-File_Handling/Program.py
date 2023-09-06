#!/usr/bin/python3
# File Handling

"""
>>>>
>>>>
>>>>
>>>>
>>>>
>>>>
"""

# Reading the file and printing each line.
f = open("data.txt", "r")
print(f.readline())  # Printing the first line.
print(f.readline())  # Printing the next line.
print(f.readline())  # Printing the next line.
print(f.readline(2))  # Printing only two letters of the next line.
# Closing the file.
f.close()

# Reading the file and save the content into a list.
f = open("data.txt", "r")
list_1 = f.readlines()
print(list_1)
f.close()

# Reading the content from one file and writing to other file.
f = open("data.txt", "r")
f_copy = open("data_copy.txt", "w")
for data in f:
    f_copy.write(data)
f.close()
f_copy.close()

# Copying content of one image into other.
f = open("parrot.jpg", "rb")
f_copy = open("parrot_copy.jpg", "wb")
for data in f:
    f_copy.write(data)
f.close()
f_copy.close()
