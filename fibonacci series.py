terms = int(input("how many terms?"))
#for taking the number of Fibonacci series terms to be shown

n1, n2= 0, 1
count= 0
if terms <= 0:
    print("please enter a positive integer")
if terms ==1:
    print ("Fibonacci series upto", terms,":", n1)
else:
    print ("Fibonacci series:")
    while count < terms:
        print(n1)
        nth = n1+n2
        n1=n2
        n2=nth
        count +=1
#for displating the output