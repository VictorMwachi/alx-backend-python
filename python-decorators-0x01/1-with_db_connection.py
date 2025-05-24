import sqlite3
import functools

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        conn = sqlite3.connect('users.db')
        result = func(*args,**kwargs)
        conn.close()
        return result
    return wrapper