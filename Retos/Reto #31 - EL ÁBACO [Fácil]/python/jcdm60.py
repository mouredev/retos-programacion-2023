# Reto #31: El ábaco
#### Dificultad: Fácil | Publicación: 31/07/23 | Corrección: 07/08/23

## Enunciado


#
# Crea una función que sea capaz de leer el número representado por el ábaco.
# - El ábaco se representa por un array con 7 elementos.
# - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar operaciones)
#   para las cuentas y una secuencia de "---" para el alambre.
# - El primer elemento del array representa los millones, y el último las unidades.
# - El número en cada elemento se representa por las cuentas que están a la izquierda del alambre.
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

class AbacusConverter:
    def __init__(self, abacus): 
        self.abacus = abacus

    def element_to_number(self, element):
        balls = element.split("---")[0]
        return balls.count("O")

    def convert_to_number(self):
        number = ""
        for element in self.abacus:
            number += str(self.element_to_number(element))

        if not number:
            number = "0"

        number_with_dots = "{:,}".format(int(number)).replace(",", ".")

        return number_with_dots
    
if __name__ == "__main__":
    abacus = [
    "O---OOOOOOOO",
    "OOO---OOOOOO",
    "---OOOOOOOOO",
    "OO---OOOOOOO",
    "OOOOOOO---OO",
    "OOOOOOOOO---",
    "---OOOOOOOOO"
]
    converter = AbacusConverter(abacus)
    resultado = converter.convert_to_number()
    print(resultado)  # Salida: 1.302.790

    abacus = [
    "----OOOOOOOO",
    "OO---OOOOOOO",
    "OOO---OOOOOO",
    "OOOO---OOOOO",
    "OOOOO---OOOO",
    "OOOOOO---OOO",
    "OOOOOOO---OO"
]
    converter = AbacusConverter(abacus)
    resultado = converter.convert_to_number()
    print(resultado)  # Salida: 234.567