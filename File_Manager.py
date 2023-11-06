import os
import sqlite3


def run():
    with open('Position.txt','r') as f:
        pos = f.read()

    print(os.getcwd())

    x=0
    contacts = []
    conn = sqlite3.connect('contact.db')
    print("connected to SQLite")
    c = conn.cursor()
    row = c.execute("SELECT Username FROM Users WHERE Position = ?",(pos,))
    rows = c.fetchall()
    for row in rows:
        #contacts[x].append(row)
        contacts.append(row)

    for n in range(0,len(contacts)): 
        os.mkdir(str(contacts[n]))



