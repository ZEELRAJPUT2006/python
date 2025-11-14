from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector as sql
root = Tk()

root.geometry("700x600")

con = sql.connect(
    host = "localhost",
    user = "root",
    password = "root",
    port = "3306",
    database = "school"

)

cursor = con.cursor()
# cursor.execute("create database school")
 # cursor.execute("create table student(id int primary key auto_increment, name varchar(50), email varchar(50), phone varchar(50))")

# def insert():
#     name = e1.get()
#     email = e2.get()
#     phone = e3.get()

#     
    
    # qry = "INSERT INTO student (name, email, phone) VALUES (%s, %s, %s)"
    # values = (name, email, phone)
    # cursor.execute(qry,values)
    # con.commit()
    # print("data inserted")


def show():
    cursor = con.cursor()
    cursor.execute("select * from student")
    data = cursor.fetchall()
    for i,(id,name,email,phone) in enumerate(data, start=1):
        table.insert("",END,values=(id,name,email,phone))

def adddata():
    name = e1.get()
    email = e2.get()
    phone = e3.get()
    cursor = con.cursor()
    qry = "insert into student values (%s,%s,%s,%s)"
    val = (0,name,email,phone)
    cursor.execute(qry,val)
    con.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e1.focus()
    for i in table.get_children():
        table.delete(i)
    show()
    messagebox.showinfo("success","data inserted")

id = 0
def getdata(self):
    global id
    rowid = table.selection()[0]
    data = table.set(rowid)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    id = data['id']
    e1.insert(0,data['name'])
    e2.insert(0,data['email'])
    e3.insert(0,data['phone'])


def updatedata():
    name = e1.get()
    email = e2.get()
    phone = e3.get()
    cursor = con.cursor()
    qry = "update student set name=%s, email=%s,phone=%s where id=%s"
    val = (name,email,phone,id)
    cursor.execute(qry,val)
    con.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e1.focus()
    for i in table.get_children():
        table.delete(i)
    show()
    messagebox.showinfo("success","data updated") 


def deletedata():
    cursor = con.cursor()
    cursor.execute(f"delete from student where id={id}")
    con.commit()
    for i in table.get_children():
        table.delete(i)
    show()
    messagebox.showinfo("success","data deleted")

l1 = Label(root,text="name").place(x=300,y=200)
l2 = Label(root,text="email").place(x=300,y=250)
l3 = Label(root,text="phone").place(x=300,y=300)

e1 = Entry(root)
e1.place(x=350,y=200)
e2 = Entry(root)
e2.place(x=350,y=250)
e3 = Entry(root)
e3.place(x=350,y=300)

b1 = Button(root,text="add", command=adddata).place(x=350,y=350)
b2 = Button(root,text="update", command=updatedata).place(x=400,y=350)
b1 = Button(root,text="delete", command=deletedata).place(x=470,y=350)


cols = ("id","name","email","phone")
table = ttk.Treeview(root, columns=cols, show="headings")
for col in cols:
    table.heading(col, text=col)
    table.place(x=10,y=400)

show()

table.bind("<Double-Button-1>",getdata)
root.mainloop()