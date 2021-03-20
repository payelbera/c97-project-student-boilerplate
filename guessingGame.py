import random
print("Guessing Number game")
number = random.randint(1,9)
chance = 0
print("Guess a number between 1-9")

# write while loop for chance less than 5:
    # take input from user convert into int and store in a variable called guess 
     #check if guess equal to number
        # print a congralutaion message
        break
    # else check if guess less than number
        # print "Guess is low
    # else:
        # print "Guess is high
chance+=1

if(not chance<5):
    print("You lose, the number was",number)






    