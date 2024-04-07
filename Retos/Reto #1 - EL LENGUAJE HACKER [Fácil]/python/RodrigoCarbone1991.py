text = input("Introduce un texto: ")

leet_table = {
    'a': '4',
    'b': '8',
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
    'm': '/\/',
    'n': '^/',
    'o': '0',
    'p': '|*',
    'q': '(_,)',
    'r': '|2',
    's': '5',
    't': '7',
    'u': '(_)',
    'v': '\/',
    'w': '\/\/',
    'x': '><',
    'y': 'j',
    'z': '2',
}
    
    
leet_text = ""

for c in text:
    if c.lower() in leet_table:
        leet_text += leet_table[c.lower()]
print("Leet Alphabet: ", leet_text)
