#Version 3 - checks that response is in a given list

#Functions go here
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

#lists for checking responses
rps_list = ["rock", "paper", "scissors", "xxx"]

#Loop for testing purposes
user_choice = ""
while user_choice != "xxx":

    #Ask user for choice and check it's valid
    user_choice = choice_checker("Choose rock, paper, scissors (r/p/s): ", rps_list, "Please choose from rock / paper / scissors" "(or xxx to quit)")

    #Print out choice for comparison purposes
    print(f"You choose {user_choice}.")