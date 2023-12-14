from tkinter import *
import sqlite3
from tkinter import ttk
from turtle import width

def validate():
    # get form data
    name = entryName.get()
    email = entryEmail.get()
    age = entryAge.get()
    
    conn = sqlite3.connect("mydatabase.db")
    cur = conn.cursor()

    req  = "CREATE TABLE IF NOT EXISTS students ( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL, age INTEGER NOT NULL)"
    cur.execute(req)
    
    rqt = "INSERT INTO students (name, email, age) VALUES (?, ?, ?)"
    cur.execute(rqt, (name, email, age))
    conn.commit()
    conn.close()
    
    
root = Tk()
root.geometry("600x400")

#==============================
# create a form to insert date
#==============================
# Lbael & Entry for name

lblName = Label(root, text="Name : ")
lblName.place(x=10, y = 10)
entryName = Entry(root)
entryName.place(x=100, y = 10, width=200)

# Lbael & Entry for email

lblEmail = Label(root, text="E mail : ")
lblEmail.place(x=350, y = 10)
entryEmail = Entry(root)
entryEmail.place(x=390, y = 10, width=200)

# Lbael & Entry for age

lblAge = Label(root, text="Age : ")
lblAge.place(x=10, y = 40)
entryAge = Entry(root)
entryAge.place(x=100, y = 40, width=100)

# validate button
btnValide = Button(root, text="valider", command = validate)
btnValide.place(x =350, y = 40, width=200, height=25)

#==============================
# display data
#==============================

tree = ttk.Treeview(root, columns =(1,2,3,4), height =5, show="headings")
tree.place(x= 25, y = 170, width=550, height=175)

tree.heading(1 , text = "ID")
tree.heading(2 , text = "Name")
tree.heading(3 , text = "Email")
tree.heading(4 , text = "Age")

tree.column(1, width =50)
tree.column(2 ,width =100)
tree.column(3 ,width =100)
tree.column(3 ,width =50)


conn = sqlite3.connect("mydatabase.db")
cur = conn.cursor()
req  = "CREATE TABLE IF NOT EXISTS students ( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL, age INTEGER NOT NULL)"
cur.execute(req)
select  = cur.execute("SELECT * FROM students")
for row in select:
    tree.insert('', END, values = row)
# cur.execute(select)

root.mainloop()