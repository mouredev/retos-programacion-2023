def jugar_partida(jugadas: list[tuple]) -> str:
    reglas = {
        '🗿': {'✂️', '🦎'},
        '✂️': {'📄', '🦎'},
        '📄': {'🗿', '🖖'},
        '🦎': {'📄', '🖖'},
        '🖖': {'✂️', '🗿'}
    }

    p1, p2 = 0, 0
    for jugada in jugadas:
        if jugada[1] in reglas[jugada[0]]:
            p1 += 1
        else:
            p2 += 1

    if p1 > p2:
        result = 'Player 1'
    elif p2 > p1:
        result =  'Player 2'
    else:
        result = 'Tie'

    return result

print(jugar_partida([('🗿', '✂️'), ('🖖', '🗿'), ('📄', '✂️')]))
