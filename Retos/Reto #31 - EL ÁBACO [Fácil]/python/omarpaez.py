#
# Crea una función que sea capaz de leer el número representado por el ábaco.
# - El ábaco se representa por un array con 7 elementos.
# - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar
#   operaciones) para las cuentas y una secuencia de "---" para el alambre.
# - El primer elemento del array representa los millones, y el último las unidades.
# - El número en cada elemento se representa por las cuentas que están a
#   la izquierda del alambre.
#
# Ejemplo de array y resultado:
# ["O---OOOOOOOO",
#  "OOO---OOOOOO",
#  "---OOOOOOOOO",
#  "OO---OOOOOOO",
#  "OOOOOOO---OO",
#  "OOOOOOOOO---",
#  "---OOOOOOOOO"]
#
#  Resultado: 1.302.790
#

def read_number(abaco: list()) -> list():

    acum = 0
    numero = " "

    if valid_abaco(abaco):
        for number in abaco:
            for digit in number:
                if digit == "O":
                    acum += 1
                else:
                    digito = acum
                    acum = 0
                    numero += str(digito)
                    break

        result = '{:,}'.format(int(numero))
        return result
    return "Abaco No Valido"


def valid_abaco(abaco) -> bool:
    if len(abaco) != 7:
        return False

    for element in abaco:
        if len(element) != 12 or element.count("O") != 9:
            return False

    return True


print(read_number(["O---OOOOOOOO",
                  "OOO---OOOOOO",
                   "---OOOOOOOOO",
                   "OO---OOOOOOO",
                   "OOO---OOOOOO",
                   "OOOOOOOOO---",
                   "---OOOOOOOOO"]))
