import sqlite3 
import functools


"""
Implement a decorator to manage database transactions (commit/rollback).
Ensure robust error handling and data consistency.
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

def transaction(func):
    @functools.wraps(func)
    def wrapper(conn,*args,**kwargs):
        try:
            result = func(conn,*args,**kwargs)
            conn.commit()
            return result
        except sqlite3.Error as e:
            conn.rollback()
            print(f"❌ SQL error: {e}")
            return None
    return wrapper
