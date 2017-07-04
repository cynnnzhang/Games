###########################################
#Objects: Paint, Wall, Sconce, Window, Art
###########################################
#Explanations
###########################################
    #Paint beats Wall since it covers it
    #Paint beats Window since spray paint can be used to grafitti it

    #Wall beats Window since wall is needed to install a window
    #Wall beats Sconce since will is needed to install a sconce

    #Sconce beats Art since the art cannot be seen in the night without the artificial light
    #Sconce beats Paint since the paint colour cannot be seen in the night without the artificial light

    #Window beats Sconce since it brings in natural light (better than artificial)
    #Window beats Art since the real art is the natural world outside

    #Art beats Paint since is is much more artistic and expressive
    #Art beats Wall since a hole must be drilled to hang up art

from random import *
playAgain = "yes"

while playAgain == "yes":
    playerScore = 0
    compScore = 0
    
    print("")
    numPlays = int(input("How many times would you like to play?: "))

    for x in range(numPlays):
        playerChoice = input("Enter your move (P, Wa, S, Wi, A): ")
        while playerChoice not in ["P", "Wa", "S", "Wi", "A"]:
            print("Please enter a valid option")
            playerChoice = input("Enter your move (P, Wa, S, Wi, A): ")   
        cpu = choice(["P", "Wa", "S", "Wi", "A"])
        print("The computer played", cpu)

        if playerChoice == cpu:
            print("You tied this round")
            print("Your current score is", playerScore)
            print("The computer's current score is", compScore)
        
        elif playerChoice == "P" and cpu == "Wa":
            print("You won this round!")
            playerScore = playerScore + 1
            print("Your current score is", playerScore)
            print("The computer's current score is", compScore)
        
        elif playerChoice == "P" and cpu == "Wi":
            print("You won this round!")
            playerScore = playerScore + 1
            print("Your current score is", playerScore)
            print("The computer's current score is", compScore)
        
        elif playerChoice == "Wa" and cpu == "Wi":
            print("You won this round!")
            playerScore = playerScore + 1
            print("Your current score is", playerScore)
            print("The computer's current score is", compScore)
        
        elif playerChoice == "Wa" and cpu == "S":
            print("You won this round!")
            playerScore = playerScore + 1
            print("Your current score is", playerScore)
            print("The computer's current score is", compScore)
        
        elif playerChoice == "S" and cpu == "A":
            print("You won this round!")
            playerScore = playerScore + 1
            print("Your current score is", playerScore)
            print("The computer's current score is", compScore)
        
        elif playerChoice == "S" and cpu == "P":
            print("You won this round!")
            playerScore = playerScore + 1
            print("Your current score is", playerScore)
            print("The computer's current score is", compScore)
        
        elif playerChoice == "Wi" and cpu == "S":
            print("You won this round!")
            playerScore = playerScore + 1
            print("Your current score is", playerScore)
            print("The computer's current score is", compScore)
        
        elif playerChoice == "Wi" and cpu == "A":
            print("You won this round!")
            playerScore = playerScore + 1
            print("Your current score is", playerScore)
            print("The computer's current score is", compScore)
        
        elif playerChoice == "A" and cpu == "P":
            print("You won this round!")
            playerScore = playerScore + 1
            print("Your current score is", playerScore)
            print("The computer's current score is", compScore)
        
        elif playerChoice == "A" and cpu == "Wa":
            print("You won this round!")
            playerScore = playerScore + 1
            print("Your current score is", playerScore)
            print("The computer's current score is", compScore)
        
        else: 
            print("Computer won this round")
            compScore = compScore + 1
            print("Your current score is", playerScore)
            print("The computer's current score is", compScore)

        print("")

    print("*" * 20)
    print("Your total number of wins is", playerScore)
    print("The computers total number of wins is", compScore)

    if playerScore == compScore:
        print("You tied with the computer! Thanks for playing!")

    elif playerScore > compScore:
        print("You won the game! Thanks for playing!")

    else:
        print("The computer won the game! Thanks for playing!")

    print("")
    playAgain = input("Would you like to play again? (yes/no): ")



