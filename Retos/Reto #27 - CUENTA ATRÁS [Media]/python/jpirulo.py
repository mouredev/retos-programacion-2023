import time
from colorama import init, Fore
import random

init()  # Inicializar Colorama

class CuentaAtras:
    def __init__(self, inicio, segundos):
        self.inicio = inicio
        self.segundos = segundos

    def cuenta_regresiva(self):
        for numero in range(self.inicio, 0, -1):
            color = random.choice([Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA])  # Colores aleatorios
            print(color + str(numero) + Fore.RESET)
            time.sleep(self.segundos)

if __name__ == '__main__':
    inicio = int(input("Ingresa el número de inicio: "))
    segundos = int(input("Ingresa los segundos entre cada cuenta: "))

    if inicio > 0 and segundos > 0:
        cuenta = CuentaAtras(inicio, segundos)
        cuenta.cuenta_regresiva()
    else:
        print("Error: Solo se aceptan números enteros positivos.")
