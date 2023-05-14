#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://retosdeprogramacion.com/semanales2023

# ! CUIDADO
# todo por hacer
# ? aviso
# * explicación

"""
/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */
 """

import os

if __name__ == '__main__':
    os.system('clear')

    texto_para_analizar = """Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim.
Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus.
Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui.
Etiam rhoncus. Maecenas tempus, tellus eget. condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante.
Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, quis gravida magna mi a libero. Fusce vulputate eleifend sapien. Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Nullam accumsan lorem in dui. Cras ultricies mi eu turpis hendrerit fringilla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In ac dui quis mi"""

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

    print('Resultados')
    print('----------')
    print(f'Número total de palabras: {numero_palabras}')
    print(f'Longitud media de las palabras: {longuitud_media}')
    print(f'Número de oraciones del texto: {numero_frases}')
    print(f'Palabra más larga: {palabras_ordenadas[0]}')

