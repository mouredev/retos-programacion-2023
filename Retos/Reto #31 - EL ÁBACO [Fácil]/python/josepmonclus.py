'''
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
'''

def decode_abacus(abacus: []) -> int:
    num = 0
    
    for i in range(len(abacus) - 1, -1, -1):
        split = abacus[i].split('---')
        if len(split) == 1:
            n = 0
        else:
            n = len(split[0])
        
        num += n * pow(10, 6-i)
    
    return num

print(decode_abacus([
    "O---OOOOOOOO",
    "OOO---OOOOOO",
    "---OOOOOOOOO",
    "OO---OOOOOOO",
    "OOOOOOO---OO",
    "OOOOOOOOO---",
    "---OOOOOOOOO"]
))

print(decode_abacus([
    "OOOOOO---OOO",
    "OOOOOOOOO---",
    "O---OOOOOOOO",
    "OOO---OOOOOO",
    "O---OOOOOOO",
    "OOOOOOOOO---",
    "OO---OOOOOOO"]
))