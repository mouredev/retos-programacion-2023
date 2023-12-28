# Reto #15: La escalera
#### Dificultad: Media | Publicación: 17/04/23 | Corrección: 24/04/23

## Enunciado

#
# Crea una función que dibuje una escalera según su número de escalones.
# - Si el número es positivo, será ascendente de izquiera a derecha.
# - Si el número es negativo, será descendente de izquiera a derecha.
# - Si el número es cero, se dibujarán dos guiones bajos (__).
#
# Ejemplo: 4
#         _
#       _|
#     _|
#   _|
# _|
#


class Ladder:
    def __init__(self, steps):
        self.steps = steps

    def print_ladder(self):
        ladder = ""
        if self.steps > 0:
            for step in range(self.steps + 1):
                ladder += " " * (self.steps - step) * 2 + "_|" * bool(step) + "_" * (1 - bool(step)) + "\n"
        elif self.steps < 0:
            for step in range(abs(self.steps) + 1):
                ladder += " " * step * 2 + "|_\n" * bool(step)
        else:
            ladder = "__\n"

        return ladder


if __name__ == "__main__":
    steps = int(input("Número de escalones: "))
    ladder = Ladder(steps)
    print(ladder.print_ladder())
