"""
¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 

Crea un programa que dibuje una Trifuerza de "Zelda"
formada por asteriscos.
- Debes indicarle el número de filas de los triángulos con un entero positivo (n).
- Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.

Ejemplo: Trifuerza 2

   *
  ***
 *   *
*** ***
"""

def draw_triforce(n: int) -> str:
    """
    Genera una Trifuerza inspirada en "The Legend of Zelda" utilizando asteriscos.

    La Trifuerza está compuesta por tres triángulos equiláteros:
    uno superior y dos en la base. Cada triángulo tiene como fila más ancha
    la longitud calculada con la fórmula ``2n - 1``.

    Args:
        n (int): Número de filas de cada triángulo. Debe ser un entero positivo.

    Returns:
        str: El patrón de la Trifuerza en forma de cadena.

    Raises:
        TypeError: Si el valor proporcionado no es un entero.
        ValueError: Si el número es negativo.
    """
    if not isinstance(n, int):
        raise TypeError("Solo se admiten enteros positivos.")
    if n <= 0:
        raise ValueError("El número de filas debe ser un entero positivo.")

    lines = []
    for i in range(n):
        lines.append(" " * (2 * n - i - 1) + "*" * (2 * i + 1))
    for i in range(n):
        left = " " * (n - i - 1) + "*" * (2 * i + 1)
        right = "*" * (2 * i + 1)
        middle = " " * (2 * (n - i) - 1)
        lines.append(f"{left}{middle}{right}")

    return "\n".join(lines)


if __name__ == "__main__":
    print(draw_triforce(5))
