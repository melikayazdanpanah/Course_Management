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
    
    return connection


#create close def 

def close_connection(connection):
    try:
        connection.close()
    except Error as e :
        print(f"the error '{e}' not close ")


    connection.commit()
#def for creating database 

def create_database(database_name):
    connection = mysql.connector.connect(
        host="localhost",
        user = "root",
        password = "melika1380",
    )
    sql = f"create database {database_name}"

    try_execute(connection=connection,sql_query=sql)
    close_connection(connection)



    )

           
    