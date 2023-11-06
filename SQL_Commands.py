import sqlite3


def file_connection():
    my_file = ('/Users/jacoblewis/Library/CloudStorage/OneDrive-StJohnFisherCatholicAcademy/Documents/nea/contact.db')
    conn = sqlite3.connect(my_file)
    c = conn.cursor()


def usernamecheck(userinput):
    rows = c.execute("SELECT Username FROM Users WHERE Username = ?",(userinput,))
    row = c.fetchall()

def userandpasswordcheck(userinput, passinput):
    rows = c.execute("SELECT Password FROM Users WHERE Username = ? AND Password = ?",(userinput, passinput,))
    row = c.fetchall()

def privilage_check(admincheck):
    row = c.execute("SELECT UserName FROM Users WHERE UserType = ?",admincheck,)
    rows = c.fetchall()

def user_adding(EmpID, Usrnme, PssWrd, UsrTpe, Pos):
    conn.execute("INSERT INTO Users VALUES (?,?,?,?,?)", (EmpID, Usrnme, PssWrd, UsrTpe, Pos))
    conn.commit()

def user_deleting(EmpID):
    conn.execute("DELETE FROM Users WHERE EmployeID = ?",(EmpID))
    conn.commit()
    conn.close()

def File_Manager():
    row = c.execute("SELECT Username FROM Users WHERE Position = ?",(pos,))
    rows = c.fetchall()
    return(rows)

def File_Manager_Server():
    row = c.execute("SELECT EmployeID FROM Users")
    rows = c.fetchall()
    return rows
 

