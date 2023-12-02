import sqlite3
import pickle

class ExampleClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value

def savedata(name,value):  
# Connect to the SQLite database (creates a new database if it doesn't exist)
  conn = sqlite3.connect('BillForge.db')

# Create a cursor object to execute SQL queries
  cursor = conn.cursor()

# Define a table if it doesn't exist
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS Bill (
        id INTEGER PRIMARY KEY,
        name TEXT,
        data BLOB
    )
  ''')



# Sample objects to be saved

  obj= ExampleClass(name=name, value=value)
    

# Save the objects to the database

    # Serialize the object using pickle
  serialized_object = pickle.dumps(obj)
    
    # Insert the serialized object into the table along with the name
  cursor.execute('INSERT INTO Bill (name, data) VALUES (?, ?)', (obj.name, serialized_object))

# Commit the changes
  conn.commit()

# Fetch and print the objects based on their names

# Close the connection
  conn.close()


#savedata("admin","swaraj")

def savedata2(name,value,DB):  
# Connect to the SQLite database (creates a new database if it doesn't exist)
  db = DB+".db"
  conn = sqlite3.connect(db)

# Create a cursor object to execute SQL queries
  cursor = conn.cursor()

# Define a table if it doesn't exist
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS Bill (
        id INTEGER PRIMARY KEY,
        name TEXT,
        data BLOB
    )
  ''')



# Sample objects to be saved

  obj= ExampleClass(name=name, value=value)
    

# Save the objects to the database

    # Serialize the object using pickle
  serialized_object = pickle.dumps(obj)
    
    # Insert the serialized object into the table along with the name
  cursor.execute('INSERT INTO Bill (name, data) VALUES (?, ?)', (obj.name, serialized_object))

# Commit the changes
  conn.commit()

# Fetch and print the objects based on their names

# Close the connection
  conn.close()

