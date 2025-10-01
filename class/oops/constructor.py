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
        
class student:
    clg = 'C.B.Patel'
    def __init__(self,id,name,email):
        self.id = id
        self.name = name
        self.email = email

    @classmethod
    def smaple(self):
        print("sample is running........")
        print(self.clg)

    @staticmethod
    def run():
            print("run is calling.......")



    def display(self):
        # print("running student")
        print(self.id,self.name,self.email,self.clg)

student.clg 
student.smaple()
student.run()
s = student(1,"Tisha","tisha@gmail.com")
s.display()