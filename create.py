# SQL
# SQLite Setup: Sets up an in-memory SQLite database and creates a table named students with columns id, name, age, and course. Inserts a record into the table.
# Import necessary libraries
import sqlite3

# Connect to the SQLite database (in-memory)
conn = sqlite3.connect(':memory:')
c = conn.cursor()

# Create a table in SQLite database
c.execute('''CREATE TABLE students
             (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, course TEXT)''')
print("SQLite table 'students' created successfully.")

# Insert some data into the SQLite table
c.execute("INSERT INTO students (name, age, course) VALUES ('Alice', 20, 'Computer Science')")
print("Record inserted into SQLite table 'students'.")

# NoSQL
# Simulate a NoSQL database using a Python dictionary
students_nosql = {
    1: {'name': 'Alice', 'age': 20, 'course': 'Computer Science'}
}
print("NoSQL database 'students_nosql' created successfully.")
