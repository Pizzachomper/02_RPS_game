import random

#Functions go here

def check_rounds():
    
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an integer that is more than 0"
        if response != "":
            try:
                #If infinite mode not chosen, check response
                response = int(response)

                #Start of loop
                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue


        return response

def choice_checker(question, valid_list, error):
    
    valid = False
    while not valid:

        #Ask user for their choice
        response = input(question).lower()

        #checks through list and is response is a item in list (or first letter of item), the full name returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item
            
        #output error if not list
        print(error)
        print()


#Main routine goes here

#lists for testing purposes
rps_list = ["rock", "paper", "scissors", "xxx"]

#Ask user for # of rounds

rounds_played = 0

#Ask user for # of rounds, enter for INFINITE MODE

rounds = check_rounds()
end_game = "no"

while end_game == "no":

    #Start of game Play Loop

    #Rounds heading
    print()
    if rounds == "":
        heading = f"Continous Mode: Round {rounds_played + 1}"
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"
    
    print(heading)
    
    choose_instruction = "Please choose rock (r), paper (p), scissors (s) or 'xxx' to exit: "
    choose_error = "Please choose from rock, paper, scissors or 'xxx' to end"

    #Ask user for choice and check it's valid
    choose = choice_checker(choose_instruction, rps_list, choose_error)

    #get computer choice

    
    #compare choice


    #End game if exit code is typed
    if choose == "xxx":
        break

    #Rest of loop / game
    print(f"You choose {choose}")

    rounds_played += 1
    #end_game if requested number of rounds have been played
    if rounds_played == rounds:
        break


#Lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

#Ask user if they have played before
#If yes, show instructions


#If user for # of rounds then loop...

#Ask user if they want to see their game history
#If yes, show instructions
