'''
*
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
 *
'''

def matching (string_one: str, string_two: str):
    
    equals = []
    
    if len(string_one) != len(string_two):

        return print('Las cadenas son de distinto largo')
    else:
        count = 0

        for caracter in string_two:
            
            if  caracter != string_one[count]:
                equals.append(caracter)

            count += 1


    return equals

if __name__ == '__main__':
    
    string_one = 'Me llamo mouredev'
    string_two = 'Me llemo mouredov'
    print(matching(string_one,string_two))
    string_one = 'Me llamo.Brais Moure'
    string_two = 'Me llamo brais moure'
    print(matching(string_one,string_two))