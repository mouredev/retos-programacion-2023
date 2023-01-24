# Reto #1: EL "LENGUAJE HACKER" en lenguaje python - Laker Garcia

def leet(texto):
  diccionario = {
    'a': '4',
    'b': 'I3',
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
    'm': 'm', # Se mantiene la misma letra para evitar error en warining errorLens
    'n': '1',
    'ñ': '~', # La letra eñe ha sido agregada para uso de palabras con esta en español
    'o': '0',
    'p': '|*',
    'q': '(_,)',
    'r': 'I2',
    's': '5',
    't': '7',
    'u': '(_)',
    'v': '5',
    'w': '7',
    'x': '9',
    'y': '1',
    'z': '2',
    '1': 'L',
    '2': 'R',
    '3': 'E',
    '4': 'A',
    '5': 'S',
    '6': 'b',
    '7': 'T',
    '8': 'B',
    '9': 'g',
    '0': 'o',
  }
  
  texto_leet = ''
  for palabra in texto.split():
    for letra in palabra:
      texto_leet += diccionario.get(letra, letra)
    texto_leet += ' '
  return texto_leet

texto = "Este programa imprime tambien en español"
texto_leet = leet(texto)
print(texto_leet)