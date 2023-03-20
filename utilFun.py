from connector import *
from GPA import posImgID
from verify import *

class utilFun:
    #Initializing necessary object variables to keep track of the program
    def __init__(self):
        self.passw = ""
        self.track = []
        self.count = 0

    #To store the sequence selected by the user
    def getImgId(self,t):
        if (t not in self.track):
            print(posImgID[t])
            self.passw += str(posImgID[t])
            self.track.append(t)
        else:
            print("You have " + str(2-self.count) + " tries left")
            res = self.clear(1)
            
        # return posImgID[t]

    def getImgIdReg(self,t):
        if (t not in self.track):
            print(posImgID[t])
            self.passw += str(posImgID[t])
            self.track.append(t)
        else:
            print("Cleared Try Again")
            res = self.clear(1)

    #To clear everything and start selecting the images from beginning
    def clear(self, state):
        self.passw = ""
        self.track = []
        if state:
            self.count += 1
        if self.count == 3:
            print("Out of tries")
            return True
        return False

    def insertDetails(self,email,name,username,password,date):
        connection = connectDb()

        if connection:
            cursor = connection.cursor()
            insert_details_query = '''insert into users(Name, username, email, password, AccRegDate) values (%s, %s, %s, %s, %s);'''
            insert_details_tuple = (name, username, email, password, str(date))
            result = cursor.execute(insert_details_query, insert_details_tuple)
            connection.commit()

        if connection.is_connected():
            cursor.close()
            connection.close()

        return result