"""
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
"""
#string_1:str, string_2:str
def indentificator (string_1:str, string_2:str):
    try:
        vaule = 0
        list_result = []
        if len(string_1) == len(string_2):
            for index in string_1:
                if index != string_2[vaule]:
                    list_result.append(index)
                vaule += 1
        elif len(string_1) > len(string_2):
            return(f"la longitud del  string_1 es de {len(string_1)} la cual es superior a la del string_2 que es de {len(string_2)}")
        else:
            return(f"la longitud del  string_1 es de {len(string_2)} la cual es superior a la del string_2 que es de {len(string_1)}")
        return(list_result)
    except:
        return("ERROR")
print(indentificator("Hola como.estas", "hoLa como estas?"))
