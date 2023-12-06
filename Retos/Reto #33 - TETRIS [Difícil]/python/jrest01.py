game = ["1000000000",
            "1110000000",
            "0000000000",
            "0000000000",
            "0000000000",
            "0000000000",
            "0000000000",
            "0000000000",
            "0000000000",
            "0000000000"]

def tetris(game):
    
    for row in game:
            for pixel in row:
                print("🔳", end="") if pixel == "1" else print("🔲", end="")
            print()
            
    while True:
        move = input("Ingrese un movimiento (abajo ,derecha, arriba, izquierda, rotar): ")
        
        if move == 'abajo':
            game.insert(0, game.pop(9))
        elif move == 'arriba':
            game.insert(9, game.pop(0))
        elif move == 'derecha':
            for row in range(10):
                new_row = list(game[row])
                new_row.insert(0, new_row.pop(9))
                game[row] = new_row
            # print(new_game)
        elif move == 'izquierda':
            for row in range(10):
                new_row = list(game[row])
                new_row.insert(9, new_row.pop(0))
                game[row] = new_row
                
        tetris(game)    
        
            
            
tetris(game)