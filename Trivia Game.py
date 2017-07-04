from random import * 

playAgain = "yes"
score = 0
numquestionsAnswered = 0

Q1 = "Q1: What floor is the math pod located on?"
Q2 = "Q2: What is the most visited event at SJAM?"
Q3 = "Q3: What is the name of the notorious event SJAM holds every Wednesday?"
Q4 = "Q4: What is the name of SJAMs business club?"
Q5 = "Q5: State the first name of one of SJAM's current coprimes."
Q6 = "Q6: What is the name of SJAMs current principal? Enter their last name"
Q7 = "Q7: Who is the head of the guidance departement? Enter their last name."
Q8 = "Q8: Who's the head of the English departement? Enter their last name" 
Q9 = "Q9: How many musicals had SJAM had so far?"
Q10 = "Q10: Who's the awesome teacher who teaches grade 10 CS this semester? Enter their last name."



print("Welcome to SJAM TRIVIA!!!!")
printRules = input("Would you like to read the rules of the game?(yes/no): ")

if printRules == "yes":
    print("")
    print("The purpose of the game is to earn points by answering 10 trivia questions about SJAM.")
    print("The best score with all correct answers is 55 points.")
    print("There is an increasing level of difficulty through questions 1-10. Easier questions are worth less points, harder questions are worth more.")
    print("Questions are randomized. However, easier questions are more likely to appear than hard.")
    print("So if you answer the easy questions correctly, it'll be more likely you'll recieve the harder questions.")
    print("Important : Enter all answers in letters (e.g. 5 = five)")
    print("Good luck, and goooo!!!!")

print("")

while playAgain == "yes":
    
    if numquestionsAnswered == 0: 
        a = 10
        b = 9
        c = 8
        d = 7
        e = 6
        f = 5
        g = 4
        h = 3
        i = 2
        j = 1
        
    question = choice([Q1]*a+[Q2]*b+[Q3]*c+[Q4]*d+[Q5]*e+[Q6]*f+[Q7]*g+[Q8]*h+[Q9]*i+[Q10]*j)
    print(question)
    answer = input("Answer: ")
    
    
    if question == Q1 and answer in ["Second", "second"]:
        print("Correct!")
        score = score + 1
        a = 0
        
    elif question == Q2 and answer in ["Double blue day", "double blue day"]:
        print("Correct!")
        score = score + 2
        b = 0
        
    elif question == Q3 and answer in ["Hump day", "hump day"]:
        print("Correct!")
        score = score + 3
        c = 0
        
    elif question == Q4 and answer in ["DECA", "deca", "Deca"]:
        print("Correct!")
        score = score + 4
        d = 0
        
    elif question == Q5 and answer in ["Katelyn", "katelyn", "Abbey", "abbey"]:
        print("Correct!")
        score = score + 5
        e = 0
    
    elif question == Q6 and answer in ["Shortreed", "shortreed"]:
        print("Correct!")
        score = score + 6
        f = 0
        
    elif question == Q7 and answer in ["Todd", "todd"]:
        print("Correct!")
        score = score + 7
        g = 0
        
    elif question == Q8 and answer in ["Grant", "grant"]:
        print("Correct!")
        score = score + 8
        h = 0
        
    elif question == Q9 and answer in ["Five", "five"]:
        print("Correct!")
        score = score + 9
        i = 0
          
    elif question == Q10 and answer in ["Schattman", "schattman"]:
        print("Correct!")
        score = score + 10
        j = 0
        
    else:
        print("Incorrect!")

    numquestionsAnswered = numquestionsAnswered + 1
    print("Your score is", score)
    print("")

    if numquestionsAnswered == 10:
        print("Your final score is", score)
        print("Thanks for playing!")
        print("")

        playAgain = input("Would you like to play again? (yes/no): ")
        numquestionsAnswered = 0 
        print("")
    

