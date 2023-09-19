"""/*
 * Crea una función que sea capaz de transformar Español al lenguaje básico del universo
 * Star Wars: el "Aurebesh".
 * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 * - También tiene que ser capaz de traducir en sentido contrario.
 *  
 * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
 *
 * ¡Que la fuerza os acompañe!
 */"""

Aurebesh_alphabet = { 
    " ": " ",
    "a": "aurek",
    "b": "besh",
    "c": "cresh",
    "d": "dorn",
    "e": "esk",
    "f": "forn",
    "g": "grek",
    "h": "herf",
    "i": "isk",
    "j": "jenth",
    "k": "krill",
    "l": "leth",
    "m": "mern",
    "n": "nern",
    "o": "osk",
    "p": "peth",
    "q": "qek",
    "r": "resh",
    "s": "senth",
    "t": "trill",
    "u": "usk",
    "v": "vev",
    "w": "wesk",
    "x": "xesh",
    "y": "yirt",
    "z": "zerek", 
    "ae": "enth", 
    "ch": "cherek",
    "eo": "onith",
    "kh": "krenth",
    "ng": "nen",
    "oo": "orenth",
    "sh": "shen",
    "th": "thesh",
}
def get_sentence():
    return input("Escribe tu frase: ")

def get_traduction():
    opcion = 0
    while opcion != 1 and opcion != 2:
        print("1- Español -> Aurebesh\n2- Aurebesh -> Español\n")
        try:
            opcion = int(input("Introduce tu opcion: "))
        except ValueError:
            print(opcion)
    return opcion

def spanish_aurenesh(sentence):
    traduction_aurenesh = []
    two_letters = 0
    for character in sentence:
        for i in Aurebesh_alphabet:
            if character == i:
                traduction_aurenesh.append(Aurebesh_alphabet[i])
    return traduction_aurenesh
def main():
    opcion = get_traduction()
    sentence = get_sentence()
    if opcion == 1:
        list_aurenesh =(spanish_aurenesh(sentence))
        string_aurenesh = ''.join(map(str, list_aurenesh))
        print(string_aurenesh)
"""    elif opcion == 2:
        print(aurenesh_spanish(sentence))"""
    
    
if __name__ == "__main__":
    main()