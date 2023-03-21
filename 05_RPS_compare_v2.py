import random

#RPS componenet 3 - compare user choice and computer choice
rps_list = ["rock", "paper", "scissors"]

def play_game():
    #Get user input
    user_choice = input("Choose rock, paper, or scissors: ")

    #Make an error option
    while user_choice not in rps_list:
        user_choice = input("Error, Please choose Rock, Paper, Scissors: ")

    #Get computer choice
    comp_choice = random.choice(rps_list)

    #Determine winner
    if user_choice == comp_choice:
        print(f"Its a Tie! both players choose {user_choice}")
    elif user_choice == "rock" and comp_choice == "scissors":
        print("You win! Rock uses mighty bolder and smashed scissors.")
    elif user_choice == "paper" and comp_choice == "rock":
        print("You win! Paper uses blistering paper cut and injures rock.")
    elif user_choice == "scissors" and comp_choice == "paper":
        print("You win! Scissor used ninja slice and cut paper.")
    else:
        print(f"You lose! Grandmaster uses {comp_choice} and summons ultimate trio and wipes {user_choice} out of the earth.")

#Play game
play_game()