def translate(source_language, text_to_translate):
    spanish = {
            'a': 'aurek', 'b': 'besh', 'c': 'cresh', 'd': 'dorn', 'e': 'esk', 
            'f': 'forn', 'g': 'grek', 'h': 'herf', 'i': 'isk', 'j': 'jenth', 
            'k': 'krill', 'l': 'leth', 'm': 'mern', 'n': 'nern', 'o': 'osk', 
            'p': 'peth', 'q': 'qek', 'r': 'resh', 's': 'senth', 't': 'trill', 
            'u': 'usk', 'v': 'vev', 'w': 'wesk', 'x': 'xesh', 'y': 'yirt', 
            'z': 'zerek', 'ch': 'cherek', 'æ': 'enth', 'eo': 'onith', 
            'kh': 'krenth', 'ng': 'nen', 'oo': 'orenth', 'sh': 'shen',
            'th': 'thesh'
            }
            
    aurebesh = {value: key for key, value in spanish.items()}
    translation = ""
    if source_language == "esp":
        for letter in text_to_translate:
            if letter in spanish: 
                translation += spanish[letter]
            else:
                translation += letter
    elif source_language == "aur":
        words = text_to_translate.split()
        for word in words:
            if word in aurebesh:
                translation += aurebesh[word]
            else:
                for letter in word:
                    if letter in aurebesh.values():
                        translation += list(aurebesh.keys())[list(aurebesh.values()).index(letter)]
                    else:
                        translation += letter
                translation += ""
    return translation

print("Bienvenido al traductor de Español y Aurebesh\n")
source_language = input("Selecciona el idioma de origen (esp/aur): ")
text_to_translate = input("Introducir texto a traducir:\n==>")
translation = translate(source_language, text_to_translate)
print("Traducción: ", translation)
