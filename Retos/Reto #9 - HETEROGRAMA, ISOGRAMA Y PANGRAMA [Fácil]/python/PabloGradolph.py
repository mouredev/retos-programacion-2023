'''
/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */
 '''

def heterograma(text: str) -> str:
    letras = []
    text = text.lower()
    for letter in text:
        if letter != " ":
            if letter in letras:
                return "No se trata de un heterograma."
            else:
                letras.append(letter)
    return "Estamos ante un heterograma."

def isograma(text: str) -> str:
    letras = {}
    text = text.lower()
    for letter in text:
        if letter != " ":
            if letter in letras:
                letras[letter] += 1
            else:
                letras[letter] = 1
    
    nuevo_valor = letras[letter]
    for value in letras.values():
        if value != nuevo_valor:
            return "No se trata de un isograma."
    
    return f"Estamos ante un isograma de orden {nuevo_valor}."
    
def pangrama(text: str) -> str:
    text = text.lower()
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for letter in text:
        if letter in alfabeto:
            alfabeto.remove(letter)
    
    if len(alfabeto) == 0:
        return "Estamos ante un pangrama."
    else:
        return "No se trata de un pangrama."
    
def main():
    textos = []
    text1 = "qwertyuiopñlkjhgfdsazxcvbnm ñalsdhfadjadkf"
    text2 = "qwertyuiopñlkjhgfdsazxcvbnm"
    text3 = "mama"
    text4 = "Hola esto es un texto cualquiera a ver si cumple alguna de las condiciones anteriores."
    textos.append(text1)
    textos.append(text2)
    textos.append(text3)
    textos.append(text4)
    i = 1
    for texto in textos:
        print(f"TEXTO {i}")
        print(heterograma(texto))
        print(isograma(texto))
        print(pangrama(texto))
        print()
        i += 1

if __name__ == "__main__":
    main()
