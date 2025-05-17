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
    cursor.execute("SELECT * FROM user_data")
    for user in cursor.fetchall():
        yield {
            'user_id':user[0],
            'name':user[1],
            'email':user[2],
            'age':user[3]
            }
if __name__ == '__main__':
    from itertools import islice
    for user in islice(stream_users(), 6):
        print(user)