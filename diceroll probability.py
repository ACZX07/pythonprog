import random

#function to generate (roll) a random number
def diceRoll():
    return random.randint(1, 6)

#calculation of average probability
def avgProbability(num_rolls):
    totalsixes = 0

    for roll_num in range(1, num_rolls + 1):
        n = diceRoll()
        if n == 6:
            totalsixes += 1
            
        print(f"Roll {roll_num}: {n}")
        #printing the result of each roll
#we set totalsixes to 0 then increment it by +1 everytime we get a 6 from the diceRoll() function
    average_probability = totalsixes / num_rolls
    return average_probability
#avg=[no of obs(here, total no of sixes)/no of total rolls]

# Number of dice rolls to simulate
num_rolls = int(input("Enter the number of rolls: "))

average_probability = avgProbability(num_rolls) #we take total no of rolls as input

print(f"Average probability of getting a 6 in {num_rolls} dice rolls: {average_probability:.4f}")
#f-string displays updated values