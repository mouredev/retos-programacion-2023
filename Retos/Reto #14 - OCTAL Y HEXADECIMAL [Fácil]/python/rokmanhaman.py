"""
Reto #14: OCTAL Y HEXADECIMAL
FÁCIL | Publicación: 03/04/23 | Resolución: 10/04/23
/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */
"""

class Number():
    
    def __init__(self, number):
        self.number = number
    
    def dec_to_oct(self):
        
        cociente_list = [self.number // 8]
        resto_list = [self.number % 8]
        i = 0
        while cociente_list[i] >= 8:
            cociente_list.append(cociente_list[i] // 8)
            resto_list.append(cociente_list[i] % 8)
            i = i + 1

        
        largo = len(resto_list)
        last_cociente  = cociente_list[i]
        invert_resto = [resto_list[x] for x in range(largo-1,-1,-1)]

        resultado_text = str(last_cociente)+ "".join(map(str, invert_resto))

        return print(f" el num decimal: {self.number} se corresponde con el num octal: {resultado_text}")
    
    def dec_to_hex(self):
        cociente_list = [self.number // 16]
        resto_list = [self.number % 16]
        i = 0
        while cociente_list[i] >= 16:
            cociente_list.append(cociente_list[i] // 16)
            resto_list.append(cociente_list[i] % 16)
            i = i + 1

        
        last_cociente  = cociente_list[i]
        invert_resto = resto_list[::-1]
        hex_values = "0123456789ABCDEF"
        last_cociente_hex = hex_values[last_cociente]
        invert_resto_hex = [hex_values[y] for y in invert_resto]

        resultado_text = str(last_cociente_hex)+ "".join(map(str, invert_resto_hex))

        return print(f" el num decimal: {self.number} se corresponde con el num hexa: {resultado_text}")


num_dec = Number(255)

num_dec.dec_to_oct()
num_dec.dec_to_hex()

