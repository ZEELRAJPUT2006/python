# n = int(input('enter number'))
# temp = n
# sum = 0

# while n!=0:
#     rem = n%10
#     sum += rem**3
#     n = n // 10

# if sum == temp:
#     print('number is amstrong')
# else:
#     print('number is not amstrong')


# n = int(input('enter number'))
# flag = 0

# for i in range(2,n):
#     if n % i == 0:
#         flag = 1
#         break

# if flag == 0:
#     print('number is prime')
# else:
#     print('number is not prime')



# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)

# print(fact(5))

# n = int(input('enter number'))
# a = 0
# b = 1
# for i in range(0,n):
#     c = a+b
#     print(c)
#     a = b
#     b = c

# s = input('enter the string')
# rev = s[::-1]
# print(rev)

# s = input('enter string')
# count = 0
# con = 0
# di = 0

# for ch in s:
#     if ch.lower() in 'aeiou':
#         count += 1
#     elif ch.isalpha():
#         con += 1
#     elif ch.isdigit():
#         di += 1

# print('vowels count',count)
# print('constant',con)
# print('digit',di)

# li = [1,2,3,4,1,2]
# new_list = list(set(li))
# print(new_list)

# n = [1,2,3,4,5,6]
# print('largest number is:',max(n))


