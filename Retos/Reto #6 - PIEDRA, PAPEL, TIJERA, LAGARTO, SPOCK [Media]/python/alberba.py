def game(games: list):
    reglas = {"🗿": "✂️🦎", "✂️": "🦎📄", "🦎": "🖖📄", "📄": "🗿🖖", 
              "🖖": "✂️🗿"}
    wins_p1 = 0
    wins_p2 = 0
    for round in games:
        p1, p2 = round
        if p1 not in reglas.keys() or p2 not in reglas.keys():
            raise ValueError
        if p2 in reglas[p1]:
            wins_p1 += 1
        else:
            wins_p2 += 1
    
    print("Player 1") if wins_p1 > wins_p2 else print("Player 2") \
                     if wins_p2 > wins_p1 else print("Empate")

game([("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")])