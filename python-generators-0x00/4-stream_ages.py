#!/usr/bin/python3
import mysql.connector


def stream_user_ages():
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'admin',
        database = 'ALX_prodev',
        password = 'adminpassword'
        )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")
    for row in cursor:
        yield row['age']


def average_stream_user_age():
    total_age,count=0,0
    for age in stream_user_ages():
        total_age+=age
        count+=1
        if count !=0:
            average_age=total_age/count
        else:
            print("No users to calculate average age.")
    print(f"Average age of users: {average_age}")
average_stream_user_age()
