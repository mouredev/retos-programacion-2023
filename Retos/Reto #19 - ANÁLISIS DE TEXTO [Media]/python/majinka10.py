import re

# La libreria re, es un operador de expresiones regulares.

def analizador(texto:str):
    oraciones=texto.count('.')
    # Con re.findall, encuentro todas las palabras del texto y las meto en palabras.
    palabras=re.findall(r'\w+',texto)
    longitud_palabras=0
    chars_longest_word=0
    longest_word=0

    #Para encontrar la palabra más larga y la longitud media de las palabras utilizo el siguiente for.

    for palabra in palabras:
        if len(palabra)>=chars_longest_word:
            chars_longest_word=len(palabra)
            longest_word=palabra
        longitud_palabras+=len(palabra)
    cantidad_promedio=longitud_palabras/len(palabras)

    # Retorono todos los datos que pidieron en el enunciado del ejercicio.

    return len(palabras), cantidad_promedio, oraciones, longest_word

print(analizador('El cielo estaba despejado y el sol brillaba con intensidad. Las flores del jardín bailaban al compás del viento suave. Era un día perfecto para salir a pasear.'))