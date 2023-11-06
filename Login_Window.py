import tkinter as tk
from tkinter import ttk
from tkinter import *
import subprocess
import sqlite3
from SQL_Commands import *





def fetch():
    global username, password, userinput, passinput
    username = username.get()
    password = password.get()
    userinput = username
    passinput = password
    admincheck = (("Admin",))
    my_file = ('/Users/jacoblewis/Library/CloudStorage/OneDrive-StJohnFisherCatholicAcademy/Documents/nea/contact.db')
    conn = sqlite3.connect(my_file)
    c = conn.cursor()
    print(userinput)
    usernamecheck(userinput)
    #rows = c.execute("SELECT Username FROM Users WHERE Username = ?",(userinput,))
    #row = c.fetchall()
    #print(row)
    #row = row[0][0]
    #print(type(row))
    #for row in rows:
    print("here")
    if row ==  userinput:
        usertrue = 1
        print("username correct")
    else:
        print("username incorrect")
        exit()
    userandpasswordcheck(userinput, passinput)
    #rows = c.execute("SELECT Password FROM Users WHERE Username = ? AND Password = ?",(userinput, passinput,))
    #rows = rows[0][0]
    #row = c.fetchall()
    #print(row)
    #print(type(row))
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
    privilage_check(admincheck)
    #row = c.execute("SELECT UserName FROM Users WHERE UserType = ?",admincheck,)
    #rows = c.fetchall()
    #rows = rows[0][0]
    for row in rows:
        result = rows
        if rows == username :
            admintrue = 1
            ("administrator access granted")
        else:
            pass




def run():
    global userinput, passinput, usertrue, passtrue, admintrue
    userinput = ""
    passinput = ""
    usertrue = 0 
    passtrue = 0 
    admintrue = 0 
    root = Tk()

    canvas = tk.Canvas()
    canvas.pack(side = tk.LEFT, fill = tk.BOTH, expand=1 )

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
        run_UI(username)
        
    elif admintrue == 1 and passtrue == 1:
       run_admin(username) 

