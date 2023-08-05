"""
 * Crea una función que sea capaz de leer el número representado por el ábaco.
 * - El ábaco se representa por un array con 7 elementos.
 * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar operaciones)
 *   para las cuentas y una secuencia de "---" para el alambre.
 * - El primer elemento del array representa los millones, y el último las unidades.
 * - El número en cada elemento se representa por las cuentas que están a la izquierda del alambre.
 *
 * Ejemplo de array y resultado:
 * ["O---OOOOOOOO",
 *  "OOO---OOOOOO",
 *  "---OOOOOOOOO",
 *  "OO---OOOOOOO",
 *  "OOOOOOO---OO",
 *  "OOOOOOOOO---",
 *  "---OOOOOOOOO"]
 *  
 *  Resultado: 1.302.790
"""

def abacus_number(abacus:list) -> str:
    """ Receives a list of abacus and returns the number it contains with the
     appropiate formatting. """

    if len(abacus) != 7:
        return "Error: Abacus must have a length of 6 digits."

    if any((len(digit) != 12 or len(digit.split("0")) != 10 for digit in abacus)):
        return "Wrong number definition in abacus!"
    
    numbers_list = list(map(lambda digit: str(len(digit.split("---")[0])), abacus))
    number = "{:,}".format(int("".join(numbers_list))).replace(",", ".")
    return number


abacus_list = [
    "0---00000000",
    "000---000000",
    "---000000000",
    "00---0000000",
    "0000000---00",
    "000000000---",
    "---000000000"
]

print(abacus_number(abacus_list))     # 1.302.790