n = int(input("Enter the number you need the table of: "))

lim = int(input("Enter the ending multiple: "))

for i in range(lim,0,-1):
    print(i,"*",n,"=",i*n)