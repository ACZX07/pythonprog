n=int(input("enter number:"))
#for taking any number as input

sum = 0
t = n
while t > 0:
    digit = t % 10
    sum += digit **3
    t//=10
#for checking if the input is an armstrong number
    
if n == sum:
    print (n,"is an armstrong number")
    
else:
    print(n,"is not an armstrong number")
#for displaying the final output 