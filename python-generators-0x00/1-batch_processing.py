#!/usr/bin/python3
import mysql.connector


def stream_users_in_batches(batch_size):
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'admin',
        database = 'ALX_prodev',
        password = 'adminpassword',
        )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data")
    yield cursor.fetchmany(size=batch_size)


#def batch_processing(batch):
print(stream_users_in_batches(batch_size=50))