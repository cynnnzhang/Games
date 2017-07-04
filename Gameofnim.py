from random import *

totalMarble = 12

while totalMarble != 0:
    print("Marbles left:", str(totalMarble))
          
          
    userMove = int(input("How many marbles do you want to take?: "))

    while userMove not in(1,2,3) or userMove > totalMarble:
        print("ILLEGAL MOVE! Try again")
        userMove = int(input("How many marbles do you want to take?: "))

    if userMove == 1:
          totalMarble = totalMarble - 1
          
    elif userMove == 2:
          totalMarble = totalMarble - 2

    else:
          totalMarble = totalMarble - 3

    print("")
    print("Marbles left:", str(totalMarble))

    if totalMarble >= 5:
        cpuMove = randint(1,3)
        print("The computer took", str(cpuMove))
        totalMarble = totalMarble - cpuMove
          
    elif totalMarble >= 2:
        cpuMove = totalMarble - 1
        print("The computer took", str(cpuMove))
        totalMarble = totalMarble - cpuMove
          
    elif totalMarble == 0:
        print("Computer wins!")
        
    else:
        print("The computer took 1")
        totalMarble = totalMarble - 1
        print("")
        print("Human wins!")
        
    print("")



