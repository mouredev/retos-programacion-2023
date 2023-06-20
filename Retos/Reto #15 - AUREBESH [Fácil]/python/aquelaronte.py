import re

def aurebesh():
    caracteres_espanol = {
        'a' : 'aurek',
        'b' : 'besh',
        'c' : 'cresh',
        'd' : 'dorn',
        'e' : 'esk',
        'f' : 'forn',
        'g' : 'grek',
        'h' : 'herf',
        'i' : 'isk',
        'j' : 'jenth',
        'k' : 'krill',
        'l' : 'leth',
        'm' : 'mern',
        'n' : 'nern',
        'o' : 'osk',
        'f' : 'feth',
        'q' : 'qek',
        'r' : 'resh',
        's' : 'senth',
        't' : 'trill',
        'u' : 'usk',
        'v' : 'vek',
        'w' : 'wesk',
        'x' : 'xesh',
        'y' : 'yirt',
        'z' : 'zerek',
    }

    caracteres_aurebesh = {}

    for keys, values in caracteres_espanol.items():
        caracteres_aurebesh[values] = keys

    opcion = input('Bienvenido usuario, ingrese la opción que desee hacer\n1.Español a Aurebesh\n2.Aurebesh a Español\n')
    prompt = input('Ingrese la palabra que desee traducir\n').lower()
    output = ''

    if opcion == '1':
        for caracter in prompt:
            try:
                output += caracteres_espanol[caracter]
            except:
                output += caracter.lower()
    elif opcion == '2':
        indice = 0
        palabras = []
        while indice < len(prompt):
            try:
                palabras.append(prompt[indice:indice + len(caracteres_espanol[prompt[indice]])])
            except:
                palabras.append(prompt[indice])

            indice += len(palabras[-1])
        
        for palabra in palabras:
            try:
                output += caracteres_aurebesh[palabra]
            except:
                output += palabra


    
    print(output.capitalize())

if __name__ == '__main__':
    aurebesh()
