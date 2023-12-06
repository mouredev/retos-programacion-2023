'''
 * Los primeros dispositivos móviles tenían un teclado llamado T9
 * con el que se podía escribir texto utilizando únicamente su
 * teclado numérico (del 0 al 9).
 *
 * Crea una función que transforme las pulsaciones del T9 a su
 * representación con letras.
 * - Debes buscar cuál era su correspondencia original.
 * - Cada bloque de pulsaciones va separado por un guión.
 * - Si un bloque tiene más de un número, debe ser siempre el mismo.
 * - Ejemplo:
 *     Entrada: 6-666-88-777-33-3-33-888
 *     Salida: MOUREDEV
'''


def traductorT9(texto):

    t9 = {"1": ".", "11": ",", "111": "?", "1111": "!", "2": "A", "22": "B", "222": "C", "3": "D", "33": "E",
                "333": "F", "4": "G", "44": "H", "444": "I", "5": "J", "55": "K", "555": "L", "6": "M",
                "66": "N", "666": "O", "7": "P", "77": "Q", "777": "R", "7777": "S", "8": "T", "88": "U", "888": "V",
                "9": "W", "99": "X", "999": "Y", "9999": "Z", "0": " "}
    
    texto = texto.split('-')
    texto_T9 = ''

    for clave in texto:

        if clave in t9.keys():
            texto_T9 += t9[clave]
        else:
            texto_T9 += clave

    return texto_T9

print(traductorT9("6-666-88-777-33-3-33-888"))
print(traductorT9(input("Pulsaciones a traducir: ")))
