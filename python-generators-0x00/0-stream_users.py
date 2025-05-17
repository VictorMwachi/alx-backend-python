#!/usr/bin/python3
import mysql.connector
def stream_users():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "admin",
        database = 'ALX_prodev',
        password = "adminpassword"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data LIMIT 10")
    yield cursor.fetchone()