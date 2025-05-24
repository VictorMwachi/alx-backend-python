import sqlite3
import functools
from datetime import datetime
"""
Create a decorator to log all SQL queries executed by a function.
Learn to intercept function calls to enhance observability.
"""

def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        query = kwargs.get('query') or args[0]
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if query:
            print(f"[{timestamp}] Executing query: {query}")
        else:
            print(f"[{timestamp}] No query to execute")
    
        connect = func(*args,**kwargs)
        return connect
    return wrapper