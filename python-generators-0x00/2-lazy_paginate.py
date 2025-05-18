#!/usr/bin/python3
import mysql.connector

def paginate_users(page_size, offset=0):
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'admin',
        database = 'ALX_prodev',
        password = 'adminpassword'
        )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s",(page_size,offset))
    yield cursor.fetchall()


def lazy_paginate(page_size):
    for user in paginate_users(page_size, offset):
        print(*user)

lazy_paginate(50)