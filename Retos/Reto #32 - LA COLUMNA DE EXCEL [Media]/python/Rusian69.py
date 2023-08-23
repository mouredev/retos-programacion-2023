"""
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
"""
#version mejorada de codigo
list_vaule = ["A","B","C","D","E","F","G","H","I","J","K","L",
              "M","N","O","P","Q","R","S","T","U","V","W","X",
              "Y","Z"]
def excel_2(letter:str):
    count = 1
    result = 0
    if len(letter) <= 1:
        result = list_vaule.index(letter.upper())+1
    elif len(letter) >= 2:
        for index in letter:
            while count < len(letter):
                result += (list_vaule.index(index.upper()) + 1) * 26
                count += 1
                break
        result += list_vaule.index(index.upper()) + 1
    return result
print(excel_2("CBA"))
