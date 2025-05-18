#!/usr/bin/python3
import mysql.connector


def stream_users_in_batches(batch_size):
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'admin',
        database = 'ALX_prodev',
        password = 'adminpassword'
        )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data LIMIT %s",(batch_size,))
    yield cursor.fetchall()
    


def batch_processing(batch_size):
    filtered_users = [user for user in stream_users_in_batches(batch_size) if user['age']>25]
    yield filtered_users