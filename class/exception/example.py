# value error
# a = "abc"
# b = int(a)
# print(b)

# index error
# l = [10,20,30]
# print(l[3])

# key error
# d = {"name":"zeel"}
# print(d["email"])

# name error
# a = 10
# print(b)

# type error
# s = "hello"+10
# print(s)

# file not found
# f = open("test.txt",'r')
# data = f.read()
# print(data)

# try:
#     l = [10,20,30]
#     print(l[3])
# except Exception as e:
#     print(e)
# else:
#     print("you are correct, your index is in your list")
# finally:
#     print("hello")

# try:
#     f = open("test.txt",'r')
#     data = f.read()
#     print(data)
#     f.close()
# except Exception as e:
#     print(e)
# finally:
#     if(f is not None):
#         f.close()

# try:
#     d = {"name":"zeel","age":20}
#     print(d["email"])
# except Exception as e:
#     print(e)

# try:
#     s = "hello"+10
#     print(s)
# except Exception as e:
#     print(e)

def test():
    
    a = int(input("enter the numbr"))
    print(a)

test()

def test():
    try:
        a = int(input("enter the number"))
        return 1
    except Exception as e:
        return 0
    finally:
        print("always executed")

k = test()
print(k)
