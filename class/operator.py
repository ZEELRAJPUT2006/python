# airthmethic operator #
# a=10
# b=20
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(5**3)
# print(3//10)

# assignment operator #
a=10
a+=20
print(a)
a-= 10
print(a)
a*=20
print(a)
a/=20
print(a)
a**=5
print(a)
a//=4
print(a)

#==================relational operator====================
a=10
b=20
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)
print(a!=b)

#==================== membership operator ====================
a = [10,20,30,40,50]
print(10 in a)
print(60 in a)
print(70 not in a)

# =================== identity operator ======================
a = [10,20,30,40]
b = [20,30,40,50]
print(a is not b)

a = "hello"
b = "hello"
print(a is b)

# ===================== logical operator =========================
print(True or False)
print(False or True)
print(True or True)
print(False or False)

print(True and True)
print(False and False)
print(True and False)

# =================== concat operator ===============================
c = "hello"
d = "world"
print(c+d)