# El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
#  *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
#  - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".

def game(plays):
    
    rock = "🗿"
    scissors = "✂️"
    paper = "📄"
    lizard = "🦎"
    spock = "🖖"
    P1_points = 0
    P2_points = 0
    
    for i in plays:
        if i[0] == rock:
            if i[1] == scissors or i[1] == lizard:
                P1_points += 1
            elif i[1] == paper or i[1] == spock:
                P2_points += 1
            else: 
                return "Datos no validos"
        elif i[0] == scissors:
            if i[1] == rock or i[1] == spock:
                P2_points += 1
            elif i[1] == paper or i[1] == lizard:
                P1_points += 1
            else: 
                return "Datos no validos"
        elif i[0] == paper:
            if i[1] == rock or i[1] == spock:
                P1_points += 1
            elif i[1] == scissors or i[1] == lizard:
                P2_points += 1
            else: 
                return "Datos no validos"
        elif i[0] == lizard:
            if i[1] == rock or i[1] == scissors:
                P2_points += 1
            elif i[1] == paper or i[1] == spock:
                P1_points += 1
            else: 
                return "Datos no validos"
        elif i[0] == spock:
            if i[1] == rock or i[1] == scissors:
                P1_points += 1
            elif i[1] == paper or i[1] == lizard:
                P2_points += 1
            else: 
                return "Datos no validos"
        else: 
            return "Datos no validos"
    
    if P1_points > P2_points:
        return "Player 1"
    elif P1_points < P2_points:
        return "Player 2"
    elif P1_points == P2_points:
        return "Empate"

print(game([("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]))
print(game([("🗿","✂️"), ("✂️","🗿"), ("📄","✂️"), ("🦎","🖖")]))
print(game([("🖖","🗿"), ("✂️","🗿"), ("🗿","✂️"), ("🦎","🖖")]))
print(game([("🖖","🗿"), ("✂️","🗿"), ("🗿","😊"), ("🦎","🖖")]))
