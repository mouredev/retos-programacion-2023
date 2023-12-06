def rock_paper_scissor_lizard_spock(games):

    rules = {
    "rock": ("scissor", "lizard"),
    "paper": ("rock", "spock"),
    "scissor": ("paper", "lizard"),
    "lizard": ("paper", "spock"),
    "spock": ("rock", "scissor")
    }

    player_one = 0
    player_two = 0

    for game in games:
        player_one_game = game[0]
        player_two_game = game[1]
        if player_one_game != player_two_game:
            if player_two_game in rules[player_one_game]:
                player_one += 1
            else:
                player_two += 1

    return "Tie" if player_one == player_two else "Player 1" if player_one > player_two else "Player 2"


print(rock_paper_scissor_lizard_spock([("rock", "paper"), ("spock", "lizard"), ("scissor", "rock")]))
print(rock_paper_scissor_lizard_spock([("paper", "paper"), ("spock", "spock"), ("scissor", "scissor")]))
print(rock_paper_scissor_lizard_spock([("paper", "paper"), ("spock", "spock"), ("scissor", "paper")]))
