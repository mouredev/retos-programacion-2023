def dibujar_espiral(lado):
    matriz = [[' '] * lado for _ in range(lado)]
    direccion = 0
    fila_inicio = 0
    fila_fin = lado - 1
    columna_inicio = 0
    columna_fin = lado - 1
    contador = 0

    while fila_inicio <= fila_fin and columna_inicio <= columna_fin:
        if direccion == 0:
            for i in range(columna_inicio, columna_fin + 1):
                if i == columna_fin:
                    matriz[fila_inicio][i] = '╗'
                else:
                    matriz[fila_inicio][i] = '═'
            fila_inicio += 1
        elif direccion == 1:
            for i in range(fila_inicio, fila_fin + 1):
                if i == fila_fin:
                    matriz[i][columna_fin] = '╝'
                else:
                    matriz[i][columna_fin] = '║'
            columna_fin -= 1
        elif direccion == 2:
            for i in range(columna_fin, columna_inicio - 1, -1):
                if i == columna_inicio:
                    matriz[fila_fin][i] = '╚'
                else:
                    matriz[fila_fin][i] = '═'
            fila_fin -= 1
        elif direccion == 3:
            for i in range(fila_fin, fila_inicio - 1, -1):
                if i == fila_inicio:
                    matriz[i][columna_inicio] = '╔'
                else:
                    matriz[i][columna_inicio] = '║'
            columna_inicio += 1

        direccion = (direccion + 1) % 4

    # Imprimir la matriz
    for fila in matriz:
        for elemento in fila:
            print(elemento, end='')
        print()

# Ejemplo de uso
dibujar_espiral(5)
