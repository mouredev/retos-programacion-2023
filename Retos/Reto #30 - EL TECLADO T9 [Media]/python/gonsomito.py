"""
 * Crea una función que transforme las pulsaciones del T9 a su representación con letras.
 * - Debes buscar cuál era su correspondencia original.
 * - Cada bloque de pulsaciones va separado por un guión.
 * - Si un bloque tiene más de un número, debe ser siempre el mismo.
 * - Ejemplo:
 *     Entrada: 6-666-88-777-33-3-33-888
 *     Salida: MOUREDEV
"""

def teclado_9(secuencia):
#compruebo que entra un bloque con elementos y si entra vacío me voy
    if len(secuencia) == 0:
        return ""
        
#declaro variables
    dict_teclado={"1":",", "11":".", "111":"?", "1111":"!", "11111":"@",
                "2":"A", "22":"B","222":"C","3":"D","33":"E","333":"F",
                 "4":"G", "44":"H", "444":"I", "5":"J", "55":"K", "555":"L",
                 "6":"M", "66":"N", "666":"O", "6666":"Ñ", "7":"P", "77":"Q", "777":"R", "7777":"S",
                  "8":"T", "88":"U", "888":"V", "9":"W", "99":"X", "999":"Y", "9999":"Z", "0":" "}
    secuencia=secuencia.split("-")
    traduccion=""
    print(secuencia)
#reviso cada nuevo bloque. me quedo con el primer valor de cada bloque para que no haya diferencias
    for bloque in secuencia:
        if len(bloque) > 0:
            bloque=bloque[0]*len(bloque)
        if bloque in dict_teclado:
            traduccion= traduccion + dict_teclado[bloque]
        else:
            traduccion= traduccion + "_"
    return traduccion
    
print(teclado_9("6-666-88-777-33-3-33-888")) #MOUREDEV
print(teclado_9("44-666-555-2-1-0-22-88-33-66-2-7777-0-8-2-777-3-33-7777-1111")) #HOLA, BUENAS TARDES!
print(teclado_9("6-656-88-757-33-3-33-858")) #MOUREDEV pero forzando bloques con numeros mal
print("problemas:")
print(teclado_9("")) #PROBLEMA 0 - SIN ELEMENTOS
print(teclado_9("68866-00-66-66666-1-1111111")) #PROBLEMA 1 - DUPLICADO NÚMEROS
print(teclado_9("666-0--66-666--1111")) #PROBLEMA 2 - DUPLICADO guión (-)
