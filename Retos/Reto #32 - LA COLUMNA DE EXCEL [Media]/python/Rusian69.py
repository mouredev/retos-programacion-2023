"""
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
"""
list_vaule = {"A":1,"B":2,"C":3,"D":4,"E":5,
              "F":6,"G":7,"H":8,"I":9,"J":10,
              "K":11,"L":12,"M":13,"N":14,"O":15,
              "P":16,"Q":17,"R":18,"S":19,"T":20,
              "U":21,"V":22,"W":23,"X":24,"Y":25,
              "Z":26
              }
def excel(letter:str):
    suma = 0
    vaule = 0
    count = 1
    result = 0
    long = len(letter)
    if long <= 1:
        result = list_vaule[letter.upper()]
    elif long >= 2:
        for index in letter:
            while count < long:
                vaule = list_vaule[index.upper()]
                suma += vaule * list_vaule["Z"]
                count += 1
                break
        val = letter[-1]
        suma += list_vaule[val.upper()]
        result = suma
    return result
print(excel("CBA"))
