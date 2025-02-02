import mysql.connector # type: ignore
from mysql.connector import Error # type: ignore

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"
        )

        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        connection.database = 'alx_book_store'

        if connection.is_connected():
            print("Connected to the database 'alx_book_store' successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

connect_to_database()

