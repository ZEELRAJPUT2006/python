import sqlite3

db = sqlite3.connect("data.db")

# db.execute("create table emp(id int primary key, name varchar(50), email varchar(50))")

# db.execute("insert into emp values(3,'devanshi','devansi@gmail.com')")

# db.execute("update emp set name='nency' where id = 2")

# db.execute("delete from emp where id=3")
# db.commit()

data = db.execute("select * from emp").fetchall()
# print(data)

for dt in data:
    print(dt)