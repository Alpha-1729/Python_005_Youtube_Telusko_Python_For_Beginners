#!/usr/bin/python3
# Init Method

"""
>>>> __init__ is same as constructor in other programming languages.
>>>>
>>>>
>>>>
>>>>
>>>>
"""


class Computer:
    def __init__(self, cpu, ram) -> None:
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Ram:", self.ram, "CPU:", self.cpu)


com_1 = Computer("i5", "8GB")
com_2 = Computer("i7", "16GB")

com_1.config()
com_2.config()
