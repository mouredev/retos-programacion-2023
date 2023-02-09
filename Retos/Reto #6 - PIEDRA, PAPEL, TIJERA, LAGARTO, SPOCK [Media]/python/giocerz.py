def winner(lista):
    reglas = {"🗿":[1,0,-1,1,1,-1], "📄":[2,1,0,-1,-1,1], "✂️": [3,-1,1,0,1,-1], "🦎":[4,-1,1,-1,0,1], "🖖":[5,1,-1,1,-1,0]}
    p1 = 0
    p2 = 0
    for elementos in lista:
        elemento1 = elementos[0]
        elemento2 = reglas[elementos[1]][0]
        result = reglas[elemento1][elemento2]
        if result == 1:
            p1 +=1
        elif result == -1:   
            p2 +=1
    if p1>p2:
        return "Player 1"
    elif p2>p1:
        return "Player 2"
    else:
        return "Tie"    

