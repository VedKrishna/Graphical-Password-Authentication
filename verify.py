from connector import *

def checkCredentials(email, passw):
    #Connecting to database
    connection = connectDb()

    if connection:
        cursor = connection.cursor()
        get_email_query = '''select password from users where email = %s'''
        get_email_tuple = (email, )

        cursor.execute(get_email_query, get_email_tuple)
        result = cursor.fetchall()
        
        #Checking whether the password is correct
        if passw == result[0][0]:
            return True
        else:
            return False

#To check whether the email entered is correct
def verifyEmail(email):
    connection = connectDb()

    if connection:
        cursor = connection.cursor()
        get_email_query = '''select userid from users where email = %s'''
        get_email_tuple = (email, )

        cursor.execute(get_email_query, get_email_tuple)
        result = cursor.fetchall()

        try:
            result[0][0]
            return True
        except IndexError:
            return False

if __name__ == "__main__":
    print(checkCredentials("pvedkrishna@gmail.com", "312"))