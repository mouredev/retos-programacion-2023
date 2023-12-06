def game(sequence):
    player1 = 0
    player2 = 0

    combinations = {
        "🗿": "✂🦎",
        "📄": "🗿🖖",
        "✂":  "🦎📄",
        "🦎": "📄🖖",
        "🖖": "✂🗿"
    }

    for attempt in sequence:
        if attempt[0] not in combinations or attempt[1] not in combinations:
            return "Jugada no valida"
            
        if attempt[1] in combinations[attempt[0]]:
            player1 += 1
        
        elif attempt[0] in combinations[attempt[1]]:
            player2 += 1
    
    return "Tie" if player1 == player2 else "Player 1" if player1 > player2 else "Player 2"


print(game([["🖖", "📄"], ["🖖", "📄"], ["🗿", "🦎"]]))
print(game([["🗿", "✂"],  ["🖖", "✂"],  ["📄", "🦎"]]))
print(game([["🖖", "🖖"], ["🖖", "🗿"], ["✂", "🖖"]]))
