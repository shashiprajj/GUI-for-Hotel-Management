from tkinter import *
from tkinter import messagebox
import io
import os
from index import Encrypt
import sqlite3
import StudentDatabase_backEnd

conn=sqlite3.connect("data.sqlite")
cur=conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS "AUTHORIZED_DATA" (
	"id"	INTEGER NOT NULL ,
	"name"	TEXT NOT NULL UNIQUE,
	"password"	TEXT NOT NULL,
	"contact_number"	INTEGER NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);''')


def validate(hashed_password,row):
    print(hashed_password,row)
    if hashed_password == row:
        sign_up_window.destroy()

        class Student:
            def __init__(self, root):
                self.root = root
                self.root.title("Student Database Management System")
                self.root.geometry("1350x7500+0+0")
                self.root.config(bg = "#074463")

                StdID = StringVar()
                Firstname = StringVar()
                Surname = StringVar()
                DoB = StringVar()
                Age = StringVar()
                Gender = StringVar()
                Address = StringVar()
                Mobile = StringVar()

                # ============================================ FUNCTION DECLARATION ==============================================================

                def iExit():
                    iExit = messagebox.askyesno("Students Database Management System","Confirm if you want to exit")
                    if iExit > 0:
                        root.destroy()
                        return


                def clearData():
                    self.txtStdID.delete(0, END)
                    self.txtfna.delete(0, END)
                    self.txtsna.delete(0, END)
                    self.txtDoB.delete(0, END)
                    self.txtAge.delete(0, END)
                    self.txtGender.delete(0, END)
                    self.txtAdr.delete(0, END)
                    self.txtMobile.delete(0, END)


                def addData():
                    if(len(StdID.get()) != 0):
                        StudentDatabase_backEnd.addStdRec(StdID.get(), Firstname.get(), Surname.get(), DoB.get() ,Age.get() ,Gender.get() , \
                                    Address.get(),Mobile.get())
                        studentList.delete(0, END)
                        studentList.insert(END, ("             "+str(StdID.get())+"      "+Firstname.get()+" "+Surname.get()+"          "+DoB.get()+"         "+Age.get()+"        "+Gender.get() +"          "+ \
                                    Address.get()+"         "+Mobile.get()))


                def DisplayData():
                    studentList.delete(0, END)
                    for rows in StudentDatabase_backEnd.viewData():
                        studentList.insert(END, ( str(rows[0])+"      "+str(rows[1])+"         "+rows[2]+" "+rows[3]+"          "+rows[4]+"         "+rows[5]+"        "+rows[6]+"          "+rows[7]+"         "+rows[8] ), str(""))

                def StudentRec(event):
                    global sd

                    searchStd = studentList.curselection()[0]
                    sd = studentList.get(searchStd)

                    self.txtStdID.delete(0, END)
                    self.txtStdID.insert(END, sd[1])
                    self.txtfna.delete(0, END)
                    self.txtfna.insert(END, sd[2])
                    self.txtsna.delete(0, END)
                    self.txtsna.insert(END, sd[3])
                    self.txtDoB.delete(0, END)
                    self.txtDoB.insert(END, sd[4])
                    self.txtAge.delete(0, END)
                    self.txtAge.insert(END, sd[5])
                    self.txtGender.delete(0, END)
                    self.txtGender.insert(END, sd[6])
                    self.txtAdr.delete(0, END)
                    self.txtAdr.insert(END, sd[7])
                    self.txtMobile.delete(0, END)
                    self.txtMobile.insert(END, sd[8])



                def delete_data(ent1):
                    StudentDatabase_backEnd.deleteRec(ent1)


                def DeleteData():
                    Delete_window = Tk()
                    Delete_window.title('Delete Data')
                    Delete_window.geometry("500x700")
                    Delete_window.configure(bg = "cadet blue")
                    Delete_window.state('zoomed')

                    Lab1 = Label(Delete_window,text ="Ganesh Hotel",font = "Times 35 bold",relief =GROOVE, bd=8,width=100,height=2,bg="#074463",fg="White")
                    Lab1.place(x=-700,y=0)

                    delete = Label(Delete_window,text ="Delete(By ID)",bg = "#074463", fg = "White",font = "Times 25 bold",relief =GROOVE,bd=8,height=1,width=18,pady=5,padx=5)
                    delete.place(x=500,y=200)

                    delete_label = Label(Delete_window,text="Enter ID of Staff",font = "Times 15 bold",relief = GROOVE, bd=8,width=20,height=2,bg="Black",fg="White",padx=5,pady=5)
                    delete_label.place(x=300,y=300)

                    ent1=Entry(Delete_window, font = "Times 20 bold",relief =GROOVE, bd=8)
                    ent1.place(x= 700, y= 300,width=250,height=60)
                    btn = Button(Delete_window,text='delete', font = "Times 20 bold",relief =GROOVE,bg="red", bd=8,command=lambda:delete_data(ent1.get()))
                    btn.place(x=500, y = 400, width=250,height=60)


                def searchDatabase():
                    studentList.delete(0, END)
                    for rows in StudentDatabase_backEnd.searchData(StdID.get(), Firstname.get(), Surname.get(), DoB.get() ,Age.get() ,Gender.get() , \
                                    Address.get(),Mobile.get()):
                        studentList.insert(END, ( str(rows[0])+"      "+str(rows[1])+"         "+rows[2]+" "+rows[3]+"          "+rows[4]+"         "+rows[5]+"        "+rows[6]+"          "+rows[7]+"         "+rows[8] ), str(""))





                # ============================================ FRAMES ==============================================================
                MainFrame = Frame(self.root, bg = "#074463")
                MainFrame.grid()

                TitFrame = Frame(MainFrame,bd = 8, padx = 54, pady = 8, bg = "#074463", relief = GROOVE)
                TitFrame.pack(side = TOP)

                self.lblTit = Label(TitFrame, font = "arial 47 bold", text = "Manager's Database Management Systems", bg = "#074463")
                self.lblTit.grid()

                ButtonFrame = Frame(MainFrame,bd = 8,width = 1350, height = 70, padx = 18, pady = 10, bg = "#074463", relief = GROOVE)
                ButtonFrame.pack(side = BOTTOM)

                DataFrame = Frame(MainFrame,bd = 8,width = 1400, height = 400, padx = 20, pady =20, bg = "#074463", relief = GROOVE)
                DataFrame.pack(side = BOTTOM)

                DataFrameLEFT = LabelFrame(DataFrame,bd = 8,width = 700, height = 600, padx = 20, bg = "#074463",fg="gold", relief = GROOVE
                                                    , font = "arial 20 bold", text = "Staff Info\n")
                DataFrameLEFT.pack(side = LEFT)

                DataFrameRIGHT = LabelFrame(DataFrame,bd = 8,width = 1250, height = 200, padx = 31, pady = 3, bg = "#074463",fg="gold", relief = GROOVE
                                                     , font = "arial 20 bold", text = "Staff's Details\n")
                DataFrameRIGHT.pack(side = RIGHT)

                # ============================================ LABELS AND ENTRY WIDGET ==============================================================

                self.lblStdID = Label(DataFrameLEFT, font = "arial 20 bold", text = "Staff's ID", bg = "#074463", padx = 2, pady = 2)
                self.lblStdID.grid(row = 0, column = 0, sticky = W)
                self.txtStdID = Entry(DataFrameLEFT, font = "arial 20 bold", textvariable = StdID, width = 20)
                self.txtStdID.grid(row = 0, column = 1)

                self.lblfna = Label(DataFrameLEFT, font = "arial 20 bold", text = "First Name", bg = "#074463", padx = 2, pady = 2)
                self.lblfna.grid(row = 1, column = 0, sticky = W)
                self.txtfna = Entry(DataFrameLEFT, font = "arial 20 bold", textvariable = Firstname, width = 20)
                self.txtfna.grid(row = 1, column = 1)

                self.lblsna = Label(DataFrameLEFT, font = "arial 20 bold", text = "Last Name", bg = "#074463", padx = 2, pady = 2)
                self.lblsna.grid(row = 2, column = 0, sticky = W)
                self.txtsna = Entry(DataFrameLEFT, font = "arial 20 bold", textvariable = Surname, width = 20)
                self.txtsna.grid(row = 2, column = 1)

                self.lblDoB = Label(DataFrameLEFT, font = "arial 20 bold", text = "Salary", bg = "#074463", padx = 2, pady = 2)
                self.lblDoB.grid(row = 3, column = 0, sticky = W)
                self.txtDoB = Entry(DataFrameLEFT, font = "arial 20 bold", textvariable = DoB, width = 20)
                self.txtDoB.grid(row = 3, column = 1)

                self.lblAge = Label(DataFrameLEFT, font = "arial 20 bold", text = "Age", bg = "#074463", padx = 2, pady = 2)
                self.lblAge.grid(row = 4, column = 0, sticky = W)
                self.txtAge = Entry(DataFrameLEFT, font = "arial 20 bold", textvariable = Age, width = 20)
                self.txtAge.grid(row = 4, column = 1)

                self.lblGender = Label(DataFrameLEFT, font = "arial 20 bold", text = "Gender", bg = "#074463", padx = 2, pady = 2)
                self.lblGender.grid(row = 5, column = 0, sticky = W)
                self.txtGender = Entry(DataFrameLEFT, font = "arial 20 bold", textvariable = Gender, width = 20)
                self.txtGender.grid(row = 5, column = 1)

                self.lblAdr = Label(DataFrameLEFT, font = "arial 20 bold", text = "Address", bg = "#074463", padx = 2, pady = 2)
                self.lblAdr.grid(row = 6, column = 0, sticky = W)
                self.txtAdr = Entry(DataFrameLEFT, font = "arial 20 bold", textvariable = Address, width = 20)
                self.txtAdr.grid(row = 6, column = 1)

                self.lblMobile = Label(DataFrameLEFT, font = "arial 20 bold", text = "Mobile", bg = "#074463", padx = 2, pady = 2)
                self.lblMobile.grid(row = 7, column = 0, sticky = W)
                self.txtMobile  = Entry(DataFrameLEFT, font = "arial 20 bold", textvariable = Mobile , width = 20)
                self.txtMobile.grid(row = 7, column = 1)


                # ============================================ LISTBAR AND SCROLLBAR WIDGET ========================================================

                scrollbar = Scrollbar(DataFrameRIGHT)
                scrollbar.grid(row = 0, column = 1, sticky = 'ns')

                label = Label(DataFrameRIGHT, text= "id       Staff-ID          Name                    Salary     Age   Gender     Adddress            Mobile No ",
                         font = "arial 12 bold",)
                label.grid(row=0, column=0)

                studentList = Listbox(DataFrameRIGHT, width = 72, height = 14, font = "arial 12 bold", yscrollcommand = scrollbar.set)
                studentList.bind('<<Listboxselect>>',StudentRec)
                studentList.grid(row = 1, column = 0, padx = 8)
                scrollbar.config(command = studentList.yview)


                # ============================================ BUTTON WIDGET ==============================================================

                self.btnAddData = Button(ButtonFrame, text = "Add New",bg="cadet blue", font = "Arial 20 bold", height = 1, width = 10, bd = 6, relief = GROOVE, command = addData)
                self.btnAddData.grid(row = 0, column = 0)

                self.btnDisplayData = Button(ButtonFrame, text = "Display All",bg="cadet blue", font = "Arial 20 bold", height = 1, width = 11, bd = 6, relief = GROOVE, command = DisplayData)
                self.btnDisplayData.grid(row = 0, column = 1)

                self.btnClearData = Button(ButtonFrame, text = "Clear",bg="cadet blue", font = "Arial 20 bold", height = 1, width = 10, bd = 6, relief = GROOVE, command = clearData)
                self.btnClearData.grid(row = 0, column = 2)

                self.btnDeleteData = Button(ButtonFrame, text = "Delete",bg="cadet blue", font = "Arial 20 bold", height = 1, width = 10, bd = 6, relief = GROOVE, command = DeleteData)
                self.btnDeleteData.grid(row = 0, column = 3)

                self.btnSearchData = Button(ButtonFrame, text = "Search(Staff-ID)",bg="cadet blue", font = "Arial 20 bold", height = 1, width = 13, bd = 6, relief = GROOVE, command = searchDatabase)
                self.btnSearchData.grid(row = 0, column = 4)

                self.btnExitData = Button(ButtonFrame, text = "Exit",bg="cadet blue", font = "Arial 20 bold", height = 1, width = 10, bd = 6, relief = GROOVE, command= iExit)
                self.btnExitData.grid(row = 0, column = 5)



        if __name__ == '__main__':
            root = Tk()
            application = Student(root)
            root.mainloop()

    else:
        messagebox.showwarning("showwarning", "INVALID USERNAME OR PASSWORD") 

def register_info(entry1,entry2,entry3,contact_entry):
    try:
        name=(entry1.get())
        password=(entry2.get())
        retype_passwowrd = (entry3.get())
        contact_number = (contact_entry.get())
        if password == retype_passwowrd:

        #ENCRYPTING THE PASSWORD
            Hash = Encrypt(password)
            hashed_password = Hash.hash()

            cur.execute('''INSERT INTO
                        AUTHORIZED_DATA(name,password,contact_number)
                        VALUES(?,?,?)''',
                        (name,hashed_password,contact_number))
            conn.commit()
            main()
        else:
            messagebox.showwarning("showwarning", "PASSWORD DOES NOT MATCH")

    except:
        messagebox.showwarning("showwarning", "USERNAME ALREADY EXISTS")

    

def login_info(password_entry,username_entry):
    password = password_entry.get()
    username = username_entry.get()
    Hash = Encrypt(password)
    hashed_password = Hash.hash()
    rows = cur.execute('SELECT name,password FROM AUTHORIZED_DATA WHERE name = ?  ',(username,))

    for row in rows:
        password = row[1]

    validate(hashed_password,password)
    
def forgot_info(entry1,entry2,entry3):
    Hash = Encrypt(entry3.get())
    hashed_password = Hash.hash()
    try:
        cur.execute('''UPDATE AUTHORIZED_DATA SET password=?
                    WHERE name=? ''',(hashed_password,entry1.get()))
        conn.commit()
    except Exception as e:
        print(e)
        forgot_password_window.destroy()

def forget_maintain():
    sign_up_window.destroy()
    forgot_password_window = Tk()

    forgot_password_window.geometry("500x700")
    forgot_password_window.title("Change your password here!")
    forgot_password_window.configure(bg = "cadet blue")
    forgot_password_window.state('zoomed')

    Lab1 = Label(forgot_password_window,text ="CHANGE PASSWORD",font = "Times 35 bold",relief =GROOVE, bd=8,width=100,height=2,bg="#074463",fg="White")
    Lab1.place(x=-700,y=0)

    Label1  = Label(forgot_password_window,text = "Username", bg = "Black", fg = "White",font = "Times 15 bold",relief =GROOVE, bd=8,height=2,width=20,pady=5,padx=5)
    Label1.place(x=400,y=250)

    Label2  = Label(forgot_password_window,text = "Contact", bg = "Black", fg = "White",font = "Times 15 bold",relief =GROOVE, bd=8,height=2,width=20,pady=5,padx=5)
    Label2.place(x=400,y=350)

    Label3  = Label(forgot_password_window,text = "Change Password", bg = "Black", fg = "White",font = "Times 15 bold",relief =GROOVE, bd=8,height=2,width=20,pady=5,padx=5)
    Label3.place(x=400,y=450)

    entry1 = Entry(forgot_password_window,bg = "white",fg="Black",font = "Times 15 bold", relief =GROOVE, bd=8)
    entry1.place(x=700,y=250,width=250,height=60)

    entry2 = Entry(forgot_password_window,bg = "white",fg= "Black",font = "Times 15 bold",show = "*", relief =GROOVE, bd=8)
    entry2.place(x=700,y=350,width=250,height=60)

    entry3 = Entry(forgot_password_window,bg = "white",fg= "Black",font = "Times 15 bold",show = "*", relief =GROOVE, bd=8)
    entry3.place(x=700,y=450,width=250,height=60)

    button1 = Button(forgot_password_window,text = "Log-in again",bg = "#074463",width = 15,height = 1,padx = 5,pady = 5,fg = "White",font = "Times 20 bold",relief =GROOVE, bd=8,activebackground = "gold",command = lambda:forgot_info(entry1,entry2,entry3))
    button1.place(x=570,y=550)

    forgot_password_window.mainloop()

def register():
    global root
    sign_up_window.destroy()
    root = Tk()

    root.geometry("500x700")
    root.title("Sign Up here!")
    root.configure(bg = "cadet blue")
    root.state('zoomed')

    global verify_username
    global verify_password
    global img1
    verify_username = StringVar()
    verify_password = StringVar()
    verify_password_again = StringVar()

    Lab1 = Label(root,text ="Ganesh Hotel",font = "Times 35 bold",relief =GROOVE, bd=8,width=100,height=2,bg="#074463",fg="White")
    Lab1.place(x=-700,y=0)

    login = Label(root,text ="Register Now",bg = "#074463", fg = "White",font = "Times 25 bold",relief =GROOVE,bd=8,height=1,width=18,pady=5,padx=5)
    login.place(x=500,y=150)

    Label1  = Label(root,text = "Username", bg = "Black", fg = "White",font = "Times 15 bold",relief =GROOVE, bd=8,height=2,width=20,pady=5,padx=5)
    Label1.place(x=400,y=250)

    Label2  = Label(root,text = "Password", bg = "Black", fg = "White",font = "Times 15 bold",relief =GROOVE, bd=8,height=2,width=20,pady=5,padx=5)
    Label2.place(x=400,y=350)

    Label3  = Label(root,text = "Re-type Password", bg = "Black", fg = "White",font = "Times 15 bold",relief =GROOVE, bd=8,height=2,width=20,pady=5,padx=5)
    Label3.place(x=400,y=450)

    contact_label = Label(root,text="contact number",width=20,height=2,font = "Times 15 bold",relief =GROOVE, bd=8,bg="Black",fg="White",padx=5,pady=5)
    contact_label.place(x=400,y=545)


    entry1 = Entry(root,bg = "white",fg="Black",font = "Times 15 bold",textvariable = verify_username, relief =GROOVE, bd=8)
    entry1.place(x=700,y=250,width=250,height=60)

    entry2 = Entry(root,bg = "white",fg= "Black",font = "Times 15 bold",textvariable = verify_password,show = "*", relief =GROOVE, bd=8)
    entry2.place(x=700,y=350,width=250,height=60)

    entry3 = Entry(root,bg = "white",fg= "Black",font = "Times 15 bold",textvariable = verify_password_again,show = "*", relief =GROOVE, bd=8)
    entry3.place(x=700,y=450,width=250,height=60)

    contact_entry = Entry(root,fg="Black",bg="white",font = "Times 20 bold",textvariable = contact1, relief =GROOVE, bd=8)
    contact_entry.place(x=700,y=550,width=250,height=60)

    button1 = Button(root,text = "Register",bg = "#074463",width = 15,height = 1,padx = 5,pady = 5,fg = "White",font = "Times 20 bold",relief =GROOVE, bd=8,activebackground = "gold",command = lambda:register_info(entry1,entry2,entry3,contact_entry))
    button1.place(x=570,y=620)

    root.mainloop()

def function():
    try:
        root.destroy()
    except:
        pass

def main():
    function()
    global sign_up_window
    global username1
    global password1
    global contact1
    sign_up_window = Tk()
    sign_up_window.geometry("500x700")
    sign_up_window.title("Sign_Up_Window")
    sign_up_window.configure(bg = "cadet blue")
    sign_up_window.state('zoomed')



    username1 = StringVar()
    password1 = StringVar()
    contact1 = StringVar()

    Lab1 = Label(sign_up_window,text ="Ganesh Hotel",font = "Times 35 bold",relief =GROOVE, bd=8,width=100,height=2,bg="#074463",fg="White")
    Lab1.place(x=-700,y=0)

    login = Label(sign_up_window,text ="Login Now",bg = "#074463", fg = "White",font = "Times 25 bold",relief =GROOVE,bd=8,height=1,width=18,pady=5,padx=5)
    login.place(x=500,y=200)

    username_label = Label(sign_up_window,text="Enter Username",font = "Times 20 bold",relief = GROOVE, bd=8,width=20,height=2,bg="Black",fg="White",padx=5,pady=5)
    username_label.place(x=300,y=300)

    password_label = Label(sign_up_window,text="Enter password",width=20,height=2,font = "Times 20 bold",relief = GROOVE, bd=8,bg="Black",fg="White",padx=5,pady=5)
    password_label.place(x=300,y=400)

    username_entry = Entry(sign_up_window,fg="black",bg="white",font = "Times 20 bold",relief = GROOVE, bd=8,textvariable = username1)
    username_entry.place(x=700,y=300,width=400,height=70)

    password_entry = Entry(sign_up_window,fg="black",bg="white",font = "Times 20 bold",relief = GROOVE, bd=8,textvariable = password1,show = "*")
    password_entry.place(x=700,y=400,width=400,height=70)

    sign_up_Button = Button(sign_up_window,text = "SIGN UP", bg = "#074463", fg = "White",font = "Times 20 bold",relief =GROOVE,bd=8,height=1,width=15,pady=5,padx=5,activebackground = "gold" ,command=lambda :login_info(password_entry,username_entry))
    sign_up_Button.place(x=500,y=520)


    register_Button = Button(sign_up_window,text = "New user?? Register", bg = "#074463", fg = "White",font = "Times 20 bold",relief =GROOVE,bd=8,height=1,width=15,pady=5,padx=5,activebackground = "gold", command = register)
    register_Button.place(x=500,y=600)

    forget_button = Button(sign_up_window,text = "forgot password?", bg = "#074463", fg = "White",font = "Times 20 bold",relief =GROOVE,bd=8,height=1,width=14,pady=5,padx=5,activebackground = "gold", command = forget_maintain)
    forget_button.place(x=1110,y=400)
    sign_up_window.mainloop()

if __name__ == '__main__':
    main()