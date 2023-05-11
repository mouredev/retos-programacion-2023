import string

texto = """La asignación dinámica de memoria en el Lenguaje de programación C, conocida también como malloc (abreviatura del inglés memory allocation), se realiza a través de un grupo de funciones en la biblioteca estándar de C , es decir, malloc, realloc, calloc y free. En C++, se incluyen estas funciones por retrocompatibilidad, pero han sido sustituidas en gran parte por los operadores new y new[].

Están disponibles muchas implementaciones diferentes del mecanismo de asignación de memoria real, utilizado por malloc. Su rendimiento varía tanto en tiempo de ejecución y memoria requerida."""

signos_puntuacion = string.punctuation

def analisis_texto(texto):
    valor = True
    longitud_de_palabras = []
    while valor:
        texto_limpio = ""
        palabra_mas_larga = ""
        for i in texto:
            if i not in signos_puntuacion:
                texto_limpio += i
            
        for i in texto_limpio.split():
            if len(i) > len(palabra_mas_larga):
                palabra_mas_larga = i

        for i in texto_limpio.split():
            longitud = len(i)
            longitud_de_palabras.append(longitud)

        valor = False

    total_de_palabras = len(texto_limpio.split())
    longitud_media = sum(longitud_de_palabras) // total_de_palabras
    oraciones = len(texto.split(".")) - 1

    # 1. total de palabras
    print(f"Total de palabras: {total_de_palabras}")

    #2. longitud media de palabras
    print(f"Longitud media de las palabras: {longitud_media}")

    # 3. total de oraciones
    print(f"Total de oraciones: {oraciones}")

    # 4. palabra mas larga
    print(f"Palabra mas larga: {palabra_mas_larga}")

analisis_texto(texto)
