# Reto #20: La Trifuerza
# Dificultad: Media | Publicación: 15/05/23 | Corrección: 22/05/23

# Enunciado

#
#	¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
#
# Crea un programa que dibuje una Trifuerza de "Zelda"
# formada por asteriscos.
# - Debes indicarle el número de rows de los triángulos con un entero positivo (n).
# - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
#
# Ejemplo: Trifuerza 2
# 
#    *
#   ***
#  *   *
# *** ***
#
#
class Zelda:
    def __init__(self, rows):
        self.rows = rows
        self.lenght_row = 2 * rows

    def print_triangles(self):
        for n in range(1, self.rows + 1):
            line = '*' * (2 * n - 1)
            line = line.center(self.lenght_row * 2)
            print(line)

        for n in range(1, self.rows + 1):
            line = '*' * (2 * n - 1)
            line = line.center(self.lenght_row) + line.center(self.lenght_row)
            print(line)

if __name__ == "__main__":
    zelda = Zelda(int(input("Número de filas: ")))
    zelda.print_triangles()            