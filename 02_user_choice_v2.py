#version 2 - error message included when calling function



#Functions go here
def choice_checker(question, error):
    
    valid = False
    while not valid:

        #Ask user for their choice
        response = input(question).lower()

        if response == "r" or response == "rock":
            return "Rock"
        
        elif response == "p" or response == "paper":
            return "Paper"
        
        elif response == "s" or response == "scissors":
            return "Scissors"

        # check for exit code
        elif response == "xxx":
            return "xxx"
        
        else:
            print(error)


#Main routine goes here

#Loop for testing purposes
user_choice = ""
while user_choice != "xxx":

    #Ask user for choice and check it's valid
    user_choice = choice_checker("Choose rock, paper, scissors (r/p/s): ", "Please choose from rock / paper / scissors" "(or xxx to quit)")

    #Print out choice for comparison purposes
    print(f"You choose {user_choice}.")