def leet(text):
    # Creamos un diccionario con las transformaciones del lenguaje "leet"
    leet_dict = {
        'a': '4',
        'b': '8',
        'e': '3',
        'g': '6',
        'l': '1',
        'o': '0',
        's': '5',
        't': '7',
        'z': '2'
    }

    # Creamos una lista vacía para almacenar el texto transformado
    leet_text = []

    # Recorremos cada caracter del texto
    for char in text:
        # Si el caracter está en el diccionario, lo reemplazamos por su valor en "leet"
        if char in leet_dict:
            leet_text.append(leet_dict[char])
        # Si no está en el diccionario, dejamos el caracter sin cambiar
        else:
            leet_text.append(char)

    # Devolvemos el texto transformado como una cadena
    return ''.join(leet_text)

# Probamos la función con un ejemplo
print(leet('Como estas, Mariano?'))  # Debería mostrar "h0l4 mund0"
