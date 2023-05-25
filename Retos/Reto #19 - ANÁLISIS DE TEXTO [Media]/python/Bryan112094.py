# Crea un programa que analice texto y obtenga:
# - Número total de palabras.
# - Longitud media de las palabras.
# - Número de oraciones del texto (cada vez que aparecen un punto).
# - Encuentre la palabra más larga.
# Todo esto utilizando un único bucle.

import re

def analityText(texto):
    #Total de palabras
    words = re.sub(r"[,.]", "", texto).split(" ")
    totalWord = len(words)
    
    #Longitud y palabra más larga
    mediaWords = 0
    largeWord = ''
    for word in words:
        largeWord = word if len(largeWord) < len(word) else largeWord
        mediaWords += len(word)
    mediaWords = mediaWords / totalWord

    #Oraciones del texto
    prayers = texto.split(".")
    prayers = [prayer for prayer in prayers if prayer]

    print(f"Número total de palabras: {totalWord}")
    print(f"Longitud media de las palabras: {mediaWords}")
    print(f"Número de oraciones del texto: {len(prayers)}")
    print(f"La palabra más larga: {largeWord}")

textoEjemplo = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras vel justo erat. Curabitur facilisis ante mauris, at auctor nisl sodales eu. Nam sollicitudin dapibus orci, id feugiat libero ultrices ut. Phasellus bibendum congue cursus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Cras augue lorem, suscipit sit amet suscipit ac, suscipit sed tellus. Sed nisi urna, finibus et nisi non, volutpat hendrerit ante. Aliquam pharetra elementum felis, vel fermentum elit commodo vel. Cras eu tempor purus, ut commodo magna. Mauris id pretium odio."
analityText(textoEjemplo)