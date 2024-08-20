########pip install mysql-connector-python


import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='52.206.97.24',
            port=3306,
            database='hoppr',
            user='uan_process',
            password='U@n@789'  
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Connected to MySQL Server version {db_info}")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM `uan_linking_process`;")
            record = cursor.fetchall()
            print(f"You're connected to database: {record}")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

create_connection()
