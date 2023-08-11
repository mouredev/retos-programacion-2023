"""
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
"""
list_vaule = ["A","B","C","D","E","F","G","H","I","J","K","L",
              "M","N","O","P","Q","R","S","T","U","V","W","X",
              "Y","Z"]
def excel(letter:str):
    count = 1
    result = 0
    long = len(letter)
    if long <= 1:
        result = list_vaule.index(letter)+1
    elif long >= 2:
        for index in letter:
            while count < long:
                result += (list_vaule.index(index) + 1) * 26
                count += 1
                break
        result += list_vaule.index(index) + 1
    return result
print(excel_2("CBA"))
