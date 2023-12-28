def reglas(jugado):
    options=["🗿","📄","✂️","🦎","🖖"]
    points=[0,0,0,0,0]
    if jugado[0]!=jugado[1]:
        if jugado[0]==options[0]:
            points=[0,0,1,1,0]
        elif jugado[0]==options[1]:
            points=[1,0,0,0,1]
        elif jugado[0]==options[2]:
            points=[0,1,0,1,0]
        elif jugado[0]==options[3]:
            points=[0,1,0,0,1]
        elif jugado[0]==options[4]:
            points=[1,0,1,0,0]
        return points[options.index(jugado[1])]
    else:
        return 2

def piedra_papel_tijera_lagarto_spock(listado):
    player1_points=0
    player2_points=0
    for i in listado:
        if reglas(i)==0:
            player2_points+=1
        elif reglas(i)==1:
            player1_points+=1
    print('Tie' if player1_points==player2_points else 'Player 1' if player1_points>player2_points else 'Player 2')

piedra_papel_tijera_lagarto_spock([("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")])
piedra_papel_tijera_lagarto_spock([("🗿","🖖"), ("🖖","🗿"), ("🦎","✂️"),("🗿","✂️")])
piedra_papel_tijera_lagarto_spock([("🗿","🖖"), ("🖖","🗿"), ("🦎","✂️"),("🗿","✂️"),("🦎","🖖"),("✂️","📄")])