def trifuerza(level):
    tamaño = 2 * level

    n = 1
    while (n != level + 1):
        linea = '*' * ( 2 * n-1)
        linea=linea.center(tamaño*2)
        print(linea)
        n += 1

    n = 1
    while (n != level + 1):
        linea = '*' * ( 2 * n-1)
        linea = linea.center(tamaño) + linea.center(tamaño)
        print(linea)
        n += 1

trifuerza(2)