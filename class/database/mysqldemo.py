import mysql.connector as sql

con = sql.connect(
      host = 'localhost',
      username = 'root',
      password = 'root',
      port = 3306,
      database = 'pythonsql' 
     

)

cursor = con.cursor()

# cursor.execute("create database pythonsql")

# cursor.execute("create table emp(id int primary key, name varchar(20), age int, email varchar(50))")

# cursor.execute("insert into emp values(1,'tisha',20,'tisha@gmail.com')")

# cursor.execute("update emp set name='zeel' where id=1")

# cursor.execute("delete from emp where id=1")

# con.commit()

# cursor.execute("select * from emp")
# data = cursor.fetchall()
# print(data)
