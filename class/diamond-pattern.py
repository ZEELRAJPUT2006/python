lines = 5
for i in range(lines):
    print(" "*(lines-i),"* "*(i+1),end=" ")
    print()
for i in range(lines-1,0,-1):
    print(" "*((lines-1)-i+2),"* "*(i),end="")
    print()