import sqlite3

class DatabaseConnection:
    def __init__(self,db='user.db'):
        self.db = db
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db)
        return self.conn
    
    def __exit__(self,type,value,traceback):
        if self.conn:
            self.conn.close()

with DatabaseConnection as db_conn:
    cursor = db_conn.cursor()
    cursor.execute('SELECT * FROM users')