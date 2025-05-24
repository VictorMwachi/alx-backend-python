import sqlite3
import functools

"""
Automate database connection handling with a decorator.
Eliminate boilerplate code for opening and closing connections.
"""
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        conn = sqlite3.connect('users.db')
        try:
            result = func(conn,*args,**kwargs)
        finally:
            conn.close()
        return result
    return wrapper