DICTIONARY = {
    "0": [" "],
    "1": [".", ",", "?", "!"],
    "2": ["A", "B", "C"],
    "3": ["D", "E", "F"],
    "4": ["G", "H", "I"],
    "5": ["J", "K", "L"],
    "6": ["M", "N", "O"],
    "7": ["P", "Q", "R", "S"],
    "8": ["T", "U", "V"],
    "9": ["W", "X", "Y", "Z"]
}


def get_letter(key):
    num = key[0]
    times_num = len(key)

    if not num in DICTIONARY:
        raise ValueError("Número inválido")
    
    return DICTIONARY[num][times_num - 1]


def t9_2_text(t9):
    if not t9:
        raise ValueError("Error: cadena vacía, escriba algo")
    
    t9_list = t9.split("-")

    text = ""
    for i in t9_list:
        letter = get_letter(i)
        text += letter

    return text.title()


print(t9_2_text("44-666-555-2-0-99-3"))
