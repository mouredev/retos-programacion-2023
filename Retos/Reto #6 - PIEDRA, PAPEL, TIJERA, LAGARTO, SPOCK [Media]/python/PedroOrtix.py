def quien_gana(partidas):
    reglas = {
        ("🗿", "✂️"): 1,  # Piedra gana a tijera
        ("🗿", "🦎"): 1,  # Piedra gana a lagarto
        ("📄", "🗿"): 1,  # Papel gana a piedra
        ("📄", "🖖"): 1,  # Papel gana a spock
        ("✂️", "📄"): 1,  # Tijera gana a papel
        ("✂️", "🦎"): 1,  # Tijera gana a lagarto
        ("🦎", "📄"): 1,  # Lagarto gana a papel
        ("🦎", "🖖"): 1,  # Lagarto gana a spock
        ("🖖", "🗿"): 1,  # Spock gana a piedra
        ("🖖", "✂️"): 1,  # Spock gana a tijera
        ("🗿", "🗿"): 0,  # Empate
        ("📄", "📄"): 0,  
        ("✂️", "✂️"): 0,  
        ("🦎", "🦎"): 0,  
        ("🖖", "🖖"): 0   
    }

    # Contadores de victorias
    victorias_1 = 0
    victorias_2 = 0

    # Iteramos sobre las partidas
    for jugada_1, jugada_2 in partidas:
        # Si las jugadas son iguales, es un empate
        if jugada_1 == jugada_2:
            continue

        # Comprobamos quién gana según las reglas
        if (jugada_1, jugada_2) in reglas:
            victorias_1 += reglas[(jugada_1, jugada_2)]
        else:
            victorias_2 += reglas[(jugada_2, jugada_1)]

    # Devolvemos el resultado
    if victorias_1 > victorias_2:
        return "Player 1"
    elif victorias_2 > victorias_1:
        return "Player 2"
    else:
        return "Tie"


if __name__ == "__main__":
    ganador = quien_gana([("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")])
    print(ganador)