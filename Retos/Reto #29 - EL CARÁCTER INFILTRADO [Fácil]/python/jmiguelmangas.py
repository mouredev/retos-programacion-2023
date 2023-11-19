"""```
/*
 * Crea una función que reciba dos cadenas de texto casi iguales,
 * a excepción de uno o varios caracteres. 
 * La función debe encontrarlos y retornarlos en formato lista/array.
 * - Ambas cadenas de texto deben ser iguales en longitud.
 * - Las cadenas de texto son iguales elemento a elemento.
 * - No se pueden utilizar operaciones propias del lenguaje
 *   que lo resuelvan directamente.
 * 
 * Ejemplos:
 * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
 * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
 */
```"""


def get_two_strings():
    frase1 = input("Frase 1: ").strip().split(" ")
    frase2 = input("Frase 2: ").strip().split(" ")
    return (frase1, frase2)


def check_characters(tupla):
    lista = []
    for i in range(len(tupla[0])):
        if tupla[0][i] == tupla[1][i]:
            continue
        else:
            lista.append(check_difference(tupla[0][i], tupla[1][i]))
    return lista


def check_difference(string1, string2):
    lista = []
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            lista.append([string1[i], string2[i]])
    return lista


def main():
    print(check_characters(get_two_strings()))


if __name__ == "__main__":
    main()
