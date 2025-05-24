import sqlite3
import functools
import datetime

#### decorator to lof SQL queries

""" YOUR CODE GOES HERE"""
def log_queries(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        print(result)
        return result
    return wrapper
