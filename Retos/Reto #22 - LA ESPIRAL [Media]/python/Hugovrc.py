def dibuja_espiral(num):
    
    for fila in range (0, num):
        spiral = ""
        barra_horizontal = fila == 0
        for columna in range(0, num):
            if fila + columna == num - 1:
                if columna >= fila:
                    spiral += "╗"
                    barra_horizontal = False
                else:
                    spiral += "╚"
                    barra_horizontal = True
            elif fila - columna == 1 and fila < num / 2:
                spiral += "╔"
                barra_horizontal = True
            elif fila == columna and fila > num / 2:
                spiral += "╝"
                barra_horizontal = False
            else:
                if barra_horizontal == True:
                    spiral += "═"        
                else:
                    spiral += "║"
                
        print(spiral)

dibuja_espiral(9)
dibuja_espiral(5)