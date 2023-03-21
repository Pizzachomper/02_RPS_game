#RPS componenet 3 - compare user choice and computer choice
rps_list = ["rock", "paper", "scissors"]
comp_index = 0
for item in rps_list:
    user_index = 0
    for item in rps_list:
        user_choice = rps_list[user_index]
        comp_choice = rps_list[comp_index]
        user_index += 1

        #Compare options
        if comp_choice == user_choice:
            result = "Its a tie"
        if comp_choice > user_choice:
            result = "You win"
        if comp_choice < user_choice:
            result = "You Lose"
        
        
        
        print(f"You choose {user_choice}, the computer choose {comp_choice}. Results: {result}")

comp_index += 1
print()