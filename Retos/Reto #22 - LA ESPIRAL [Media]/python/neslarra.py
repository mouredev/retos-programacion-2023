r"""
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

def create_spiral(side_size: int):

    def add_after_top(side_size, line):
        return "║" * (line - 1) + "╔" + "═" * (side_size - (2 * line + 1)) + "╗" + "║" * line

    def add_before_bottom(side_size, line):
        return "║" * (side_size - 1 - line) + "╚" + "═" * (2 * line - side_size) + "╝" + "║" * (side_size - 1 - line)

    liner = ["═" * (side_size - 1) + "╗"]                # TOP
    for line in range(1, side_size - 1):
        if line < side_size / 2:
            liner.append(add_after_top(side_size, line))
        else:
            liner.append(add_before_bottom(side_size, line))
    liner.append("╚" + "═" *  (side_size - 2) + "╝")     # BOTTOM
    return liner


for line in create_spiral(15):
    print(line)
