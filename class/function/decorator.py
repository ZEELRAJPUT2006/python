# def beforetest(test):
#     def wrapper():
#         print("test is calling before test function")
#         test()
#     return wrapper



# @beforetest
# def test():
#     print("test is calling....")

# test()

# @beforetest
# def demo():
#     print("demo is calling ....")

# demo()

# def add(calc):
#     def wrapper(*a):
#         print(a[0]+a[1])
#         calc(*a)
#     return wrapper

# def div(calc):
#     def wrapper(*a):
#         print(a[0]/a[1])
#         calc(*a)
#     return wrapper

# def multi(calc):
#     def wrapper(*a):
#         print(a[0]*a[1])
#         calc(*a)
#     return wrapper



# @add
# @multi
# @div
# def calc(a,b):
#     print("calc operations")

# def calc(*a):
#     print("calc operation")

# calc(10,20)

def valid(number):
    def wrapper(*a):
        if not str(a[0]).isdigit():
            print("only number allowed")
        else:
            number(*a)
        # number()
        
    return wrapper

def alph(number):
    def wrapper(*a):
        if not str(a[0]).isalpha():
            print("only aplha is allowed")
        else:
            number(*a)
    return wrapper

def both(number):
    def wrapper(*a):
        if str(a[0]).isalnum():
            print("only allowed special character")
        else:
            number(*a)
    return wrapper




@both
# @alph
# @valid
def number(a):
    print(a)
    

# number("a")
number("j_j")
