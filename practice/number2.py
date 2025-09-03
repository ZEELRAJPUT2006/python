# num = 1
# for i in range(5):
#     for j in range(i+1):
#          print(num,end=" ")
#          num += 1
#     print()

# for i in range(5):
#     for j in range(i+1):
#         print(i*j,end=" ")
#     print()

for i in range(1,5):
    for j in range(i+1):
        print()
        for k in range(j*i):
            print((k-1)+1,end=" ")
    print()

