# Reto #31: El ábaco
#### Dificultad: Fácil | Publicación: 31/07/23 | Corrección: 07/08/23

## Enunciado

"""
/*
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
 */
"""

abaco = [
    "O---OOOOOOOO", "OOO---OOOOOO", "---OOOOOOOOO", "OO---OOOOOOO",
    "OOOOOOO---OO", "OOOOOOOOO---", "---OOOOOOOOO"
]

def read_abaco(abaco):
  number = ""

  for i in abaco:
    contador = 0
    for j in i:
      if j == "O":
        contador += 1
      elif j == "-":
        break
    number = number + str(contador)

  return "{:,}".format(int(number)).replace(",", ".")

print(read_abaco(abaco))