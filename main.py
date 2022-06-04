# I havent quite figured out loops, and i dont know to manage wrong input. i put else: print(invalid) but still wont work.

import random
rulelist1 = ["Rock", "Paper", "Scissors"]
rulelist= ["R","P", "S"]

def game():
    while True:
        print ("*****Welcome to my rock scissor game")
        playerchoice = str(input("Choose between R for rock, P for paper and S for scissors(use Capital R or P or S) \n"))
        computerchoice = computer()
        
        relation = rulelist.index(playerchoice)
        interil = rulelist.index(computerchoice)
        
        
        print("Your choice is %s " %rulelist1[relation])
        print("Computer choice is %s" %rulelist1[interil])
        if playerchoice == "R" and computerchoice == "R":
            print("Its a tie")      
        elif playerchoice == "P" and computerchoice == "R":
            print("You win")
        elif playerchoice == "S" and computerchoice == "R":
            print("You lose")
        elif playerchoice == "R" and computerchoice == "P":
            print("You lose")
        elif playerchoice == "P" and computerchoice == "P":
            print("Its a tie")
        elif playerchoice == "S" and computerchoice == "P":
            print("You win")
        elif playerchoice == "R" and computerchoice == "S":
            print("You win")
        elif playerchoice == "P" and computerchoice == "S":
            print("You lose")
        elif playerchoice == "S" and computerchoice == "S":
            print("Its a tie")
        else:
            print ("Enter a valid option")
        
def computer():
    return random.choice(rulelist)

game()
