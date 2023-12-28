def trifuerza(nivel:int):
    longitud = 2*nivel

    n = 1
    while (n != nivel+1):
        linea = '*'*(2*n-1)
        linea=linea.center(longitud*2)
        print(linea)
        n+=1

    n = 1
    while (n != nivel+1):
        linea = '*' *(2*n-1)
        linea=linea.center(longitud) + linea.center(longitud)
        print(linea)
        n+=1

trifuerza(10)