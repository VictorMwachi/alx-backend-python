import sqlite3
class ExecuteQuery:
    def __init__(self, query, param):
        self.query = query
        self.param = param

    def __enter__(self):
        self.conn = sqlite3.connect(self.db)
        self.cursor = db_conn.cursor()
        self.cursor.execute(self.query,(self.param,))
        return self.cursor.fetchall()

    def __exit__(self,type,value,traceback):
        if self.conn:
            self.conn.close()
