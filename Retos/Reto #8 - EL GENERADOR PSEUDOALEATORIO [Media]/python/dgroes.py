"""
/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */
"""

from datetime import datetime

def randomNumber():
    numbers = set()
    x = 0

    now = datetime.now()
    second = now.second
    microsecond = now.microsecond

    new_number = ((microsecond * 73) * 251) * second

 
    while x < 30:
        new_number = (new_number * 43) + 10139

        numbers.add(new_number % 101)

        x += 1
    final = sum(numbers) % 101
    return final


resultado = randomNumber()
print(f"Número pseudoaleatorio generado: {resultado}")

