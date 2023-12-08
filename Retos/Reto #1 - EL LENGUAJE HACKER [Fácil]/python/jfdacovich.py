# Reto 1: El Lenguaje del Hacker

alphabet = {
    "a" : "(L", "b" : "!3", "c" : "[", "d" : "|>", "e" :  "€",
    "f" : "|=", "g" : "(_+", "h" : "#", "i" : "1", "j" : ",_]",
    "k" : ">|", "l" : "7", "m" : "nn", "n" : "{\}", "o" : "oh",
    "p" : "|7", "q" : "(_,)", "r" : "I2", "s" : "es", "t" : "-|-",
    "u" : "|_|", "v" : "\/", "w" : "\/\/", "x" : "ecks", "y" : "j",
    "z" : "%", "1" : "L", "2" : "R", "3" : "E", "4" : "A",
    "5" : "S", "6" : "b", "7" : "T", "8" : "B", "9" : "g",
    "0" : "o" 
}

def translator(texto):
    """
    Función que recibe un texto y lo convierte a lenguaje hacker,
    Dicho lenguaje se caracteriza por la sustitución de carácteres
    alfanuméricos.
    """
    converted_text = ""
    for letter in texto:
        if letter.lower() in alphabet:
            converted_text += alphabet[letter.lower()]
        else:
            converted_text += letter
    return(converted_text)

print(translator("jf_dev_01"))
    