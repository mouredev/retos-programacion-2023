diccionarioleet = {
    "a":"4",
    "b":"|3",
    "c":"[",
    "d":")",
    "e":"3",
    "f":"|=",
    "g":"&",
    "h":"#",
    "i":"1",
    "j":",_|",
    "k":">|",
    "l":"1",
    "m":"/\/\\", #se corrige y se coloca un \ adicional
    "n":"^/",
    "o":"0",
    "p": "|*",
    "q":"(_,)",
    "r":"I2",
    "s":"5",
    "t":"7",
    "u":"(_)",
    "v":"\/",
    "w":"\/\/",
    "x":"><",
    "y":"j",
    "z":"2",
    "1":"l",
    "2":"Z",
    "3":"E",
    "4":"A",
    "5":"S",
    "6":"G",
    "7":"T",
    "8":"B",
    "9":"g",
    "0":"o",
    " ":" "
    }

palabra = input("Ingrese un texto: ")
palabraleet=""
for i in palabra.lower():
    if i in diccionarioleet:
        palabraleet += diccionarioleet[i]
    else: #con esta condición se contemplan los caracteres que no están en la lista
        palabraleet += i
        
print(palabraleet)   
