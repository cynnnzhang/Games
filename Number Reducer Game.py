print("Welcome to the Number Reduction Game!")
num = int(input("Enter a starting value greater than 5: "))

if num < 5:
    print("Please enter a number greater than 5")
    num = int(input("Enter the starting value: "))
              
while num > 0:

#Computersturn
    choice1 = int(num / 2)
    choice2 = int(num - 1)

    if choice1 == choice2:
        print("My only choice is", choice1)
        num = choice1
        
    elif choice1 % 2 == 0 and choice2 % 2 != 0:
        print("My choices are", choice1, "or", choice2)
        num = choice1
     
    elif choice1 % 2 != 0 and choice2 % 2 == 0:
        print("My choices are", choice1, "or", choice2)
        num = choice2

    elif choice1 % 2 == 0 and choice2 % 2 == 0:
        print("My choices are", choice1, "or", choice2)
        calculation = choice1
        divisions = 0
     
        while calculation % 2 == 0:
            divisions = divisions + 1
            calculation = calculation / 2
        
        if divisions % 2 == 0:
            num = choice2
            
        else:
            num = choice1
            
    else:
        print("My choices are", choice1, "or", choice2)
        num = choice1
        
    print("I choose", num)
    print("")
    if num == 0:
        print("Sorry, I win this time.")


#PlayersTurn
        
    if num != 0:
        choice1 = int(num / 2)
        choice2 = int(num - 1)
        num = int(input("Your choices are " + str(choice1) + " or " + str(choice2) + ": "))
        
        while num not in [choice1, choice2]:
            print("Please enter a valid option")
            num = int(input("Your choices are " + str(choice1) + " or " + str(choice2) + ": "))

        if num == 0:
            print("Congrats! You win!")
    print ("")
    
print("Game over! Thanks for playing!")
