#Functions go here

def check_rounds():
    
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter>" "or an integer that is more than 0"
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue


        return response
    
#Main routine goes here

rounds_played = 0
choose_instruction = "Please choose rock (r), paper (p), or scissors (s)"

#Ask user for # of rounds, enter for INFINITE MODE

rounds = check_rounds()
end_game = "no"
while end_game == "no":

    #Rounds heading
    print()
    if rounds == "":
        heading = f"Continue mode: Round {rounds_played}"
        print(heading)
        choose = input(f"{choose_instruction} or xxx to quit")
        if choose == "xxx":
            break

    else:
        heading = f"Round {rounds_played + 1} of {rounds}"
        print(heading)
        choose = input(choose_instruction)
        if rounds_played == rounds - 1:
            end_game = "yes"

    #rest of loop / game
    print(f"You choose {choose}")

    rounds_played += 1
    #end_game if requested number of rounds have been played
    if rounds_played == rounds:
        break

#Put endgame content here
print("Thank you for playing my game (:")