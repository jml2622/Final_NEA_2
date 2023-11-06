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
        
