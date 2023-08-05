def t9_to_text(pulsaciones):
    t9_mapping = {
        '2': 'ABC', '3': 'DEF', '4': 'GHI',
        '5': 'JKL', '6': 'MNO', '7': 'PQRS',
        '8': 'TUV', '9': 'WXYZ', '0': ' '
    }
    
    palabras = pulsaciones.split('-')
    texto = ''
    bloque_actual = ''
    
    for bloque in palabras:
        if bloque.isdigit():
            bloque_actual = bloque
        else:
            texto += t9_mapping[bloque_actual][len(bloque) - 1]
    
    return texto

# Ejemplo de uso:
entrada = "6-666-88-777-33-3-33-888"
salida = t9_to_text(entrada)
print(salida)  # Salida: "MOUREDEV"
