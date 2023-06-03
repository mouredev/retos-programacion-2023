"""
 * Crea un programa que encuentre y muestre todos los pares de números primos
 * gemelos en un rango concreto.
 * El programa recibirá el rango máximo como número entero positivo.
 * 
 * - Un par de números primos se considera gemelo si la diferencia entre
 *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
"""

def numero_primos_gemelos():
#codigo para sacar numero primos
    number = int(input("ingrese el rango maximo: "))
    count = 0
    list_primos = list()
    result = 0
    result_str = ""
    for index in range(2, number + 1):
        for index_2 in range(2, int(index/2) + 1):
            if index % index_2 == 0:
                count += 1

        if count == 0:
            list_primos.append(index)
        count = 0
    print(list_primos)
#genero un rango para que recorra i del la longitud de la lista - 1 e itero si la funcion se cierta guarda los valores 1 y 2 sino pasa al siguiente 
    for i in range(len(list_primos) - 1):
        if list_primos[i+1] - list_primos[i] == 2:
            val_1 = list_primos[i]
            val_2 = list_primos[i+1]
            result_str += f"({val_1},{val_2})"
    print(result_str)
numero_primos_gemelos()
