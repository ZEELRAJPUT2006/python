import mysql.connector as sql
from tkinter import *
root = Tk()

root.geometry("700x500")
def insert():
    id = e1.get()
    name = e2.get()
    email = e3.get()

    con = sql.connect(
        host = "localhost",
        user = "root",
        password = "root",
        port = 3306,
        database = "schooldb"
        
    )

    cursor = con.cursor()
    # cursor.execute("create database schooldb")
#   cursor.execute("create table student(id int primary key, name varchar(50), email varchar(60))")
#   cursor.execute("insert into student values(5,'jigar','jigar@gmail.com')")
    cursor.execute(f"insert into student values({id},'{name}','{email}')")
    con.commit()
    print("data inserted")



l1 = Label(root,text="id").place(x=200,y=100)
l2 = Label(root,text="name").place(x=200,y=150)
l3 = Label(root,text="email").place(x=200,y=200)

e1 = Entry(root)
e1.place(x=300,y=100)
e2 = Entry(root)
e2.place(x=300,y=150)
e3 = Entry(root)
e3.place(x=300,y=200)

b1 = Button(root,text="submit", command=insert, width=15).place(x=300,y=250)




root.mainloop()