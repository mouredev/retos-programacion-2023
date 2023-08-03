
'''
 Crea una función que reciba dos cadenas de texto casi iguales,
 a excepción de uno o varios caracteres. 
 La función debe encontrarlos y retornarlos en formato lista/array.
 - Ambas cadenas de texto deben ser iguales en longitud.
 - Las cadenas de texto son iguales elemento a elemento.
 - No se pueden utilizar operaciones propias del lenguaje
   que lo resuelvan directamente.
 
 Ejemplos:
 - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
 - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
'''

def find_infiltrates(text1: str, text2: str):
    diff = []
    
    if len(text1) == len(text2):
        for i in range(0, len(text1)):
            if text1[i] != text2[i]:
                diff.append(text2[i])
        
    return diff

print(find_infiltrates('Me llamo mouredev', 'Me llemo mouredov'))
print(find_infiltrates('Me llamo.Brais Moure', 'Me llamo brais moure'))