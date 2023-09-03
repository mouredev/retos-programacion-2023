def analizar_oracion(text: str):
    palabras = 0
    longitudes = []
    oraciones = 0
    palabra_grande = ""

    text = text.replace("\n", " ")

    # Contador
    for palabra in text.split(" "):
        if palabra.endswith("."):
            oraciones += 1
        palabra = palabra.lower().replace(".", "")
        palabras += 1
        longitudes.append(len(palabra))
        if len(palabra) > len(palabra_grande):
            palabra_grande = palabra

    promedio = sum(longitudes) / len(longitudes)

    print(f"Numero total de palabras: {palabras}")
    print(f"Longitud media de las palabras: {round(promedio, 2)}")
    print(f"Número de oraciones del texto: {oraciones}")
    print(f"Palabra mas grande: {palabra_grande}")


if __name__ == "__main__":
    texto = """Escrito de prueba de script para validar varios aspectos de una serie de oraciones.
Segunda oración del texto. Ejemplo para probar. palabra grande computadora."""
    analizar_oracion(texto)
