import tkinter
from tkinter import * 
from tkinter import ttk
import tkinter as tk
import datetime
import subprocess
import sqlite3
import os
from tkinter.ttk import Combobox
from client_2 import run as run_client
from Encryption_Program_V2 import AsciiChange as run_encryption




def AdminContactCreation():
    
    conn = sqlite3.connect('contact.db')

    entered = []

    entered0 = ()
    entered1 = ()
    entered2 = ()
    entered3 = ()
    entered4 = ()


    root = Tk()


    root.title("Add User")
    root.geometry("800x500")


    def database():
        print(entered)
        EmpID = entered0
        Usrnme = entered1
        PssWrd = entered2
        UsrTpe = entered3
        Pos = entered4


        conn.execute("INSERT INTO Users VALUES (?,?,?,?,?)", (EmpID, Usrnme, PssWrd, UsrTpe, Pos))
        conn.commit()
        print ("Changes Committed");
        conn.close() 
            


    a = Entry(root)
    a.grid(row=0, column = 1, pady=20)
    entered0=(a.get())

    b = Entry(root)
    b.grid(row=0, column = 2, pady=20)
    entered1=(b.get())

    c = Entry(root)
    c.grid(row=0, column = 3, pady=20)
    entered2=(c.get())

    d = Entry(root)
    d.grid(row=0, column = 4, pady=20)
    entered3=(d.get())

    e = Entry(root)
    e.grid(row=0, column = 5, pady=20)
    entered4=(e.get())







    finalise = Button(root, text = "Commit Changes", command = database)
    finalise.grid(row = 1, column = 3, pady = 20)


    infomation = Label(root, text="Employee ID:   Username:  Password:   Type of User:   Position")
    infomation.grid(row=2,column=0, pady=20)


    root.mainloop()

def AdministratorUserEditor():
    def __init__():
        conn = sqlite3.connect('contact.db')
    def deleteold(conn):
        EmpID = input("please enter the ID of the employee to be delted")
        conn.execute("DELETE FROM Users WHERE EmployeID = ?",(EmpID))
        conn.commit()
        conn.close()
        print("completed")
    def createnew(conn):
        EmplID = input("please enter employee ID")
        if EmplID != (0):
            Usrnme =  input("please enter user name")
            if input !=0:
                PssWrd = input("please enter password")
                if PssWrd != (0):
                    UsrTpe = input("please enter user type") 
                    if UsrTpe != (0):
                        Pos = input("please enter compny position")
                        if input != (0):

                                conn.execute("INSERT INTO Users VALUES (?,?,?,?,?)", (EmplID, Usrnme, PssWrd, UsrTpe, Pos))
                                conn.commit()
                                print ("complete");
                                conn.close() 
                        else:
                            print("error")
                    else:
                        print("error")
                
                            




    


    decision = input("do you want to create new account or delete an old account?")

    if decision == ("create"):
        createnew()
    elif decision == ("delete"):
        deleteold()



    userinput = ""
    passinput = ""
    usertrue = 0 
    passtrue = 0 
    admintrue = 0 
    root = Tk()

    canvas = tk.Canvas()
    canvas.pack(side = tk.LEFT, fill = tk.BOTH, expand=1 )



    def fetch():
        global username, password
        username = username.get()
        password = password.get()
        userinput = username
        passinput = password
        admincheck = (("Admin",))
        my_file = ('/Users/jacoblewis/Library/CloudStorage/OneDrive-StJohnFisherCatholicAcademy/Documents/nea/contact.db')
        #conn = sqlite3.connect('contact.db')
        conn = sqlite3.connect(my_file)
        c = conn.cursor()
        print(userinput)
        rows = c.execute("SELECT Username FROM Users WHERE Username = ?",(userinput,))
        row = c.fetchall()
        print(row)
        row = row[0][0]
        print(type(row))
        #for row in rows:
        print("here")
        if row ==  userinput:
            usertrue = 1
            print("username correct")
        else:
            print("username incorrect")
            exit()
        rows = c.execute("SELECT Password FROM Users WHERE Username = ? AND Password = ?",(userinput, passinput,))
        row = c.fetchall()
        #rows = rows[0][0]
        print(row)
        print(type(row))
        passentry = str(row)
        pt1 = passentry.strip("[('")
        pt2 = pt1.strip(",'])")
        print(pt2)
        if pt2 ==  passinput:
            passtrue = 1
            print("password correct")
        else:
            print("password incorrect")
            exit()
        row = c.execute("SELECT UserName FROM Users WHERE UserType = ?",admincheck,)
        rows = c.fetchall()
        rows = rows[0][0]
        for row in rows:
            result = rows
            if rows == username :
                admintrue = 1
                ("administrator access granted")
            else:
                pass


    root.title("Logon")
    root.geometry("200x400")

    username = tk.StringVar()
    password = tk.StringVar()

    username.set("")
    password.set("")

    entry = tk.Entry(root,textvariable = username)
    canvas.create_window(100, 100, window=entry)

    entrybutton = tk.Button(root, text = "Login", command = fetch)
    entrybutton.place(x=100,y=300)

    entry2 = tk.Entry(root, textvariable=password)
    canvas.create_window(100, 200, window = entry2)

    root.mainloop()

    if usertrue == 1 and passtrue == 1:
        subprocess.run(["python","Contacts Window.py"])
        exit()
    elif admintrue == 1 and passtrue == 1:
        subprocess.run(["python","administrator contact creation service.py"])

