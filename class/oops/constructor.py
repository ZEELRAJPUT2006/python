# class student:
#     def __init__(self,id,name,email):
#         self.id = id
#         self.name = name
#         self.email = email
        
#     def display(self):
#         # print("running student")
#         print(self.id,self.name,self.email)

# s = student(1,"Tisha","tisha@gmail.com")
# s.display()

# class emp:
#     def __init__(self,emp_id,emp_name,emp_email,salary):
#         self.emp_id = emp_id
#         self.emp_name = emp_name
#         self.emp_email = emp_email
#         self.salary = salary

#     def dispaly(self):
#         print("emp id : ",self.emp_id)
#         print("emp name : ",self.emp_name )
#         print("emp email : ",self.emp_email)
#         print("emp salary : ",self.salary)

# e = emp(101,"Tisha","Tisha@gmail.com",50000)
# e.dispaly()
        
# class student:
#     clg = 'C.B.Patel'
#     def __init__(self,id,name,email):
#         self.id = id
#         self.name = name
#         self.email = email

#     @classmethod
#     def smaple(self):
#         print("sample is running........")
#         print(self.clg)

#     @staticmethod
#     def run():
#             print("run is calling.......")



#     def display(self):
#         # print("running student")
#         print(self.id,self.name,self.email,self.clg)

# student.clg 
# student.smaple()
# student.run()
# s = student(1,"Tisha","tisha@gmail.com")
# s.display()

# class demo():
#     id = 10
#     def disp(self):
#         print("display calling....")
   
#     @classmethod
#     def sample(self):
#         print("sample is calling")

#     @staticmethod
#     def util(self):
#         print("static is calling....",self)

# d = demo()
# d.disp()
# demo.sample()
# demo.util(10)

class product:
    def __init__(self,p_id,p_name,p_price):
        self.p_id = p_id
        self.p_name = p_name
        self.p_price = p_price
        

    def disp(self):
        print("product id : ",self.p_id)
        print("product name : ", self.p_name)
        print("product price", self.p_price)

p = product(1,"pen",10)
p1 = product(2,"pencil",5)
p2 = product(3,"notebook",50)
print("<===========================================>")
p.disp()
print("<===========================================>")
p1.disp()
print("<===========================================>")
p2.disp()
print("<===========================================>")

