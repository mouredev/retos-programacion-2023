def word_leet(word):
    dicc =  {'a': '4',
    'b': '13',
    'c': '[',
    'd': ')',
    'e': '3',
    'f': '|=',
    'g': '&',
    'h': '#',
    'i': '1',
    'j': ',_|',
    'k': '>|',
    'l': '1',
    'm': '"/\/\"',
    'n': '^/',
    'o': '0',
    'p': '|*',
    'q': '(_,)',
    'r': '12',
    's': '5',
    't': '7',
    'u': '(_)',
    'v': '\/',
    'w': '\/\/',
    'x': '><',
    'y': 'j',
    'z': '2',
    ' ': ' '}

    resultado=""
    for letter in word:
      if letter in (dicc):
        resultado += dicc.get(letter)
      else:
        print(f"Error: caracter invalido {letter}")
    return resultado





if __name__ == "__main__":
    word = "ingrese palabra a convertir"
    print(word_leet(word.lower()))