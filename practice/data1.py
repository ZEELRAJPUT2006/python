# import sqlite3

# db = sqlite3.connect("mypython.db")
# db.execute("create table student(id int primary key, name varchar(50), age int)")
# db.execute("insert into student values(1,'john',6)")
# db.execute("update student set name='bob' where id=1")
# data = db.execute("select * from student")
# for dt in data:
#     print(dt)
# db.commit()


import sqlite3
db = sqlite3.connect('practice.db')
# db.execute("create table emp(id int primary key, name varchar(50), age int, email varchar(50))")
db.execute("insert into emp values(1,'john',25,'john@gmail.com')")
db.commit()
