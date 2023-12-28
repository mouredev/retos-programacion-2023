def calculate_winner(plays):
    results = {
        "🗿": {
            "✂️": 1,
            "🦎": 1,
            "📄": 0,
            "🖖": 0
        },
        "📄": {
            "🗿": 1,
            "🖖": 1,
            "✂️": 0,
            "🦎": 0
        },
        "✂️": {
            "📄": 1,
            "🦎": 1,
            "🗿": 0,
            "🖖": 0
        },
        "🦎": {
            "📄": 1,
            "🖖": 1,
            "🗿": 0,
            "✂️": 0
        },
        "🖖": {
            "🗿": 1,
            "✂️": 1,
            "📄": 0,
            "🦎": 0
        }
    }

    player1_wins = 0
    player2_wins = 0

    for play in plays:
        player1, player2 = play

        if player1 == player2:
            continue
        elif results[player1][player2] == 1:
            player1_wins += 1
        else:
            player2_wins += 1

    if player1_wins > player2_wins:
        return "Player 1"
    elif player2_wins > player1_wins:
        return "Player 2"
    else:
        return "Tie"
