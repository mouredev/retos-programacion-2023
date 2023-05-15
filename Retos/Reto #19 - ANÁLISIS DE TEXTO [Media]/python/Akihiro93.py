with open("D:\codigo\Curso de python\python-intermedio\docs\my_file.txt", "r") as file:
    palabras = file.read().split()
    contador_palabras = 0
    contador_oraciones = 0
    longitud_media = 0
    palabra_larga = ""
    for palabra in palabras:
        contador_palabras += 1
        if "." == palabra[-1]:
            contador_oraciones += 1
            palabra = (palabra[:-1])
        longitud_media += len(palabra)
        if len(palabra) > len(palabra_larga):
            palabra_larga = palabra
        contador_palabras += 1
    longitud_media /= contador_palabras

print(f"el numero de palabras es: {contador_palabras}, la longitud media es: {longitud_media}, el numero de oraciones es: {contador_oraciones}, la palabra mas larga es: {palabra_larga}")