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
    # lista vacia
    leet_text = []

    for char in text:
    
        if char in leet_dict:
            leet_text.append(leet_dict[char])
    
        else:
            leet_text.append(char)

    
    return ''.join(leet_text)

# Testeamos
print(leet('Como estas, Mariano?'))  
