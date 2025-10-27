"""
Crea una función que dibuje una espiral como la del ejemplo.
- Únicamente se indica de forma dinámica el tamaño del lado.
- Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚

Ejemplo espiral de lado 5 (5 filas y 5 columnas):
════╗
╔══╗║
║╔╗║║
║╚═╝║
╚═══╝
""" 

def draw_spiral(size: int) -> None:
    """
    Dibuja una espiral cerrada de tamaño N x N usando caracteres de dibujo de cajas permitidos.

    La espiral comienza en la esquina superior izquierda y se mueve continuamente hacia adentro.

    Args:
        size (int): La longitud del lado (número de filas y columnas) de la espiral cuadrada. 
                Debe ser un entero positivo.

    Raises:
        ValueError: Si 'size' no es un entero positivo.
    """
    if not isinstance(size, int) or size < 1:
        raise ValueError("El tamaño debe ser un entero positivo.")

    spiral = [[' ' for _ in range(size)] for _ in range(size)]
    top, bottom, left, right = 0, size - 1, 0, size - 1

    while True:
        if left > right or top > bottom:
            break

        for i in range(left, right + 1):
            spiral[top][i] = '═'
        if top < bottom:
            spiral[top][right] = '╗'
        top += 1
        if top > bottom:
            break

        for i in range(top, bottom + 1):
            spiral[i][right] = '║'
        if left < right:
            spiral[bottom][right] = '╝'
        right -= 1
        if left > right:
            break

        for i in range(right, left - 1, -1):
            spiral[bottom][i] = '═'
        if top <= bottom:
            spiral[bottom][left] = '╚'
        bottom -= 1
        if top > bottom:
            break

        for i in range(bottom, top - 1, -1):
            spiral[i][left] = '║'
        if left <= right:
            spiral[top][left] = '╔'
        left += 1

    for row in spiral:
        print(''.join(row))


if __name__ == "__main__":
    draw_spiral(8)
