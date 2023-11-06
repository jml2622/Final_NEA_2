import tkinter as tk
from tkinter import ttk
from tkinter import *
import datetime
import subprocess

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
    print("i hate")
    username = "Mr Blobby"
    time = datetime.datetime.now()
    timestamp = ("<",time,">")
    finished = (timestamp, " User[",username,"]","\n")
    userentry = entry.get()
    message = ("\n",str(finished),"\n",str(userentry))
    print(message)
    file = open("messages.txt","a")
    file.writelines(message)
    file.close()
    file = open("new message.txt","a")
    file.writelines(message)
    file.close()
    #subprocess.run(["python","encryption butcher edition.py"])
    #pass





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