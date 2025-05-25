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

def retry_on_failure(retries=3, delay=2):
    def decorator_retry(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for count in range(retries):
                try:
                    result = func(*args,**kwargs)
                    return result
                except sqlite3.Error as e:
                    print(f"Operation failed with err: {e}")
                    if(count==retries-1):
                        print(f"Timeout!! Maximum retries reached")
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator_retry
