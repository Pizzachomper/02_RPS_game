#RPS Component 6 - scoring system

#Round won will be calculated
rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

#Results for testing purposes
test_results = ["won", "won", "loss", "loss", "tie"]

#Play game
for item in test_results:
    rounds_played += 1

    #Generate computer choice

    result = item

    if result == "tie":
        result = "Its a tie"
        rounds_drawn += 1

    elif result == "loss":
        result = "You lose"
        rounds_lost += 1

#Quick calculations
rounds_won = rounds_played - rounds_drawn - rounds_lost

#End of game statements
print()
print('***** End Game Summary  *****')
print(f"Won: {rounds_won} \t\t Lost: {rounds_lost} \t\t Draw: {rounds_drawn}")
print()
print("Thanks for playing")