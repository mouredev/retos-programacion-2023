# Reto #29: El carácter infiltrado
#### Dificultad: Fácil | Publicación: 17/07/23 | Corrección: 24/07/23

## Enunciado

#
# Crea una función que reciba dos cadenas de texto casi iguales,
# a excepción de uno o varios caracteres. 
# La función debe encontrarlos y retornarlos en formato lista/array.
# - Ambas cadenas de texto deben ser iguales en longitud.
# - Las cadenas de texto son iguales elemento a elemento.
# - No se pueden utilizar operaciones propias del lenguaje
#   que lo resuelvan directamente.
# 
# Ejemplos:
# - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
# - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]

class StringComparator:
    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2

    def find_differences(self):
        if len(self.string1) != len(self.string2):
            raise ValueError("Las cadenas deben tener la misma longitud")

        differences = []
        for i in range(len(self.string1)):
            if self.string1[i] != self.string2[i]:
                differences.append(self.string2[i])

        return differences


if __name__ == "__main__":
    string1 = "Me llamo.Brais Moure"
    string2 = "Me llamo brais moure"
    comparator = StringComparator(string1, string2)
    result = comparator.find_differences()
    print(result)