def ContactsWindow():
    def newwindow():
        print(clicked.get())
        global destination_user
        destination_user = clicked.get()
        MessageWrite()
        #f = open("Selected_User.txt","w")
        #selection = ("('",clicked.get,"'))")
        #f.write(str(selection))
        #subprocess.run(["python","text input window.py"])
        exit()



    x=0
    contacts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
    conn = sqlite3.connect('contact.db')
    print("connected to SQLite")
    c = conn.cursor()
    row = c.execute("SELECT Username FROM Users WHERE Position = ?",(pos,))
    rows = c.fetchall()
    for row in rows:
        
        contacts[x] = row
        x=x+1
        print(row)
        print(contacts)

    root = Tk()
    root.title("Contact Selection")
    root.geometry("400x200")

    def show():
        label.config( text = clicked.get() )

    options = [
        contacts[0],
        contacts[1],
        contacts[2],
        contacts[3],
        contacts[4],
        contacts[5],
        contacts[6],
        contacts[7],
        contacts[8],
        contacts[9],
        contacts[10],
        contacts[11],
        contacts[12],
        contacts[13],
        contacts[14],
        
    ]

    clicked=StringVar()

    clicked.set( contacts[1] )

    drop = OptionMenu( root , clicked , *options )
    drop.pack()

    button = Button( root , text = "Compose Message", command = newwindow).pack()

    label = Label( root , text = " ")
    label.pack()


    root.mainloop()

def MessageWrite():
    root = Tk()


    root.title("New Message")
    root.geometry("400x250")

    canvas = tk.Canvas()
    canvas.pack(side = tk.LEFT, fill = tk.BOTH, expand=1 )

    entry = tk.Entry(root)
    canvas.create_window(100, 100, window=entry)




    def new_line(event):
        alert = Label(root, text = "new line created" + str(event.x) + " " + str(event.y))
        lencheck=(entry.get)
        n = len(str(lencheck))
        entry.insert(n+1,"\n")


    def openarchive(event):
        subprocess.run(["python","text viewer"])
        pass
        


    def proccessing(event):
        time = datetime.datetime.now()
        file = open(username,"_",destination_user,time)
        timestamp = ("<",time,">")
        finished = (timestamp, " User[",username,"]","\n")
        userentry = entry.get()
        message = ("\n",str(finished),"\n",str(userentry))
        print(message)
        file = open(username+"_"+destination_user+".txt","a")
        global filename 
        filename = (username+"_"+destination_user+".txt")
        file.writelines(message)
        file.close()
        run_encryption()
        run_client(filename)







    newlne = Button(root, text = "Press for new line")
    newlne.bind("<Button-1>", new_line)
    newlne.place(x= 200, y = 85)


    archive = Button(root, text=("Archived Messages"))
    archive.bind("<Button-1>", openarchive)
    archive.place(x=50, y= 200)

    Send = Button(root, text= ("Send message"))
    Send.bind("<Button-1>", proccessing)
    Send.place(x=200, y = 200)



    root.mainloop()

def MessageViewer():
    root = Tk()
    root.title('Message Viewer')

    main_frame = Frame(root)
    main_frame.pack(fill = BOTH, expand=1 )

    canvas = Canvas(main_frame)
    canvas.pack(side = LEFT, fill = BOTH, expand=1 )



    #create scroll bars
    horizon = ttk.Scrollbar(main_frame, orient=HORIZONTAL, command=canvas.xview)
    horizon.pack(side = RIGHT, fill=X)
    vertical = ttk.Scrollbar(main_frame, orient=VERTICAL, command = canvas.yview)
    vertical.pack(side = RIGHT, fill=Y)

    #configure canvas things you know how it is
    canvas.configure(xscrollcommand = horizon.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox("all")))
    canvas.configure(yscrollcommand=vertical.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox("all")))

    frame = Frame(canvas)

    canvas.create_window((0,0), window=frame, anchor="nw")


    file = open(username+"_"+destination_user+".txt","r")
    global filename
    filename = (username+"_"+destination_user+".txt")
    contents = file.read()
    file.close()

    canvas.create_text(1, 1, text=contents , anchor='nw', font='TkMenuFont', fill='black')

    root.mainloop()

def run():
    ContactsWindow()
        
