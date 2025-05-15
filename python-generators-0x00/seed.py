import mysql.connector
from mysql.connector import Error

def connect_db():
    try:
        connection = mysql.connector.connect(
        host = "localhost",
        user = "admin",
        database = "ALX_prodev",
        password = "adminpassword"
        )        
        if connection.is_connected():
            print("Connected to MySQL database")
        return connection
    except Error as e:
        print(f"e")
def connect_to_prodev():
    pass
def create_database():
    pass
def create_table(connection):
    pass
def insert_data(connection, data):
    pass
if __name__ == '__main__':
    connect_db()