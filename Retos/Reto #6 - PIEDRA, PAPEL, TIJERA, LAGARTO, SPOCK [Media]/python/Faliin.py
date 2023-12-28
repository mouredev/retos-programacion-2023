def who_wins_more(plays):
    player1_score = 0
    player2_score = 0
    for play in plays:
        if play[0] == "🗿" and (play[1] == "✂️" or play[1] == "🦎"):
            player1_score += 1
        elif play[0] == "📄" and (play[1] == "🗿" or play[1] == "🖖"):
            player1_score += 1
        elif play[0] == "✂️" and (play[1] == "📄" or play[1] == "🦎"):
            player1_score += 1
        elif play[0] == "🦎" and (play[1] == "📄" or play[1] == "✂️"):
            player1_score += 1
        elif play[0] == "🖖" and (play[1] == "🗿" or play[1] == "✂️"):
            player1_score += 1
        elif play[1] == "🗿" and (play[0] == "✂️" or play[0] == "🦎"):
            player2_score += 1
        elif play[1] == "📄" and (play[0] == "🗿" or play[0] == "🖖"):
            player2_score += 1
        elif play[1] == "✂️" and (play[0] == "📄" or play[0] == "🦎"):
            player2_score += 1
        elif play[1] == "🦎" and (play[0] == "📄" or play[0] == "✂️"):
            player2_score += 1
        elif play[1] == "🖖" and (play[0] == "🗿" or play[0] == "✂️"):
            player2_score += 1

    if player1_score > player2_score:
        return "Player 1"
    elif player1_score < player2_score:
        return "Player 2"
    else:
        return "Tie"

plays = [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]
print(who_wins_more(plays))
