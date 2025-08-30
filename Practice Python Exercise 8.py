#Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, 
# and ask if the players want to start a new game)

#Remember the rules:
#Rock beats scissors
#Scissors beats paper
#Paper beats rock

correct_response = ["rock", "paper", "scissors"]
while True:
    response_needed = True
    player_responses = []
    while response_needed:
        players_move = input("choose and type rock, paper, or scissors:").lower().strip()
        if players_move not in correct_response:
            print("Incorrect input. Please type either rock, paper, or scissors. Game starts again with player 1.")
            player_responses.clear()
            continue
        else:
            player_responses.append(players_move)

        if len(player_responses)<2:
            print("Next player's turn")
        else:
            response_needed = False

    player_1_play, player_2_play = player_responses
    
    if not player_1_play==player_2_play:
        if player_1_play=="rock":
            print("Congratulations", "player 1" if player_2_play=="scissors" else "player 2")
        elif player_1_play=="paper":
            print("Congratulations", "player 1" if player_2_play=="rock" else "player 2")
        else:
            print("Congratulations", "player 1" if player_2_play=="paper" else "player 2")
    else:
        print("The game is a draw")

    if input("type yes to start new game or no to stop the game:").lower().strip()!="yes":
        break
print("Game ended")
