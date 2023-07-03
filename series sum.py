#sum of the series 1+x¹+x²+x³+.....+x^n

x = int(input("Enter the value of x:"))
n = int(input("Enter the value of n:"))
sum = 0
for i in range (n+1):
    sum += x**i
    
print("Sum of the series is:", sum)