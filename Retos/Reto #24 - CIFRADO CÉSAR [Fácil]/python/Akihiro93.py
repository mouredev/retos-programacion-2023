def cesar (text):
    keyword = {
        'a': 'f', 'b': 'g', 'c': 'h',
        'd': 'i', 'e': 'j', 'f': 'k',
        'g': 'l', 'h': 'm', 'i': 'n',
        'j': 'o', 'k': 'p', 'l': 'q',
        'm': 'r', 'n': 's', 'o': 't',
        'p': 'u', 'q': 'v', 'r': 'w',
        's': 'x', 't': 'y', 'u': 'z',
        'v': 'a', 'w': 'b', 'x': 'c',
        'y': 'd', 'z': 'e', " ": "  "
    }
    encoded = ""
    for i in text:
        encoded += keyword[i]
    return encoded


Input = input("Texto a cifrar: ")
print(cesar(Input))