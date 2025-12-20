# import mysql.connector as sql
# con = sql.connect(
#     host="localhost",
#     user = 'root',
#     password = 'root',
#     port = 3306,
#     database = 'mysqlpython'
    
# )

# cursor = con.cursor()
# cursor.execute("create database mysqlpython")
# cursor.execute("create table emp(id int primary key,name varchar(50),age int, email varchar(50))")
# cursor.execute("insert into emp values(1,'john',22,'john@gmail.com')")
# cursor.execute("update emp set age=25 where id=1")
# cursor.execute("delete from emp where id=1")
# con.commit()

# a = "test"
# b = "test"
# c = a

# print(a is b)
# print(a is c)

a = [10,20,30,40,50]

print(10 in a)
print(100 not in a)

a  ="Hello"
print('h' in a)
