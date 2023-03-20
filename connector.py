#mysql.connector module used to connect to the database
import mysql.connector

def connectDb():
    #Connecting to the database
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='gpa',
                                            user='root',
                                            password='vksql')

        return connection
        
    #Except block in case an error occurs while connecting to the database
    except mysql.connector.Error as error:
        print("Failed to connect to the database {}".format(error))
        
        return None