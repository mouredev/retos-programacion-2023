def rock_paper_scissors_lizard_spock(games):
    #Variables
    player_1 = 0
    player_2 = 0
    rules = {"🗿":["✂️","🦎"],
            "✂️":["📄","🦎"],
            "📄":["🗿","🖖"],
            "🦎":["🖖","📄"],
            "🖖":["✂️","🗿"]}

    #Recorremos la lista de juegos
    for game in games:
        #Si los valores no son iguales, miramos si lo jugado por el jugador 2 esta en el valor de la llave de lo jugado por el jugador 1
        if game[0] != game[1]:
            #Si la llave del diccionario (lo jugado por el jugador 1) contiene lo jugado por el jugador 2, gana jugador 1, si no gana jugador 2
            if game[1] in rules[game[0]]:
                player_1 += 1
            else:
                player_2 += 1
        #En caso de que ambos saquen el mismo valor no suman ningún punto
        else:
            player_1 += 0
            player_2 += 0
    
    #Comparamos cúal de los dos jugadores tiene más puntos o si han empatado
    if player_1 > player_2:
        return "Player 1"
    elif player_1 < player_2:
        return "Player 2"
    else:
        return "Tie"

print(rock_paper_scissors_lizard_spock([("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]))
print(rock_paper_scissors_lizard_spock([("🗿","✂️"), ("✂️","🗿"), ("📄","✂️"), ("🦎","🖖")]))
print(rock_paper_scissors_lizard_spock([("🖖","✂️"), ("📄","🗿"), ("🦎","✂️"), ("🦎","🦎"), ("🦎","🖖")]))