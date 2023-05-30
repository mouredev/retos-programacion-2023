# Reto #22: La espiral
#### Dificultad: Media | Publicación: 29/05/23 | Corrección: 06/06/23

## Enunciado

#
# Crea una función que dibuje una espiral como la del ejemplo.
# - Únicamente se indica de forma dinámica el tamaño del lado.
# - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
#
# Ejemplo espiral de lado 5 (5 filas y 5 columnas):
# ════╗
# ╔══╗║
# ║╔╗║║
# ║╚═╝║
# ╚═══╝
#

class Figura:
    def __init__(self, lado):
        self.lado = lado


class Espiral:
    def __init__(self, figura):
        self.figura = figura

    def generar(self):
        lado = self.figura.lado
        lados = ""
        for i in range((lado + 1) // 2):
            if i == 0:
                lados += "═" * (lado - 1) + "╗\n"
            else:
                lados += "║" * (i - 1) + "╔" + "═" * (lado - (2 * i) - 1) + "╗" + "║" * i + "\n"

        for i in range((lado + 1) // 2, lado):
            lados += "║" * (lado - i - 1) + "╚" + "═" * ((2 * i) - lado) + "╝" + "║" * (lado - i - 1) + "\n"

        return lados


if __name__ == "__main__":
    figura = Figura(int(input("Número de filas y columnas: ")))
    espiral = Espiral(figura)
    print(espiral.generar())


