#  * Crea una función que dibuje una espiral como la del ejemplo.
#  * - Únicamente se indica de forma dinámica el tamaño del lado.
#  * - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
#  *
#  * Ejemplo espiral de lado 5 (5 filas y 5 columnas):
#  * ════╗
#  * ╔══╗║
#  * ║╔╗║║
#  * ║╚═╝║
#  * ╚═══╝
#  */
def dibujar_espiral(lado):
    matriz = [[' '] * lado for _ in range(lado)]

    fila_inicio = 0
    fila_fin = lado - 1
    columna_inicio = 0
    columna_fin = lado - 1
    direccion = 0

    while fila_inicio <= fila_fin and columna_inicio <= columna_fin:
        if direccion == 0:
            for i in range(columna_inicio, columna_fin + 1):
                matriz[fila_inicio][i] = '═'
            fila_inicio += 1
        elif direccion == 1:
            for i in range(fila_inicio, fila_fin + 1):
                matriz[i][columna_fin] = '║'
            columna_fin -= 1
        elif direccion == 2:
            for i in range(columna_fin, columna_inicio - 1, -1):
                matriz[fila_fin][i] = '═'
            fila_fin -= 1
        elif direccion == 3:
            for i in range(fila_fin, fila_inicio - 1, -1):
                matriz[i][columna_inicio] = '║'
            columna_inicio += 1

        direccion = (direccion + 1) % 4

    for fila in matriz:
        print(''.join(fila))
lado = 5
dibujar_espiral(lado)