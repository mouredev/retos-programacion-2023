def humano2aurebesh(text):
    text = text.lower()
    dictionary = {"a":"aurek", "b":"besh", "c":"cresh", "d":"dorn", "e":"esk", "f":"forn",
                  "g":"grek", "h":"herf", "i":"isk", "j":"jenth", "k":"krill", "l":"leth",
                  "m":"mern", "n":"nern", "o":"osk", "p":"peth", "q":"qek", "r":"resh",
                  "s":"senth", "t":"trill", "u":"usk", "v":"vev", "w":"wesk", "x":"xesh",
                  "y":"yirt", "z":"zerek"}
    
    cadena_aurebesh = ""

    if opcion == 1:
        for i in text:
            if i in dictionary.keys():
                cadena_aurebesh += dictionary[i]
            else:
                cadena_aurebesh += i

        print(cadena_aurebesh)

    if opcion == 2:
        for key, value in dictionary.items():
            text = text.replace(value, key)

        print(text)

print("""Op 1. Humano a aurebesh
Op 2. Aurebesh a humano""")
opcion = int(input("Elige 1 o 2: "))
text = input("Text a Traducir: ")

humano2aurebesh(text)
