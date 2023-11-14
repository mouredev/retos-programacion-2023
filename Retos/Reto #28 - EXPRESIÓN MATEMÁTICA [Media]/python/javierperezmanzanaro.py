"""/*
 * Crea una función que reciba una expresión matemática (String)
 * y compruebe si es correcta. Retornará true o false.
 * - Para que una expresión matemática sea correcta debe poseer
 *   un número, una operación y otro número separados por espacios.
 *   Tantos números y operaciones como queramos.
 * - Números positivos, negativos, enteros o decimales.
 * - Operaciones soportadas: + - * / %
 *
 * Ejemplos:
 * "5 + 6 / 7 - 4" -> true
 * "5 a 6" -> false
 */"""




def expresion(expresion: str)-> bool:
    """Revisa si la expresión es una función matematica del tipo:
    numero + esp + operación + ...

    Args:
        expresion (str): expresion a analizar

    Returns:
        bool: Es o no una expresión matematica


    python3 -m doctest -v expresion.py

    >>> expresion("5 + 6 / 7 - 4")
    True
    >>> expresion("5 a 6")
    False
    """
    lista = expresion.split()
    salida_operacion = False
    salida_numero = True
    #for caracter in lista:
    for i in range(len(lista)):
        if i % 2 == 0:
            try:
                valor = float(lista[i])
            except:
                salida_numero = False
        else:
            if lista[i] in '+-*/%':
                salida_operacion = True
    # print(f'{salida_operacion=} ; {salida_numero=}')
    if salida_operacion == True and salida_numero == True:
        return True
    else:
        return False


if __name__ == '__main__':
    import doctest
    doctest.testmod() #verbose=True
    formula = input('¿Qué expresión matematica quieres analizar? ')
    print(f'La expresión: "{formula}" es: {expresion(formula)}')