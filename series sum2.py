x = int(input("Enter the value of x:"))
n = int(input("Enter the value of n:"))
sum = 0
for i in range (1,n+1):
    sum = sum + ((x**i)/i)
    
print("Sum of the series is:", sum, )