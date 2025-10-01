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

def add(calc):
    def wrapper(*a):
        print(a[0]+a[1])
        calc(*a)
    return wrapper

def div(calc):
    def wrapper(*a):
        print(a[0]/a[1])
        calc(*a)
    return wrapper

def multi(calc):
    def wrapper(*a):
        print(a[0]*a[1])
        calc(*a)
    return wrapper



@add
@multi
@div
# def calc(a,b):
#     print("calc operations")

def calc(*a):
    print("calc operation")

calc(10,20,30)