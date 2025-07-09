xlist = ['🪨','📃','✂️','🦎','🖖']
sets = []

for i in range(len(xlist)):
    for k in range(i+1, len(xlist)):
        comb = {xlist[i],xlist[k]}
        sets.append(comb)

rule = {
    frozenset(sets[0]): "📃",
    frozenset(sets[1]): "🪨",
    frozenset(sets[2]): "🪨",
    frozenset(sets[3]): "🖖",
    frozenset(sets[4]): "✂️",
    frozenset(sets[5]): "🦎",
    frozenset(sets[6]): "📃",
    frozenset(sets[7]): "✂️",
    frozenset(sets[8]): "🖖",
    frozenset(sets[9]): "🦎"
}

def game(move: tuple):
    set = frozenset(move)

    try:
        if rule[set] == move[0]:
            return 'p1'
        elif rule[set] == move[1]:
            return 'p2'
    except KeyError:
        return 'tie'

def main():
    sec = []
    xp1 = 0
    xp2 = 0

    while True:
        user_input = input("Ingresa una secuencia de juego separada por , (0 para terminar)")

        if user_input == "0":
            break
        else:
            sec.append(tuple(user_input.split(',')))
    
    for move in sec:
        if game(move) == 'p1':
            xp1 += 1
        if game(move) == 'p2':
            xp2 += 1
        if game(move) == 'tie':
            continue
    
    if xp1 > xp2:
        print("Player 1")
    elif xp2 > xp1:
        print("Player 2")
    else:
        print("Tie")
    
main()