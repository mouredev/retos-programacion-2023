def trifuerza(filas:int)->None:
    for nivel in range(1,filas+1):
        print(' '*(filas*2-nivel) + '*'*(2 * nivel-1))

    for nivel in range(1,filas+1):
        print(' '*(filas-nivel) + '*'*(2 * nivel-1) + ' ' * (filas-nivel) + ' '*(filas-nivel+1) + '*'*(2 * nivel-1))

if __name__ == '__main__':
    trifuerza(4)
