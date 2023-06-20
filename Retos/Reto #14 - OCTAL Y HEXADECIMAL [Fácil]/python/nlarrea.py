"""
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
"""

def decimalToOctalAndHexa(decNum):
    # decimal: [oct, hex]
    CONVERTIONS = {
        0: [0, 0],
        1: [1, 1],
        2: [2, 2],
        3: [3, 3],
        4: [4, 4],
        5: [5, 5],
        6: [6, 6],
        7: [7, 7],
        8: [10, 8],
        9: [11, 9],
        10: [12, 'A'],
        11: [13, 'B'],
        12: [14, 'C'],
        13: [15, 'D'],
        14: [16, 'E'],
        15: [17, 'F']
    }


    def decimalTo(base):
        number = decNum
        numList = []
        index = 0 if base == 8 else 1

        if number < 16:
            return CONVERTIONS[number][index]

        while (number > base):
            numList.append(str(CONVERTIONS[number % base][index]))
            number = int(number / base)

        numList.append(str(CONVERTIONS[number % base][index]))
        numList.reverse()

        return "".join(numList)


    octal = int(decimalTo(8))
    hexa = str(decimalTo(16))

    return {"octal": octal, "hexa": hexa}


print(decimalToOctalAndHexa(11))        # {'octal': 13, 'hexa': 'B'}
print(decimalToOctalAndHexa(495))       # {'octal': 757, 'hexa': '1EF'}
print(decimalToOctalAndHexa(1023))      # {'octal': 1777, 'hexa': '3FF'}
print(decimalToOctalAndHexa(80))        # {'octal': 120, 'hexa': '50'}