# Crea una función que sea capaz de leer el número representado por el ábaco.
def read_abacus(abacus: []) -> str:
    if check_abacus(abacus) != True:
        return "Hay algún problema con tu ábaco"
    
    number = 0
    multiplier = 1000000

    for row in abacus:
# - El primer elemento del array representa los millones, y el último las unidades.
# - El número en cada elemento se representa por las cuentas que están a la izquierda del alambre. 
        number += multiplier * row.split("---")[0].count("O") # Esta línea cuenta las cuentas que van antes de "---" y las multiplica por su unidad correspondiente
        multiplier = multiplier * 0.1

    return int(number)

def check_abacus(abacus: []) -> bool:
# - El ábaco se representa por un array con 7 elementos.
    if len(abacus) != 7:
        return False
    
    for row in abacus:
# - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar operaciones) para las cuentas
# y una secuencia de "---" para el alambre.
        if row.count("O") != 9 or row.count("---") != 1:
            return False

    return True
    
'''
 * Ejemplo de array y resultado:
 * ["O---OOOOOOOO", <- (1,000,000, 2,000,000... 9,000,000)
 *  "OOO---OOOOOO", <- (100,000, 200,000... 900,000)
 *  "---OOOOOOOOO", <- (10,000, 20,000... 90,000)
 *  "OO---OOOOOOO", <- (1,000, 2,000... 9,000)
 *  "OOOOOOO---OO", <- (100, 200, 300... 900)
 *  "OOOOOOOOO---", <- (10, 20, 30... 90)
 *  "---OOOOOOOOO"] <- (0-9)
 *  
 *  Resultado: 1.302.790
'''

abacus = [
    "O---OOOOOOOO",
    "OOO---OOOOOO",
    "---OOOOOOOOO",
    "OO---OOOOOOO",
    "OOOOOOO---OO",
    "OOOOOOOOO---",
    "---OOOOOOOOO"
]

result = read_abacus(abacus)

print(result)