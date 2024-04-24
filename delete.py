# Perform Delete operation in SQLite
try:
    # Delete a record from the SQLite table
    # Executes a DELETE query to delete the record with id=1 from the SQLite table
    c.execute("DELETE FROM students WHERE id=1")
    print('SQLite delete successful')
except Exception as e:
    print(f'SQLite delete failed: {e}')

# Perform Delete operation in NoSQL (Python dictionary)
try:
    # Delete a record from the Python dictionary
    # Deletes the record with key 1 from the Python dictionary
    del students_nosql[1]
    print('NoSQL delete successful')
except Exception as e:
    print(f'NoSQL delete failed: {e}')
