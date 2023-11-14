""" /*
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
 */ """

def numero_en_abecedario(letra:str) -> int:
    letra = letra.lower()
    if 'a' <= letra <= 'z':
        return ord(letra) - ord('a') + 1
    else:
        return None

def columna_excel(cadena:str) -> int:
    valor = 0
    largo = len(cadena)
    for letra in cadena:
        posicion = numero_en_abecedario(letra)
        if posicion is None:           
            # Columna no válida.
            return None
        else:
            
            if largo-1==0:
                valor = valor + posicion
            else:
                valor = posicion * 26 * (largo - 1)
            largo -= 1                                
    return valor

print(columna_excel('A'))
print(columna_excel('Z'))
print(columna_excel('CA5'))
print(columna_excel('CA'))