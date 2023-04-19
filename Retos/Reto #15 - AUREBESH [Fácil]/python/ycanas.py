def aurebesh_translator(text: str, aurebesh: bool = True) -> str:    
    to_aurebesh = {
        "a": "aurek",  "b": "besh",    "c": "cresh",
        "d": "dorn",   "e": "esk",     "f": "forn",
        "g": "grek",   "h": "herf",    "i": "isk",
        "j": "jenth",  "k": "krill",   "l": "leth",
        "m": "merm",   "n": "nern",    "o": "osk",
        "p": "peth",   "q": "qek",     "r": "resh",
        "s": "senth",  "t": "trill",   "u": "usk",
        "v": "vev",    "w": "wesk",    "x": "xesh",
        "y": "yirt",   "z": "zerek",   "ae": "enth",
        "eo": "onith", "kh": "krenth", "oo": "orenth",
        "sh": "sen",   "th": "thesh",  "ng": "nen"
    }

    text = text.lower()
    length = len(text)
    translate = ""

    if aurebesh:
        to_spanish = {value: key for key, value in to_aurebesh.items()}
        translate = text

        for key, value in to_spanish.items():
            translate = translate.replace(key, value)

    else:
        index = 0
        
        while index < length:
            if index < length - 1:
                search = text[index: index + 2]

            if search not in to_aurebesh:
                search = text[index]
                index = index - 1

            translate += to_aurebesh.get(search, search)
            index = index + 2
            search = None

    return translate


aurebesh = aurebesh_translator("hola mundo desde aurebesh", False)
spanish = aurebesh_translator(aurebesh)
print(aurebesh, spanish)
