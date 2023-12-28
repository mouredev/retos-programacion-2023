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
    "ae": "enth",
    "ch": "cherek",
    "eo": "onith",
    "kh": "krenth",
    "ng": "nen",
    "oo": "orenth",
    "sh": "shen",
    "th": "thesh",
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


def spanish_aurebesh(sentence):
    traduction_aurebesh = []
    two_letters_sign = False
    for i in range(len(sentence)):
        character = sentence[i]

        if i < (len(sentence)) - 1:
            character_plus = sentence[i + 1]
            two_letters = character + character_plus

        if two_letters_sign == False:
            for aurebesh_character in Aurebesh_alphabet:
                if two_letters == aurebesh_character:
                    traduction_aurebesh.append(Aurebesh_alphabet[aurebesh_character])

                    two_letters_sign = True
                    break
                elif (
                    two_letters != aurebesh_character
                    and character == aurebesh_character
                ):
                    traduction_aurebesh.append(Aurebesh_alphabet[aurebesh_character])
        else:
            two_letters_sign = False
    return traduction_aurebesh


def aurebesh_spanish(sentence):
    traduction_spanish = []
    character_search = ""
    for i in range(len(sentence)):
        character = sentence[i]
        character_search = character_search + character
        print(character_search)
        for aurebesh_key, aurebesh_value in Aurebesh_alphabet.items():
            if character_search == aurebesh_value:
                traduction_spanish.append(aurebesh_key)
                character_search=""

    return traduction_spanish


def main():
    opcion = get_traduction()
    sentence = get_sentence()

    if opcion == 1:
        list_aurebesh = spanish_aurebesh(sentence)
        string_aurebesh = "".join(map(str, list_aurebesh))
        print("Traducido a Aurebesh: ", string_aurebesh)

    elif opcion == 2:
        list_spanish = aurebesh_spanish(sentence)
        string_spanish = "".join(map(str, list_spanish))
        print("Traducido a Español: ", string_spanish)


if __name__ == "__main__":
    main()
