"""
 * Crea una función que dibuje una espiral como la del ejemplo.
 * - Únicamente se indica de forma dinámica el tamaño del lado.
 * - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
 *
 * Ejemplo espiral de lado 5 (5 filas y 5 columnas):
 * ════╗
 * ╔══╗║
 * ║╔╗║║
 * ║╚═╝║
 * ╚═══╝
"""

SYMBOLS = {
    "horizontal": "═",
    "vertical": "║",
    "corner_up_right": "╗",
    "corner_up_left": "╔",
    "corner_down_right": "╝",
    "corner_down_left": "╚"
}


def draw_spiral(side):
    if (side < 2):
        print(f"Can't draw a {side}x{side} spiral.\n")
    else:
        spiral = generate_spiral(side)
    
        spiral_str = ""
        for row in spiral:
            spiral_str += "".join(row)
            spiral_str += "\n"
    
        print(f"{side}x{side} spiral:\n" + spiral_str)


def generate_spiral(side):
    half_spiral = int(side / 2)


    def generate_half_spiral(corner_left, corner_right, is_down=False):
        spiral = []

        for row in range(half_spiral):
            row_table = []
            for col in range(side):
                if row == 0:
                    if (is_down and col == 0): row_table.append(corner_left)
                    elif (col == side-1): row_table.append(corner_right)
                    else: row_table.append(SYMBOLS["horizontal"])
                else:
                    if ((spiral[row-1][col] == SYMBOLS["horizontal"]) and
                        (spiral[row-1][col-1] == corner_left or
                         spiral[row-1][col-1] == corner_right)):
                        row_table.append(corner_left)
                    else:
                        row_table.append(SYMBOLS["vertical"])

                    if (spiral[row-1][col] == corner_right):
                        row_table[col-1] = corner_right

            if corner_left in row_table:
                start = row_table.index(corner_left) + 1
                end = row_table.index(corner_right)

                for symbol in range(start, end):
                    row_table[symbol] = SYMBOLS["horizontal"]

            spiral.append(row_table)

        return spiral


    # generate: upper half spiral

    spiral = generate_half_spiral(
        SYMBOLS["corner_up_left"],
        SYMBOLS["corner_up_right"]
    )

    # generate: middle row (only if side is odd)

    if (side % 2 != 0):
        row_table = []
        
        for _ in range(len(spiral) - 1):
            row_table.append(SYMBOLS["vertical"])

        row_table.append(SYMBOLS["corner_up_left"])
        row_table.append(SYMBOLS["corner_up_right"])

        for _ in range(side - len(row_table)):
            row_table.append(SYMBOLS["vertical"])

        spiral.append(row_table)

    # generate: down half spiral

    down_spiral = generate_half_spiral(
        SYMBOLS["corner_down_left"],
        SYMBOLS["corner_down_right"],
        True
    )
    down_spiral.reverse()

    # complete spiral

    for row in down_spiral:
        spiral.append(row)

    return spiral


draw_spiral(1)
draw_spiral(5)
draw_spiral(10)