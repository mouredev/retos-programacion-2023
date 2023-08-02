
def ceasar_cypher(phrase: str, shift: int, crypt: bool):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 
                'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 
                'X', 'Y', 'Z']
    
    phrase = phrase.upper()
    
    new_phrase = ''
    
    for s in phrase:
        if s in alphabet:
            if crypt:
                new_pos = alphabet.index(s) + shift
            else:
                new_pos = alphabet.index(s) - shift
            new_s = alphabet[new_pos % len(alphabet)]
            new_phrase += new_s
        else:
            new_phrase += s
    
    return new_phrase
        


print(ceasar_cypher('HOLA COMO ESTAS?', 3, True))

print(ceasar_cypher('KRÑD FROR HVWDV?', 3, False))