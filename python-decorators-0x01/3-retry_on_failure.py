import time
import sqlite3 
import functools

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

def retry_on_failure(func,retries=3, delay=2):
    @functools.wraps(func,retries=3, delay=2)
    def wrapper(*args,**kwargs):
        time.sleep(delay)
        time.
