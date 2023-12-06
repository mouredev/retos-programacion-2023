def abaco(tablero:list)->int:
    number = 0
    unidad = 1
    for row in list(reversed(tablero)):
        number += len(row.split('---')[0])*unidad
        unidad *= 10

    return number

if __name__ == "__main__":
    tablero_1 = ["O---OOOOOOOO",
              "OOO---OOOOOO",
              "---OOOOOOOOO",
              "OO---OOOOOOO",
              "OOOOOOO---OO",
              "OOOOOOOOO---",
              "---OOOOOOOOO"]
    
    print(abaco(tablero_1))
