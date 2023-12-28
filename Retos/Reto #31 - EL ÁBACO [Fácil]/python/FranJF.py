"""
 Crea una función que sea capaz de leer el número representado por el ábaco.
 - El ábaco se representa por un array con 7 elementos.
 - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar operaciones)
   para las cuentas y una secuencia de "---" para el alambre.
 - El primer elemento del array representa los millones, y el último las unidades.
 - El número en cada elemento se representa por las cuentas que están a la izquierda del alambre.

 Ejemplo de array y resultado:
 ["O---OOOOOOOO",
  "OOO---OOOOOO",
  "---OOOOOOOOO",
  "OO---OOOOOOO",
  "OOOOOOO---OO",
  "OOOOOOOOO---",
  "---OOOOOOOOO"]

  Resultado: 1.302.790
"""


def get_abaco_number(combinacion: str) -> str:
    combinacion: str = combinacion.split("---")[0]
    return str(len(combinacion))


def read_abaco(combinaciones: list) -> str:
    r: str = ""
    for combinacion in combinaciones:
        r += get_abaco_number(combinacion)
    return "{:,}".format(int(r)).replace(",", ".")


if __name__ == "__main__":
    combinaciones = [
        "O---OOOOOOOO",
        "OOO---OOOOOO",
        "---OOOOOOOOO",
        "OO---OOOOOOO",
        "OOOOOOO---OO",
        "OOOOOOOOO---",
        "---OOOOOOOOO",
    ]
    print(read_abaco(combinaciones))
