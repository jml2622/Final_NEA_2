import os
import sqlite3


def run():
    print(os.getcwd())

    x=0
    contacts = []
    conn = sqlite3.connect('contact.db')
    print("connected to SQLite")
    c = conn.cursor()
    row = c.execute("SELECT EmployeID FROM Users")
    rows = c.fetchall()
    for row in rows:
        #contacts[x].append(row)
        contacts.append(row)
        print(contacts)

    for n in range(0,len(contacts)): 
        os.mkdir(str(contacts[n]))



