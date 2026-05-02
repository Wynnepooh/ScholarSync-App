import sqlite3

def setup_database():
    conn= sqlite3.connect('sinx.sqlite')
    cursor= conn.cursor()

    cursor.execute('''
        CREATE  TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT NOT NULL UNIQUE,
                   TEXT NOT  NULL,
                   student_id Text UNIQUE
                           )
                          ''')
 
    conn.commit()
    print("SAB-2: Users table is ready.")
    conn.close()

if __name__ == "_main_":
    setup_database()






  
  

  


