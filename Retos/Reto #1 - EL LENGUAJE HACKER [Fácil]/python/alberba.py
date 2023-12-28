def traductor_leet(texto):
    word_translator = {'A': '4', "B": "I3", 'C': '[', 'D': ')', 'E': '3', 'F': '|=',
                        'G': '&', 'H': '#', 'I': '1', 'J': ',_|', 'K': '|<¡', 
                        'L': '|_', 'M': '/\/\\', 'N': '^/', 'O': '0', 'P': '|*', 
                        'Q': '(_,)', 'R': 'I2', 'S': '5', 'T': '7', 'U': '(_)', 
                        'V': '\/', 'W': '\/\/', 'X': '><', 'Y': 'j', 'Z': '2',
                        '0': 'o', '1': 'L', '2': 'R', '3': 'E', '4': 'A', '5': 'S',
                        '6': 'b', '7': 'T', '8': 'B', '9': 'g'}
    result = ""

    # Como el usuario puede escribir una oración con mínusculas, crearemos un
    # estandar en mayúsculas 
    for char in texto.upper():
        if char in word_translator.keys():
            result += word_translator[char]
        # Para caracteres que no esten definidos, los escribiremos sin modificar
        else:
            result += char
    print(result)
    
traductor_leet(input("Escribe tu frase: "))