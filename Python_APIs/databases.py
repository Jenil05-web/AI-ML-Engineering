##  Working with databases in python

import sqlite3

# connect to database
connection = sqlite3.connect('my_database.db') # this will create an new database file if dosent exist

cursor = connection.cursor() # this will create a cursor object to execute sql commands

cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''') # this will create a new table called users if it dosent exist

connection.commit() # this will save the changes to the database

connection.close() # this will close the connection to the database
