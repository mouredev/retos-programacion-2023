def jugar(entradas,player_1_name="Jugador 1",player_2_name="Jugador 2"):
    #Contadores
    player_1 = 0
    player_2 = 0
    
    #Reglas
    reglas = {
        "🗿" : ["✂️","🦎"],
        "✂️" : ["📄","🦎"],
        "📄" : ["🗿", "🖖"],
        "🦎" : ["📄","🖖"],
        "🖖" : ["🗿","✂️"]
    }
    
    #Iteracion de las partidas
    for entrada in entradas:
        if entrada[0] == entrada[1]:
            continue
        elif entrada[0] not in reglas[entrada[1]]:
            player_1 += 1
        else:
            player_2 += 1
    
    #Resultados 
    if player_1 > player_2:
        print(f"{player_1_name} ha ganado con {player_1} punto/s.")
    elif player_1 == player_2:
        print("Es un empate! ")
    else:
        print(f"{player_2_name} ha ganado con {player_2} punto/s.")

decisiones = [
    ("🗿", "✂️"),
    ("📄", "🗿"),
    ("🦎", "📄"),
    ("🖖", "🦎"),
    ("✂️", "🖖"),
    ("🖖", "📄"),
    ("📄", "🦎"),
    ("✂️", "🖖"),
    ("🖖", "🗿"),
    ("🦎", "✂️"),
    ("🗿", "📄"),
    ("✂️", "📄"),
    ("🗿", "🦎"),
    ("🦎", "🗿"),
    ("📄", "🖖"),
    ("🖖", "🗿"),
    ("🖖", "🦎"),
    ("📄", "✂️"),
    ("🦎", "✂️"),
    ("🗿", "🖖"),
    ("✂️", "🗿"),
    ("🖖", "🖖"),
    ("📄", "📄"),
    ("🦎", "🦎")
]

jugar(decisiones,"Nahuel","Carola")