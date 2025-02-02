import mysql.connector # type: ignore
from mysql.connector import Error # type: ignore

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="samuel@2005",
            database="alx_book_store"
        )

        if connection.is_connected():
            print("Connected to the database 'alx_book_store' successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

connect_to_database()
