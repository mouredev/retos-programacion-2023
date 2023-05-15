"""
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
"""

import os

if __name__ == '__main__':
    os.system('clear')

    texto_para_analizar = input('¿Qué cadena quieres analizar? ')
    numero_palabras = len(texto_para_analizar.split())
    numero_frases = len(texto_para_analizar.split('.'))
    media = 0
    palabra_mas_larga = ''
    palabras = {}
    for palabra in texto_para_analizar.split():
        palabras[palabra] = len(palabra)
    longuitud_media = sum(palabras.values()) / len(palabras)
    palabras_ordenadas = dict(sorted(palabras.items(), key=lambda item:item[1], reverse=True))
    palabras_ordenadas = list(palabras_ordenadas.keys())
    print()
    print('Resultado')
    print('---------')
    print(f'Número total de palabras: {numero_palabras}')
    print(f'Longitud media de las palabras: {longuitud_media}')
    print(f'Número de oraciones del texto: {numero_frases}')
    print(f'Palabra más larga: {palabras_ordenadas[0]}')

