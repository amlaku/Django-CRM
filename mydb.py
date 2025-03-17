# Install MySQL on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql-connector-python

import mysql.connector

try:
    # Establish database connection
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="072119",  # Ensure this is correct
    )

    # Prepare a cursor object
    cursorObject = dataBase.cursor()

    # Create a database (if it doesn't exist)
    cursorObject.execute("CREATE DATABASE IF NOT EXISTS elderco")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close connection
    if 'dataBase' in locals() and dataBase.is_connected():
        cursorObject.close()
        dataBase.close()
        print("All Done!")
