#THIS PROGRAM PRINTS A REVERSE MULTIPLICATION TABLE FOR ANY NUMBER UPTO THE LIMIT SET BY THE USER 

n = int(input("Enter the number you need the table of: "))

lim = int(input("Enter the ending multiple: "))

for i in range(lim,0,-1):
    print(i,"*",n,"=",i*n)