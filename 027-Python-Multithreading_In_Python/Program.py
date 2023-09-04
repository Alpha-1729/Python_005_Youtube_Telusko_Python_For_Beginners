#!/usr/bin/python3
# Multithreading In Python

"""
>>>> Multithreading in python.
        When we divide a large task into small task, each small task is called the threads.
>>>>
>>>>
>>>>
>>>>
>>>>
"""

from threading import Thread
from time import sleep


class Hello(Thread):
    # The function name should be always run.
    def run(self):
        for i in range(100):
            print("Hello")
            sleep(0.1)


class Hii(Thread):
    # The function name should be always run.
    def run(self):
        for i in range(100):
            print("Hii")
            sleep(0.1)


t1 = Hello()
t2 = Hii()

t1.start()  # This will call the run method inside the class.
sleep(0.2)
t2.start()  # This will call the run method inside the class.

# Waiting for t1 and t2 thread to complete.
t1.join()
t2.join()

print("Bye")