import sqlite3

#Initialize Database
def init_db():
    with sqlite3.connect("library.db") as con:
        cursor=con.cursor()
        #Books Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       title TEXT NOT NULL,
                       author TEXT NOT NULL,
                       published_date TEXT,
                       pages INTEGER)
                       """)
        #Members Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS members (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       email TEXT NOT NULL,
                       password TEXT NOT NULL)
                       """)
        con.commit()