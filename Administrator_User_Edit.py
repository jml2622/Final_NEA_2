import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import *







def Delete(conn, a):
    EmpID = a.get()
    print(EmpID)
    conn.execute("DELETE FROM Users WHERE EmployeID = ?",(EmpID))
    conn.commit()
    conn.close()
    print("completed")





def run():

    def database():
        EmpID = a.get()
        Usrnme = b.get()
        PssWrd = c.get()
        UsrTpe = d.get()
        Pos = e.get()


        print(EmpID)
        conn.execute("INSERT or IGNORE INTO Users VALUES (?,?,?,?,?)", (EmpID, Usrnme, PssWrd, UsrTpe, Pos))
        conn.commit()
        print ("Changes Committed")
        conn.close() 

    my_file = ('/Users/jacoblewis/Library/CloudStorage/OneDrive-StJohnFisherCatholicAcademy/Documents/nea/contact.db')
    conn = sqlite3.connect(my_file)


    root = Tk()


    root.title("Add User")
    root.geometry("1400x400")


        


    a = Entry(root)
    a.grid(row=0, column = 0, pady=10)


    b = Entry(root)
    b.grid(row=0, column = 1, pady=10)
    #entered1=(b.get())

    c = Entry(root)
    c.grid(row=0, column = 2, pady=10)


    d = Entry(root)
    d.grid(row=0, column = 3, pady=10)


    e = Entry(root)
    e.grid(row=0, column = 4, pady=10)

    finalise = Button(root, text = "Commit Changes", command = database)
    finalise.grid(row = 1, column = 0, pady = 20)


    infomation = Label(root, text="Employee ID:   Username:  Password:   Type of User:   Position")
    infomation.grid(row=2,column=0, pady=20)



    delete = Button(root, text="Delete User", command = Delete)
    delete.grid(row = 1, column = 5, pady = 20)
    root.mainloop()

if __name__ == "__main__":
    run()