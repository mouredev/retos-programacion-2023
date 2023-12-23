"""/*
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
 */
"""


def get_size():
    try:
        return int(input("Tamaño: "))
    except ValueError:
        print("Introduce un entero")


def constructor(size):
    width = size
    height = size
    bricks = {
        "horizontal": "═",
        "vertical": "║",
        "esq-sup-izq": "╔",
        "esq-sup-der": "╗",
        "esq-inf-der": "╝",
        "esq-inf-izq": "╚",
    }
    create_matrix(width, height, bricks)


def create_matrix(width, height, bricks):
    print(f"{(bricks['horizontal']*width)}{bricks['esq-sup-der']}")
    for i in range(height - 5):
        print(" " * (width - 1), bricks["vertical"])
    print(
        f"{bricks['esq-sup-izq']}{(bricks['horizontal']*(width-2))}{bricks['esq-sup-der']}{bricks['vertical']}"
    )
    for i in range(height - 5):
        print(bricks["vertical"], " " * (width - 4), bricks["vertical"] * 2)
    print(
        f"{bricks['vertical']}{bricks['esq-sup-izq']}{(bricks['horizontal']*(width-4))}{bricks['esq-sup-der']}{bricks['vertical']}{bricks['vertical']}"
    )
    for i in range(height - 5):
        print(bricks["vertical"]*2, " " * (width - 6), bricks["vertical"]*3)
    print(
        f"{bricks['vertical']}{bricks['esq-inf-izq']}{(bricks['horizontal']*(width-3))}{bricks['esq-inf-der']}{bricks['vertical']}"
    )
    for i in range(height - 5):
        print(bricks["vertical"], " " * (width - 3), bricks["vertical"])
    print(
        f"{bricks['esq-inf-izq']}{(bricks['horizontal']*(width-1))}{bricks['esq-inf-der']}"
    )


def main():
    constructor(get_size())


if __name__ == "__main__":
    main()
