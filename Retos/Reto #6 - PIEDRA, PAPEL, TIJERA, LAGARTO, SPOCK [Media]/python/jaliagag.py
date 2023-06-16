##
## Crea un programa que calcule quien gana más partidas al piedra,
## papel, tijera, lagarto, spock.
## - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
## - La función recibe un listado que contiene pares, representando cada jugada.
## - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
##   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
## - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
## - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
##/

result = 0

def check(data):
    e = [data['player1'],data['player2']]
    if e[0] == e[1]:
        print('Tie')
        return 0
    if e[0] == 2 and e[1] == 1 \
        or e[0] == 1 and e[1] == 2:
        print('tijera corta papel')
        if e[0] == 2:
            print('Player 1')
        else:
            print('Player 2')
        return 1
    if e[0] == 1 and e[1] == 0 \
        or e[0] == 0 and e[1] == 1:
        print('piedra cubre papel')
        if e[0] == 1:
            print('Player 1')
        else:
            print('Player 2')
        return 1
    if e[0] == 0 and e[1] == 3 \
        or e[0] == 3 and e[1] == 0:
        print('piedra aplasta lagarto')
        if e[0] == 1:
            print('Player 1')
        else:
            print('Player 2')
        return 1
    if e[0] == 3 and e[1] == 4 \
        or e[0] == 4 and e[1] == 3:
        print('lagarto envenena a spock')
        if e[0] == 1:
            print('Player 1')
        else:
            print('Player 2')
        return 1
    if e[0] == 4 and e[1] == 2 \
        or e[0] == 2 and e[1] == 4:
        print('spock destroza tijeras')
        if e[0] == 1:
            print('Player 1')
        else:
            print('Player 2')
        return 1
    if e[0] == 2 and e[1] == 3 \
        or e[0] == 3 and e[1] == 2:
        print('tijeras decapita lagarto')
        if e[0] == 1:
            print('Player 1')
        else:
            print('Player 2')
        return 1
    if e[0] == 3 and e[1] == 1 \
        or e[0] == 1 and e[1] == 3:
        print('lagarto come papel')
        if e[0] == 1:
            print('Player 1')
        else:
            print('Player 2')
        return 1
    if e[0] == 1 and e[1] == 4 \
        or e[0] == 4 and e[1] == 1:
        print('papel desacredita a spock')
        if e[0] == 1:
            print('Player 1')
        else:
            print('Player 2')
        return 1
    if e[0] == 4 and e[1] == 0 \
        or e[0] == 0 and e[1] == 4:
        print('spock vaporiza piedra')
        if e[0] == 1:
            print('Player 1')
        else:
            print('Player 2')
        return 1
    if e[0] == 0 and e[1] == 2 \
        or e[0] == 2 and e[1] == 0:
        print('piedra aplasta tijeras')
        if e[0] == 1:
            print('Player 1')
        else:
            print('Player 2')
        return 1
    return 0

def play():
    opciones = {0: 'piedra', 1: 'papel', 2: 'tijera', 3: 'lagarto', 4: 'spock'}
    print('opciones numéricas:', opciones)
    a = int(input('jugada: '))
    return a

while result == 0:
    data = {'player1': '', 'player2': ''}
    data['player1'] = play()
    data['player2'] = play()
    
    result = check(data)


#if __name__ == '__main__':