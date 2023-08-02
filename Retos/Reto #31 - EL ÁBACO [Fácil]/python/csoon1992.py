"""
Crea una función que sea capaz de leer el número representado por el ábaco.
- El ábaco se representa por un array con 7 elementos.
- Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar operaciones)
    para las cuentas y una secuencia de "---" para el alambre.
- El primer elemento del array representa los millones, y el último las unidades.
- El número en cada elemento se representa por las cuentas que están a la izquierda del alambre.
*
Ejemplo de array y resultado:
["O---OOOOOOOO",
    "OOO---OOOOOO",
    "---OOOOOOOOO",
    "OO---OOOOOOO",
    "OOOOOOO---OO",
    "OOOOOOOOO---",
    "---OOOOOOOOO"]

    Resultado: 1.302.790
    
    NO SEAIS MUY DUROS CONMIGO. DESPUÉS DEL print('Hello world') ESTE ES MI PRIMER CÓDIGO EN PYTHON :P
"""

def getNumber(abacus: list) -> str:
    result: str = ''
    
    for line in abacus:
        number: str = str(line.find('---'))
        result += number
        
    return getFormattedNumber(result)


def getFormattedNumber(number: str) -> int:
    return format(f'{int(number):,}').replace(',', '.')
    

abacus = [
    "O---OOOOOOOO",
    "OOO---OOOOOO",
    "---OOOOOOOOO",
    "OO---OOOOOOO",
    "OOOOOOO---OO",
    "OOOOOOOOO---",
    "---OOOOOOOOO"
]

print(getNumber(abacus))
    