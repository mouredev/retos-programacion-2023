# /*
# *	¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible!
# *
# * Crea un programa que dibuje una Trifuerza de "Zelda"
# * formada por asteriscos.
# * - Debes indicarle el número de filas de los triángulos con un entero positivo(n).
# * - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
# *
# * Ejemplo: Trifuerza 2
# *
# * *
# * ***
# * * *
# * *** ***
# *
# */

# /**
# * Funcion que calcula e imprime la trifuerza de Zelda de form recursiva
# * @ param level Nivel de la trifuerza
# * @ param currentLevel Nivel actual de la trifuerza(por defecto 0)
# */
def triforce_recursive(level, current_level=0):
    if current_level == level * 2:
        return

    row = ""
    first_level = level * 2 - 1
    second_level = 0

    if current_level < level:
        row = " " * (first_level - current_level)
        row += print_point(current_level)
    else:
        second_level = current_level - level
        row = " " * ((level - second_level) - 1)
        row += print_point(second_level)
        row += " " * (2 * (level - second_level) - 1)
        row += print_point(second_level)

    print(row)

    triforce_recursive(level, current_level + 1)


# /**
# * Función que imprime los puntos de la trifuerza
# * @ param level Nivel de la trifuerza
# */
def print_point(level):
    return "*" * (2 * level + 1)


triforce_recursive(7)
