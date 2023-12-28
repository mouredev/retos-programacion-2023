def resultadoJuego(marcador):
    points1 = 0
    points2 = 0

    rules = {
        "🗿": ["✂️", "🦎"],
        "📄": ["🗿", "🖖"],
        "✂️": ["📄", "🦎"],
        "🦎": ["🖖", "📄"],
        "🖖": ["🗿", "✂️"]
    }

    for player1, player2 in marcador:
        if player1 == player2:
            continue
        
        if player1 in rules[player2]:
            points2 += 1
        else:
            points1 += 1

    print("Tie" if points1 == points2 else "Ganador jugador 1" if points1 > points2 else "Ganador jugador 2")


resultadoJuego([("🗿","✂️"), ("✂️","🗿"), ("✂️","📄"), ("✂️","📄")])
