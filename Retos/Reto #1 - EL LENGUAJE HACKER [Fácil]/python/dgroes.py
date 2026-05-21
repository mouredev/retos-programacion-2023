# reto 1: El lenguaje Hacker 💀
# dgroes

text = "Hola, soy un texto cualquiera. Saudos"

def trans_to_hacker(text):
    letters = {"A": "4", "B": "ß", 'C': "¢", "D": "[)", "E": "£", "F": "ƒ", "G": "6", "H": "}{", "I": "!",
               "J": "_|", "K": "1<", "L": "|", "M": "^^", "N": "И", "O": "0", "P": "|*", "Q": "(_,)", "R": "Я",
               "S": "$", "T": "7", "U": "v", "V": "u", "W": "Ш", "X": "×", "Y": "Ч", "Z": "2"}
    
    upper_text = text.upper()
    
    word_list = list(upper_text)

    final = [letters.get(item, item) for item in word_list]

    final = "".join(final)
    return final

print(trans_to_hacker(text))