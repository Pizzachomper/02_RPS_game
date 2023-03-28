import random
#Functions go here


def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        # If they say yes, output 'program continues'
        if response == "yes" or response == "y":
            response = "yes"
            return response

        # If they say no, output 'display instructions'
        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("please answer yes / no")

def instructions():

    print('''

^*^ How to Play ^*^

This is a game made to play rock, paper, scissors in python. 
Answer with how many rounds you will play or type enter for infinite mode. 

Please type r (Rock), p (Paper), s (Scissors) to use commands and see if you are beating the computer choice.

If you are finished type xxx or x to quit, you can see your game summary at the end of your game. 
Enjoy 😆
    
    ''')

    return ""

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


#Lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

#Main routine goes here

#Ask user for # of rounds, then loop

rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

#Ask user if they have played before
#If yes, show instructions

played_before = yes_no("Have you played this game before? ")
print("You choose {}".format(played_before))

if played_before == "no":
    instructions()

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
    
    #End game if exit code is typed
    if choose == "xxx":
        break

    #get computer choice
    comp_choice = random.choice(rps_list[:-1])
    
    #print comp choice and user choice
    print(f"You choose {choose}")
    print("Comp_choice: ", comp_choice)
    
    #compare choice

    if choose == comp_choice:
        print(f"Its a Tie! both players choose {choose}")
        result = "tie"
        rounds_drawn += 1
    elif choose == "rock" and comp_choice == "scissors":
        print("You win! Rock uses mighty bolder and smashed scissors.")
        result = "won"
    elif choose == "paper" and comp_choice == "rock":
        print("You win! Paper uses blistering paper cut and injures rock.")
        result = "won"
    elif choose == "scissors" and comp_choice == "paper":
        print("You win! Scissor used ninja slice and cut paper.")
        result = "won"
    else:
        print(f"You lose! Grandmaster uses {comp_choice} and summons ultimate trio and wipes {choose} out of the earth.")
        result = "lost"
        rounds_lost += 1


    #Rest of loop / game

    rounds_played += 1
    #end_game if requested number of rounds have been played
    if rounds_played == rounds:
        break

#If user for # of rounds then loop...

#Ask user if they want to see their game history

#Show game statistics
#Quick calculations
rounds_won = rounds_played - rounds_drawn - rounds_lost

#Calculate Game Stats
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100
percent_tie = rounds_drawn / rounds_played * 100

#End of game statements
print()
print('***** End Game Summary  *****')
print(f"Win: {rounds_won}, {percent_win:.0f}% \nLoss: {rounds_lost}, {percent_lose:.0f}% \nTie: {rounds_drawn}, {percent_tie:.0f}%")
print()