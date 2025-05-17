import mysql.connector
from mysql.connector import Error
import csv

def connect_db():
    connection = mysql.connector.connect(
    host = "localhost",
    user = "admin",
    password = "adminpassword"
    )
    return connection
def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    connection.commit()

def connect_to_prodev():
    return mysql.connector.connect(
        host="localhost",
        user="admin",
        password="adminpassword",
        database="ALX_prodev"
    )

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(255) UNIQUE,
            age INT
            )
        """)
    connection.commit()
def insert_data(connection, data):
    cursor = connection.cursor()
    with open(data,'r') as f:
        users = csv.DictReader(f)
        for row in users:
            cursor.execute("SELECT email FROM user_data WHERE email = %s",(row['email'],))
            if cursor.fetchone() is None:
                cursor.execute("""
                               INSERT INTO user_data (name, email, age) VALUES (%s, %s, %s)""",
                               (row['name'],row['email'],row['age']))
                connection.commit()
            else:
                print("user email already exists.")
if __name__ == '__main__':
    conn = connect_db()
    create_database(conn)
    conn.close()

    conn_prodev = connect_to_prodev()
    create_table(conn_prodev)
    insert_data(conn_prodev, "user_data.csv")
    conn_prodev.close()