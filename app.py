"""
An console game of rock, paper, scissors with a computer
"""
# initialize the game
import random


#maintain user score
user_score = 0
computer_score = 0


def game():

    #access the global
    global user_score
    global computer_score
    
    # set the choices
    choices = ["rock", "paper", "scissors"]

    user_choice = input("Choose rock, paper, or scissors: ")

    #validate user choice
    while user_choice not in choices:
        print("Invalid choice. Please try again")
        user_choice = input("Choose rock, paper, or scissors: ")

    # get the computer's choice
    computer_choice = random.choice(choices)

    # print the computer's choice
    print(f"The computer chose {computer_choice}")

    # determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
        #increment user score
        user_score += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
        #increment user score
        user_score += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        #increment user score
        user_score += 1
    else:
        print("You lose!")
        #increment computer score
        computer_score += 1 

    # ask user the option to play again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again == "yes":
        game()
    else:
        print("Thanks for playing!")
        print(f"User score: {user_score}")
        print(f"Computer score: {computer_score}")

# start the game
game()
    