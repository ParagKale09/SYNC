import random

print("Rock, Paper, Scissors Game")

while True:
    #Enter 1 for Rock, 2 for Paper and 3 for Scissors 
    print("Enter choice \n1. Rock \n2. Paper \n3. Scissors")
    choice = int(input("User turn: "))

    while choice > 3 or choice < 1:
        choice = int(input("Enter valid input: "))
    if choice == 1:
        choice_name = 'rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissors'
    
    print("User choice is: " + choice_name)
    print("Now its computer turn.......")

    comp_choice = random.randint(1, 3)
    
    if comp_choice == 1:
        comp_choice_name = 'rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissors'
        
    print("Computer choice is: " + comp_choice_name)

    print(choice_name + " V/s " + comp_choice_name)

    result = (choice - comp_choice + 3) % 3
    
    if result == 0:
        print("Tie")
    elif result == 1:
        print("Sorry, computer won!")
    else:
        print("You won!")
        
    ans = input("Do you want to play again? (Y/N)")
    if ans == 'n' or ans == 'N':
        break

