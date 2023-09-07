#!/usr/bin/python3
# Python Mysql Connectivity

"""
>>>> pip install mysql-connector-python
>>>> Run the below script in MySql WorkBench.
        ALTER USER 'root'@'localhost' IDENTIFIED BY 'actual_password' PASSWORD EXPIRE NEVER;
        ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'actual_password';
>>>>
>>>>
>>>>
>>>>
"""

import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="school",
    auth_plugin="mysql_native_password",
)

my_cursor = my_db.cursor()

my_cursor.execute("SELECT * FROM students;")

# Getting all the entries from cursor.
all_student = my_cursor.fetchall()

# Fetching only one record from the result;
first_student = my_cursor.fetchone()

for i in all_student:
    print(i)