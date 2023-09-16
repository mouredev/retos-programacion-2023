"""/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */"""
from datetime import datetime
import math


def choose_number():
    now = datetime.today().second
    random = str(math.cos(60 - now))
    number, decimals = random.split(".")
    if len(decimals) >= 2:
        return decimals[0] + decimals[1]
    else:
        return "100"


def main():
    print(f"tu numero aleatorio es: {choose_number()}")


main()
