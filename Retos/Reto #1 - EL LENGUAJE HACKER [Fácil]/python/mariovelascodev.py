def leet (text):
    #Convertir el texto en una lista y en minúsculas
    text_list = list(text.lower())

    """
    Creamos una variable donde almacenar la conversion a lenguaje hacker
    y un diccionario con el lenguaje hacker
    """
    leet=""
    my_dictionary_leet = {"a":"4", "b": "I3", "c":"[", "d":")", "e": "3", "f":"|=", 
                        "g":"&", "h":"#", "i":"1", "j":",_|", "k": ">|", "l":"1", 
                        "m":"/\\/\\","n":"^/", "o":"0", "p":"|*", "q":"(_,)", "r":"I2", 
                        "s":"5", "t":"7", "u":"(_)", "v":"\/", "w":"\/\/", "x":"><", 
                        "y":"j", "z":"2", "1":"L", "2":"R", "3":"E", "4": "A", "5": "S",
                        "6":"b", "7":"T", "8": "B", "9": "g", "0": "o", " ":" "}
    
    #Comprobar cada valor de la lista y convertirlo a lenguaje hacker
    for character in text_list:
        for value_dictionary in my_dictionary_leet:
            if character == value_dictionary:
                leet +=my_dictionary_leet[value_dictionary]

    return leet

print(leet("Leet"))
print(leet("El Lenguaje hacker"))