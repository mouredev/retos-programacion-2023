def tetris():
    
    tablero = ["1000000000",
                "1110000000",
                "0000000000",
                "0000000000",
                "0000000000",
                "0000000000",
                "0000000000",
                "0000000000",
                "0000000000",
                "0000000000"]
    
    for fila in tablero:
            for pieza in fila:
                print("🔳", end="") if pieza == "1" else print("🔲", end="")
            print()

    while True:
        
        movimiento = input("ingrese un movimiento (abajo ,derecha, arriba, izquierda, rotar): ")

        if movimiento == "abajo":
            tablero.insert(0, tablero.pop(9))

        elif movimiento == "arriba":
            tablero.insert(9, tablero.pop(0))
        
        elif movimiento == "derecha":
            for fila in range(len(tablero[0])):
                tablero1 = list(tablero[fila])
                tablero1.insert(0, tablero1.pop(9))
                tablero[fila] = tablero1

        elif movimiento == "izquierda":
            for fila in range(len(tablero[0])):
                tablero1 = list(tablero[fila])
                tablero1.insert(9, tablero1.pop(0))
                tablero[fila] = tablero1
        elif movimiento == "rotar":
            tablero = list(zip(*tablero[::1]))
        
        for fila in tablero:
            for pieza in fila:
                print("🔳", end="") if pieza == "1" else print("🔲", end="")
            print()
    

tetris()