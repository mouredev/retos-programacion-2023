def permutaciones_palabra(palabra):
    # Caso base: si la palabra tiene una sola letra, no hay más permutaciones
    if len(palabra) <= 1:
        return [palabra]

    # Lista para almacenar las permutaciones
    permutaciones = []

    # Generar permutaciones recursivamente
    for i in range(len(palabra)):
        primera_letra = palabra[i]
        resto_palabra = palabra[:i] + palabra[i+1:]
        permutaciones_resto = permutaciones_palabra(resto_palabra)

        for permutacion in permutaciones_resto:
            permutaciones.append(primera_letra + permutacion)

    return permutaciones

resultado = permutaciones_palabra('sol')
print(resultado)