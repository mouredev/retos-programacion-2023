leet_dictionary = {'A': '4', 'B': 'I3', 'C': '[', 'D': ')', 'E': '3', 'F': '|=', 'G': '&', 'H': '#', 'I': '1',
                   'J': ',_|', 'K': '>|', 'L': '1', 'M': '/\/\\', 'N': '^/', 'O': '0', 'P': '|*', 'Q': '(_,)',
                   'R': 'I2',
                   'S': '5', 'T': '7', 'U': '(_)', 'V': '\/', 'W': '\/\/', 'X': '><', 'Y': 'j', 'Z': '2', '0': 'o',
                   '1': 'L', '2': 'R', '3': 'E', '4': 'A', '5': 'S', '6': 'b', '7': 'T', '8': 'B', '9': 'g'}


def txt_to_leet(txt_string):
    new_text = ''
    for i in txt_string:
        try:
            new_text += leet_dictionary[i]
        except:  # Si el caracter no está en el diccionario, simplemente lo agrega al nuevo string
            new_text += i
    print(new_text)


txt = 'Hola mundo! Mi nombre es cdnexx.'
txt_to_leet(txt.upper())
