from tkinter import *

root = Tk()

root.geometry("700x500")

# b1 = Button(root, text="LEFT").pack(side=LEFT)
# b2 = Button(root, text="RIGHT").pack(side=RIGHT)
# b3 = Button(root, text="top").pack(side=TOP)
# b4 = Button(root, text="bottom").pack(side=BOTTOM)

# l1 = Label(root,text="id").grid(row=1,column=1)
# l2 = Label(root,text="name").grid(row=2,column=1)
# l3 = Label(root,text="email").grid(row=3,column=1)

# e1 = Entry(root).grid(row=1,column=2)
# e2 = Entry(root).grid(row=2,column=2)
# e3 = Entry(root).grid(row=3,column=2)

# b1 = Button(root,text="submit").grid(row=4,column=2)

l1 = Label(root,text="id").place(x=200,y=100)
l2 = Label(root,text="name").place(x=200,y=150)
l2 = Label(root,text="email").place(x=200,y=200)

e1 = Entry(root).place(x=300, y=100)
e2 = Entry(root).place(x=300, y=150)
e3 = Entry(root).place(x=300,y=200)

b1 = Button(root,text="submit").place(x=300,y=230)
root.mainloop()

