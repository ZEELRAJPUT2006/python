import re

k = re.match('H.l',"Hello python")
k = re.search('H.l',"hello python")
k = re.findall('H.l',"hello python")
k = re.match('^hello',"hello python")
k = re.search('python$',"hello python")
print(k)

# num = input("enter the number")
# k = re.match('[0-9]{9}$',num)
# if k:
#     print("valid number")
# else:
#     print("invalid number")

# email = input("enter the email")
# k = re.match('[a-zA-Z0-9._%+-]+@[a-zA-Z.-]+\.[a-zA-Z{2,}]$',email)
# if k:
#     print("email is valid")
# else:
#     print("invalid email")

# password = input("Enter the password: ")
# k = re.findall('^[A-Z].*[0-9].*[a-z]$', password)

# if k:
#     print("valid password")
# else:
#     print("invalid password")
