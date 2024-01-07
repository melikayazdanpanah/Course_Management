import mysql.connector
from mysql.connector import Error

#create a connection

def connection(database_name):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="melika1380",
        database= f"{course_management}"
        )
    
    