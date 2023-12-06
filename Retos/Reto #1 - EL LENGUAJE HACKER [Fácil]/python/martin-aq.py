def translate_to_leet(string):
    
    leet_string = ""
    
    hashMap = {
        "a": "4", "b": "|3", "c": "[", "d": ")", "e": "3", "f": "|=", "g": "&", "h": "#",
        "i": "1", "j": ",_|", "k": ">|", "l": "1", "m": "|V|","n": "^/", "o": "0", "p": "|*",
        "q": "(_,)", "r": "|2", "s": "5", "t": "7", "u": "(_)", "v": "|/", "w": "VV",
        "x": "><", "y": "j", "z": "2", "1": "L", "2": "R", "3": "E", "4": "A", "5": "S",
        "6": "b", "7": "T", "8": "B", "9": "g", "0": "o"
    }
    
    for word in string.lower():
        if word in hashMap.keys():
            leet_string += hashMap[word]
        else:
            leet_string += word
    
    return leet_string

print(translate_to_leet(input("Ingrese una cadena de texto: ")))