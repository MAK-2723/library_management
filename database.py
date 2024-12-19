import sqlite3

def execute_query(query,args=(),fetchone=False,fetchall=False):
    with sqlite3.connect("library.db") as con:
        cursor=con.cursor()
        cursor.execute(query,args)
        con.commit()
        if fetchone:
            return cursor.fetchone()
        if fetchall:
            return cursor.fetchall()
    return None