import re

def analizar_texto(texto):
    # Dividimos el texto en oraciones, utilizando expresiones regulares
    oraciones = re.split(r"[.!?]", texto)
    numero_oraciones = len(oraciones) - 1  # Restamos 1 para contar correctamente las oraciones

    palabras = []
    longitud_total = 0

    for oracion in oraciones:
        # Dividimos cada oración en palabras, utilizando espacios en blanco como separadores
        palabras_oracion = oracion.split()
        palabras.extend(palabras_oracion)
        longitud_total += sum(len(palabra) for palabra in palabras_oracion)

    numero_palabras = len(palabras)
    longitud_media = longitud_total / numero_palabras
    palabra_mas_larga = max(palabras, key=len)

    return numero_palabras, longitud_media, numero_oraciones, palabra_mas_larga


# Ejemplo de uso
texto = "Este es un ejemplo. De un texto de prueba. Otra oración más larga. PalabraSuperLarga. Otra palabra: otraPalabrasuperlarga"
resultado = analizar_texto(texto)
print("Número total de palabras:", resultado[0])
print("Longitud media de las palabras:", resultado[1])
print("Número de oraciones:", resultado[2])
print("Palabra más larga:", resultado[3])
