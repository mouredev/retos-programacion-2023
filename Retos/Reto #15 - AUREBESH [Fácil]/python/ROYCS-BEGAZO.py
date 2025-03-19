aurebesh_dict = {
    'a': 'α', 'b': 'β', 'c': '¢', 'd': 'δ', 'e': 'ε', 'f': 'ϝ',
    'g': 'ɣ', 'h': 'ħ', 'i': 'ι', 'j': 'ʝ', 'k': 'κ', 'l': 'λ',
    'm': 'μ', 'n': 'η', 'o': 'ο', 'p': 'π', 'q': 'ϙ', 'r': 'ρ',
    's': 'ς', 't': 'τ', 'u': 'υ', 'v': 'ν', 'w': 'ω', 'x': 'χ',
    'y': 'ϒ', 'z': 'ζ', ' ': ' ', '.': '.', ',': ','
}#diccionario alternativo

def aurebesh(text):
    return ''.join(aurebesh_dict.get(char.lower(), char ) for char in text)

tex = input('ingrese un mensaje ')
print(aurebesh(tex))