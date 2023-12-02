import sqlite3
import pickle

class ExampleClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value

def showdata(name):
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





    # Fetch the object from the database based on the name
    cursor.execute('SELECT data FROM Bill WHERE name = ?', (name,))
    row = cursor.fetchone()

    if row:
        # Deserialize the object using pickle
        fetched_object = pickle.loads(row[0])
        
        # Print the fetched object
        print(f"Fetched Object Name: {fetched_object.name}")
        print(f"Fetched Object Value: {fetched_object.value}")
        print('-' * 20)
        
        return fetched_object.value
        
    

# Close the connection
    

    conn.close()

#ss=showdata("admin")
#print(ss)





def showdata2(name,DB):
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





    # Fetch the object from the database based on the name
    cursor.execute('SELECT data FROM Bill WHERE name = ?', (name,))
    row = cursor.fetchone()

    if row:
        # Deserialize the object using pickle
        fetched_object = pickle.loads(row[0])
        
        # Print the fetched object
        print(f"Fetched Object Name: {fetched_object.name}")
        print(f"Fetched Object Value: {fetched_object.value}")
        print('-' * 20)
        
        return fetched_object.value
        
    

# Close the connection
    

    conn.close()

#ss=showdata("admin")
#print(ss)