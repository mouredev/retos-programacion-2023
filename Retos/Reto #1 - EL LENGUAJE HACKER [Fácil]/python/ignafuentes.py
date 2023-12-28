def traductor_hacker(texto):

    lenguaje = {'a': '4', 'b': 'I3', 'c': '[', 'd': ')', 'e': '3', 'f': '|=', 'g': '&', 'h': '#', 'i': '1', 'j': ',_|', 'k': '>|', 'l': '1', 'm': 'JVI', 'n': '^/', 'o': '0', 'p': '|*', 'q': '(_,)', 'r': 'I2', 's': '5', 't': '7', 'u': '(_)', 'v': '\/', 'w': '\/\/', 'x': '><', 'y': 'j', 'z': '2'  }

    texto_traducido = ''

    for caracter in texto:
        if caracter.lower() in lenguaje.keys():
            texto_traducido += lenguaje[caracter.lower()]
        else:
            texto_traducido += caracter
        
    return texto_traducido


print(traductor_hacker('Hola a todo el mundo!'))
print(traductor_hacker(input('Ingresar el texto a traducir => ')))