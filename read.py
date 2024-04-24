# Perform Read operation in SQLite
# Read a record from the SQLite table
# Executes a SELECT query to retrieve a record from the SQLite table where id=1 and prints the result.
c.execute("SELECT * FROM students WHERE id=1")
print("SQLite - Read Operation:", c.fetchone())

# Perform Read operation in NoSQL (Python dictionary)
# Read a record from the Python dictionary
# Uses the get method of the dictionary to retrieve a record with key 1 and prints the result.
print("NoSQL - Read Operation:", students_nosql.get(1))
