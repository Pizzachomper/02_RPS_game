import random

#set balance for testing purposes
balance = 5

rounds_played = 0

play_again = input("Press <enter> to play . . .").lower()
while play_again == "":

    #Increase # of rounds played
    rounds_played += 1
    

    # Print round number
    print()
    print("*** Round #{} ***".format(rounds_played))

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press enter to play again or 'xxx' to quit")

print()