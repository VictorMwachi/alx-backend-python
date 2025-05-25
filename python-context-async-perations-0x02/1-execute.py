import sqlite3


class ExecuteQuery:
    def __init__(self, db_path, query, param):
        self.db_path = db_path
        self.query = query
        self.param = param
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query, (self.param,))
        return self.cursor.fetchall()

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    with ExecuteQuery('user.db', 'SELECT * FROM users WHERE age > ?', 25) as results:
        for row in results:
            print(row)