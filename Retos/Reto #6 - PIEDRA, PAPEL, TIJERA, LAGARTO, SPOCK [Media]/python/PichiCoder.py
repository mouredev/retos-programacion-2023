def piedra_Papel_Tijera_Lagarto_Spock(*entrada):
    player1 = 0
    player2 = 0
    
    for choices in entrada:
        for choice in choices:
            if choice[0] == choice[1]: continue
            elif choice[0] == "✂️" and (choice[1] == "🦎" or choice[1] == "📄"): player1 += 1
            elif choice[0] == "📄" and (choice[1] == "🗿" or choice[1] == "🖖"): player1 += 1
            elif choice[0] == "🗿" and (choice[1] == "✂️" or choice[1] == "🦎"): player1 += 1
            elif choice[0] == "🦎" and (choice[1] == "🖖" or choice[1] == "📄"): player1 += 1
            elif choice[0] == "🖖" and (choice[1] == "✂️" or choice[1] == "🗿"): player1 += 1
            else: player2 += 1
    
    if player1 == player2: return "Tie"
    elif player1 > player2: return "Player 1"
    else: return "Player 2"
