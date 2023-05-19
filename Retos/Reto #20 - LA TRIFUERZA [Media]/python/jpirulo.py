def decorador_zelda(funcion):
    def wrapper(self):
        print("¡El nuevo 'The Legend of Zelda: Tears of the Kingdom' ya está disponible!")
        funcion(self)
    return wrapper


class Zelda:
    def __init__(self, rows):
        self.rows = rows
        self.lenght_row = 2 * rows

    @decorador_zelda
    def draw(self):
        print(1, self.rows + 1)
        for n in range(1, self.rows + 1):
            line = '*' * (2 * n - 1)
            line = line.center(self.lenght_row * 2)
            print(line)

        for n in range(1, self.rows + 1):
            line = '*' * (2 * n - 1)
            line = line.center(self.lenght_row) + line.center(self.lenght_row)
            print(line)


if __name__ == "__main__":
    num_filas = int(input("Número de filas: "))
    zelda = Zelda(num_filas)
    zelda.draw()