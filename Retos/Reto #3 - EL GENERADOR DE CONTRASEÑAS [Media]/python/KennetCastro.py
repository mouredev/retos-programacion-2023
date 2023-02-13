import random


def generar(longitud: int = random.randint(8, 16), mayusculas: bool = True, digitos: bool = True, simbolos: bool = True) ->str:
    '''Retorna una contraseña gernerada de manera aleatoria.
    
    Parametros:
        longitud: Longitud de la contraseña a generar.
                    Si no se estable la longitud será asignada aleatoriamente en un rando de 8 - 16.

        mayusculas: True si quiere que se incluya letras mayúsculas.

        digitos: True si quiere que se incluya digitos.

        simbolos: True si quiere que se incluya simbolos (#, @, $, &, -).
    '''
    longitud = longitud if 8 <= longitud <= 16 else random.randint(8, 16)
    simbolos_list = ["#", "@", "$", "&", "-"]
    abc_minus = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    abc_mayus = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    letras_list = []
    if mayusculas:
        zip_list = zip(abc_minus, abc_mayus)
        for par in zip_list:
            letras_list.extend(par)
    else:
        letras_list = abc_minus

    num_opciones = 1 + digitos + simbolos
    password = ""
    for i in range(longitud):
        match random.randint(1, num_opciones):
            case 1:
                letra = letras_list[random.randint(0, len(letras_list) - 1)]
            case 2:
                letra = str(random.randint(0, 9))
            case 3:
                letra = simbolos_list[random.randint(0, len(simbolos_list) - 1)]
        password = password + letra
    return password

print("Contraseña generada: ", generar())