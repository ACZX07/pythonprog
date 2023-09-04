n=int(input("Enter the number of rows:"))
sym=(input("Choose a symbol: "))
for i in range (0,n):
#printing the spaces
    for j in range (0, n-i-1):
        print(end=" ")
#printing the symbols
    for j in range (0, i+1):
        print(sym,"", end = "")
        #space after symbols is not necessary, give if u want
    print()
    
