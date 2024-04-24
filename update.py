# Perform Update operation in SQLite
try:
    # Update a record in the SQLite table
    # Executes an UPDATE query to update the course of the record with id=1 to 'Mathematics'
    c.execute("UPDATE students SET course='Mathematics' WHERE id=1")
    print('SQLite update successful')
except Exception as e:
    print(f'SQLite update failed: {e}')

# Perform Update operation in NoSQL (Python dictionary)
try:
    # Update a record in the Python dictionary
    # Updates the course field of the record with key 1 in the Python dictionary to 'Mathematics'
    students_nosql[1]['course'] = 'Mathematics'
    print('NoSQL update successful')
except Exception as e:
    print(f'NoSQL update failed: {e}')
