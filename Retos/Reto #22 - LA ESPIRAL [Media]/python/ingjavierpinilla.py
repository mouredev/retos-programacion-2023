def dibujar_espiral(lado):
    matriz = [["║" for _ in range(lado)] for _ in range(lado)]

    for i, row in enumerate(matriz):
        if i < lado // 2:
            inicio = i
            limite = len(row) - (i + 1)
        else:
            inicio = lado - (i + 1)
            limite = len(row) - (inicio + 1)

        for j in range(inicio, limite):
            row[j] = "═"

        if lado % 2 != 0:
            if i <= lado // 2:  # impar
                row[-(i + 1)] = "╗"
                row[(i - 1)] = "╔" if i > 0 else row[(i - 1)]

            else:
                row[-(i + 1)] = "╚"
                row[i] = "╝"

        else:
            if i < lado // 2:  # par
                row[-(i + 1)] = "╗"
                row[(i - 1)] = "╔" if i > 0 else row[(i - 1)]
            else:
                row[-(i + 1)] = "╚"
                row[i] = "╝"

    for row in matriz:
        print("".join(row))


# Ejemplo de uso
for i in range(10):
    print(f"i:{i} " + "**" * 20)
    dibujar_espiral(i)
