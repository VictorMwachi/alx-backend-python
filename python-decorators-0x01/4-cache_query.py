import time
import sqlite3 
import functools

query_cache = {}
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

def cache_query(func):
    functools.wraps(func)
    def wrapper(*args,**kwargs):
        if args or kwargs:
            query = args[0] or kwargs.get('query')
        if query_cache.get(query,False):
            query_cache[query]=func(*args,**kwargs)
            result = func(*args,**kwargs)
        else:
            result = query_cache.get(query)
        return result
    return wrapper
