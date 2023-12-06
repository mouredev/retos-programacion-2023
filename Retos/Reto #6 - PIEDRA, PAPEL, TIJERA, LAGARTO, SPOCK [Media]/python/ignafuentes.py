def juego(jugadas):
    
    reglas = {
        '🗿':{
            '✂️': 1,
            '🦎': 1,
            '📄': 0,
            '🖖': 0,
        },
        '📄':{
            '🗿': 1,
            '🖖': 1,
            '✂️': 0,
            '🦎': 0,
        },
        '✂️':{
            '🦎': 1,
            '📄': 1,
            '🖖': 0,
            '🗿': 0,
        },
        '🦎':{
            '📄': 1,
            '🖖': 1,
            '✂️': 0,
            '🗿': 0,
        },
        '🖖':{
            '✂️': 1,
            '🗿': 1,
            '📄': 0,
            '🦎': 0,
        }
    }

    jugador_uno = 0
    jugador_dos = 0

    for eleccion in jugadas:

        if eleccion[0] == eleccion[1]:
            continue
        elif reglas[eleccion[0]][eleccion[1]] == 1:
            jugador_uno += 1
        else:
            jugador_dos += 1
        
    if jugador_uno == 2:
        print('Player 1')
    elif jugador_dos == 2: 
        print('Player 2')
    else:
        print('Tie')

juego([("🗿","🦎"), ("✂️","🖖"), ("📄","✂️")])