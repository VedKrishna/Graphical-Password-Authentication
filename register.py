from tkinter import *
from datetime import *
from utilFun import *
from PIL import ImageTk, Image;

temp = utilFun()

class verFuns:
    def __init__(self):
        self.email = None
        self.name = None
        self.username = None
        self.date = date.today()

    #Checking whether the password is correct or wrong
    def submitAct(self):
        self.email = root.email.get()
        self.name = root.Name.get()
        self.username = root.username.get()
        res = temp.insertDetails(self.email, self.name, self.username, temp.passw, self.date)

        print("Created!!")
        root.destroy()

    def getdetails(self):
        self.email = root.email.get()
        self.name = root.Name.get()
        self.username = root.username.get()

temp2 = verFuns()

#Creating a toplevel window which displays all the images for the user to select from after email is verified
class Window(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        #Creating a submit button once user is done selecting the images
        submitButton = Button(self, text = "Submit",command = temp2.submitAct)
        submitButton.grid(row=4, column=3, )

        #Clear button for user to select
        clearButton = Button(self, text = "Clear", command = lambda: temp.clear(0))
        clearButton.grid(row = 4, column = 1)

        #Displaying all the images as buttons
        img1 = ImageTk.PhotoImage(Image.open(r"C:\Users\pvedk\Desktop\programming\miniProject_Sem_III\dispImages\temp.png"))
        img_button1 = Button(self, image=img1, command = lambda: temp.getImgIdReg(1))
        img_button1.image = img1
        img_button1.grid(row=1,column=1,pady=20,padx=20)

        img2 = ImageTk.PhotoImage(Image.open(r"C:\Users\pvedk\Desktop\programming\miniProject_Sem_III\dispImages\temp2.png"))
        img_button2 = Button(self, image=img2, command = lambda: temp.getImgIdReg(2))
        img_button2.image = img2
        img_button2.grid(row=1,column=2,pady=20,padx=20)

        img3 = ImageTk.PhotoImage(Image.open(r"C:\Users\pvedk\Desktop\programming\miniProject_Sem_III\dispImages\temp3.png"))
        img_button3 = Button(self, image=img3, command = lambda: temp.getImgIdReg(3))
        img_button3.image = img3
        img_button3.grid(row=1,column=3,pady=20,padx=20)

        img4 = ImageTk.PhotoImage(Image.open(r"C:\Users\pvedk\Desktop\programming\miniProject_Sem_III\dispImages\temp4.png"))
        img_button4 = Button(self, image=img4, command = lambda: temp.getImgIdReg(4))
        img_button4.image = img4
        img_button4.grid(row=2,column=1,pady=20,padx=20)

        img5 = ImageTk.PhotoImage(Image.open(r"C:\Users\pvedk\Desktop\programming\miniProject_Sem_III\dispImages\temp5.png"))
        img_button5 = Button(self, image=img5, command = lambda: temp.getImgIdReg(5))
        img_button5.image = img5
        img_button5.grid(row=2,column=2,pady=20,padx=20)

        img6 = ImageTk.PhotoImage(Image.open(r"C:\Users\pvedk\Desktop\programming\miniProject_Sem_III\dispImages\temp6.png"))
        img_button6 = Button(self, image=img6, command = lambda: temp.getImgIdReg(6))
        img_button6.image = img6
        img_button6.grid(row=2,column=3,pady=20,padx=20)

        img7 = ImageTk.PhotoImage(Image.open(r"C:\Users\pvedk\Desktop\programming\miniProject_Sem_III\dispImages\temp7.png"))
        img_button7 = Button(self, image=img7, command = lambda: temp.getImgIdReg(7))
        img_button7.image = img7
        img_button7.grid(row=3,column=1,pady=20,padx=20)

        img8 = ImageTk.PhotoImage(Image.open(r"C:\Users\pvedk\Desktop\programming\miniProject_Sem_III\dispImages\temp8.png"))
        img_button8 = Button(self, image=img8, command = lambda: temp.getImgIdReg(8))
        img_button8.image = img8
        img_button8.grid(row=3,column=2,pady=20,padx=20)

        img9 = ImageTk.PhotoImage(Image.open(r"C:\Users\pvedk\Desktop\programming\miniProject_Sem_III\dispImages\temp9.png"))
        img_button9 = Button(self, image=img9, command = lambda: temp.getImgIdReg(9))
        img_button9.image = img9
        img_button9.grid(row=3,column=3,pady=20,padx=20)

#Main window where user needs to enter email to verify
class Main(Tk):
    def __init__(self):
        super().__init__()

        namemsg = Label(self, text="Name: ")
        namemsg.grid(row=1, column=1)

        self.Name = Entry(self)
        self.Name.grid(row=1, column=2)

        usernamemsg = Label(self, text = "Username: ")
        usernamemsg.grid(row=2, column=1)

        self.username = Entry(self)
        self.username.grid(row=2, column=2)

        emailmsg = Label(self, text="Email: ")
        emailmsg.grid(row=3, column=1)

        self.email = Entry(self)
        self.email.grid(row=3, column=2)

        submitDetails = Button(self, text="Submit", command=self.open_window)
        submitDetails.grid(row=4, column=2)

    #Function called to open the window with images once the email is verified
    def open_window(self):
        window = Window(self)

if __name__ == "__main__":
    root = Main()
    root.geometry("200x150")
    root.eval('tk::PlaceWindow . center')
    root.mainloop()