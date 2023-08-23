"""
/*
 * Crea una función que sea capaz de leer el número representado por el ábaco.
 * - El ábaco se representa por un array con 7 elementos.
 * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar
 *   operaciones) para las cuentas y una secuencia de "---" para el alambre.
 * - El primer elemento del array representa los millones, y el último las unidades.
 * - El número en cada elemento se representa por las cuentas que están a
 *   la izquierda del alambre.
 *
 * Ejemplo de array y resultado:
 * ["O---OOOOOOOO",
 *  "OOO---OOOOOO",
 *  "---OOOOOOOOO",
 *  "OO---OOOOOOO",
 *  "OOOOOOO---OO",
 *  "OOOOOOOOO---",
 *  "---OOOOOOOOO"]
 *
 *  Resultado: 1.302.790

["O---OOOOOOOO", "OOO---OOOOOO", "---OOOOOOOOO", "OO---OOOOOOO", "OOOOOOO---OO", "OOOOOOOOO---", "---OOOOOOOOO"]
 */"""



def expresion(array: str)-> int:

    #* Limpiamos y separamos la cadena
    array = array[1:-1]
    array = array.replace('"', '')
    array = array.replace(' ', '')
    array = array.split(',') # type: ignore

    #* Recorremos cada elemento y lo transformamos
    resultado = ''
    for elemento in array:
        elemento = elemento.split('---')
        if len(elemento[0]) > 0:
            cifra = str(len(elemento[0]))
        else:
            cifra = '0'
        resultado = resultado + cifra
    return int(resultado)


if __name__ == '__main__':
    print()
    array = input('Introduce el array del ábaco: ')
    resultado = f"{expresion(array):,}".replace(',', '.')
    print(f"El ábaco contiene el número: {resultado}")