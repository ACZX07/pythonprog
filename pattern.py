#THIS PROGRAM PRINTS A REVERSE NUM PATTERN PYRAMID OF 1,2,3,4,5
for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j, end="")
    print("\n")