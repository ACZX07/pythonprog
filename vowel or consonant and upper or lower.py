#THIS PROGRAMS CHECKS IF A LETTER IS UPPERCASE/LOWERCASE AND VOWEL/CONSONANT 

letter = input("Enter any letter:")
for i in letter:
    if (i == "a" or i=="e" or i=="i" or i=="o" or i=="u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U"):
        i1 = "vowel"
    else:
        i1 = "consonant"
    if i.isupper():
        i2 = "uppercase"
    if i.islower():
        i2 = "lowercase"
        
print("It is a", i2, i1)    