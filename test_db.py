from app.db import get_db_connection

connection = get_db_connection()

if connection.is_connected():
    print("Successfully connected to MySQL!")

connection.close()