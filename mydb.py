# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer
# pip intall mysql

# pip install mysql-connector   this OR
# pip intall mysql-connector-python


import mysql.connector

# Establishing a connection now  
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'WhySQL@804',
)

# Prepare a cursor_object 
#            use:

cursorObject = dataBase.cursor()


# Create a database

cursorObject.execute("CREATE DATABASE IF NOT EXISTS 1st_mysql")

print("All Done!")  # To print a message on terminal