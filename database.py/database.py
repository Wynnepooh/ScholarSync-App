import sqlite3.py

def create_connection():
    """ Establish a connection to the SQLite database. """
    conn = None
    try:
        # This matches the file seen in your VS Code explorer
        conn = sqlite3.connect('slnx.sqlite')
        print("SAB-2: Connection to SQLite successful")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")
    return conn

# Initialize the database connection
connection = create_connection()