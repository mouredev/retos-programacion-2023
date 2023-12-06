import colorama
from colorama import Fore
import random

colorama.init(autoreset=True)

class ColumnaExcel:
    def __init__(self):
        #crear diccionario
        self.diccionario_letras = {chr(i): i - ord('A') + 1 for i in range(ord('A'), ord('Z') + 1)}

    def _es_valido(self, nombre_columna):
        return nombre_columna.isalpha() and nombre_columna.isupper()

    def _calcular_valor_columna(self, nombre_columna):
        valor_columna = 0
        for letra in nombre_columna:
            valor_columna = valor_columna * 26 + self.diccionario_letras[letra]
        return valor_columna

    def obtener_numero_columna_excel(self, nombre_columna):
        if not self._es_valido(nombre_columna):
            return f"{self._color_aleatorio()}Nombre de columna no válido{Fore.RESET}"

        valor_columna = self._calcular_valor_columna(nombre_columna)

        return f"{self._color_aleatorio()}El número de columna para '{nombre_columna}' es: {valor_columna}{Fore.RESET}"

    def _color_aleatorio(self):
        colores = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
        return random.choice(colores)


def manejar_casos_especiales(func):
    def wrapper(nombre_columna):
            return func(nombre_columna)
    return wrapper


@manejar_casos_especiales
def numero_columna_excel(nombre_columna):
    excel = ColumnaExcel()
    return excel.obtener_numero_columna_excel(nombre_columna)


if __name__ == "__main__":
    nombre_columna = input("Ingresa el nombre de la columna de Excel: ")
    print(numero_columna_excel(nombre_columna))
