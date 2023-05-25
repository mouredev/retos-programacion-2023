def dibujar_trifuerza(n):
    fila_mayor = 2*n - 1
    espacios = fila_mayor // 2

    for i in range(n):
        for j in range(espacios):
            print(" ", end="")
        for j in range(2*i+1):
            print("*", end="")
        for j in range(espacios):
            print(" ", end="")
        print()

        espacios -= 1

    espacios = 1
    for i in range(n):
        for j in range(espacios):
            print(" ", end="")
        for j in range(fila_mayor - 2*i):
            print("*", end="")
        for j in range(espacios):
            print(" ", end="")
        print()

        espacios += 1

dibujar_trifuerza(2)
