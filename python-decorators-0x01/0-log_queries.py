import sqlite3
import functools
from datetime import datetime

#### decorator to lof SQL queries

""" YOUR CODE GOES HERE"""
def log_queries(func):
    def wrapper(*args,**kwargs):
        connect = func(*args,**kwargs)
        print(datetime.now(),result)
        
        return connect
    return wrapper
