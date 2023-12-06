alfabeto = {
    'A': '4', 'B': '8', 'C': '(', 'D': '|)', 'E': '3', 'F': '|=', 'G': '9', 'H': '#', 'I': '1',
    'J': '_|','K': '|<', 'L': '|_', 'M': '/\/\\', 'N': '|\\|', 'O': '0', 'P': '|D', 'Q': '(,)',
    'R': '|2', 'S': '5', 'T': '7', 'U': '|_|', 'V': '\/', 'W': '\/\/', 'X': '><', 'Y': '`/',
    'Z': '2' }

def convert(text):
    texto_cambiado = ""
    for caracter in text.upper():
        if caracter in alfabeto:
            texto_cambiado += alfabeto[caracter]
        else:
            texto_cambiado += caracter
    
    return ("Original: ", text, "leet: ", texto_cambiado)

texto_convertir = input("Ingrese el texto a convertir:\n")
print(convert(texto_convertir))
