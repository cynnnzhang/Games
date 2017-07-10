from random import*

score = 100

roll = "y"
while score >0 and roll == "y":
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        Sum = dice1 +dice2
        print("You rolled a", dice1, "and a", dice2)

    
        if Sum>=10 and dice1 == dice2:
            score = score + 100
            print("You win $100. You now have $", str(score))
            
        elif Sum >= 10:
            score = score + 30
            print("You win $30. You now have $", str(score))
            
        elif dice1 == dice2:
            score = score + 20
            print("You win $20. You now have $", str(score))

        else:
            score = score - 40
            print("You lose $40. You now have $", str(score))

        if score > 0:
            roll = input("Do you want to roll the dice again (y/n)?")
            


        if score <= 0:
            roll = input("Would you like to roll the dice again? (y/n): ")

if score <= 0:
    print("You went bust! We enjoyed taking your money. Play again soon!")
    
print("Thanks for playing.")
