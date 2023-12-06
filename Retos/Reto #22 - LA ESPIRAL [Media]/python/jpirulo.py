from colorama import Fore, Style

class Espiral:
    def __init__(self, size):
        self.size = size
        self.matriz = [[' ' for _ in range(size)] for _ in range(size)]

    def draw_spiral(self):
        for row in range(self.size):
            spiral = ""
            horizontal = row == 0
            for col in range(self.size):
                if row + col == self.size - 1:
                    spiral += Fore.GREEN + "╗" if col >= row else Fore.RED + "╚"
                    horizontal = col < row
                elif row - col == 1 and row < (self.size / 2):
                    spiral += Fore.BLUE + "╔"
                    horizontal = True
                elif row == col and row >= (self.size / 2):
                    spiral += Fore.YELLOW + "╝"
                    horizontal = False
                else:
                    spiral += Fore.CYAN + "═" if horizontal else Fore.MAGENTA + "║"
            self.matriz[row] = spiral

    def imprimir_espiral(self):
        for fila in self.matriz:
            print(fila + Style.RESET_ALL)


if __name__ == "__main__":
    try:
        size = int(input("Ingrese el tamaño de la espiral: "))
        espiral = Espiral(size)
        espiral.draw_spiral()
        espiral.imprimir_espiral()
    except ValueError:
        print("El tamaño de la espiral debe ser un número entero.")
