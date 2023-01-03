
# tabla de decodificacion
hack = {"a":"4", "b":"I3", "c":"[", "d":")", "e":"3", 
        "f":"|=", "g":"&", "h":"#", "i":"1", "j":",_|", 
        "k":">|", "l":"£", "m":"/\/\\", "n":"^/", "o":"0", 
        "p":"|*", "q":"(_,)", "r":"I2", "s":"5", "t":"7",
        "u":"(_)", "v":"\|", "w":"\/\/", "x":"><", "y":"j",
        "z":"2", "1":"L", "2":"R", "3":"E", "4":"A", "5":"S", 
        "6":"b", "7": "T", "8":"B", "9":"g", "0":"o"," ":" " }

def hackleet(word):
    """ La funcion recive una cadena str y al decodifica con la con la lista hack
    por ejemplo cambia las a por 4 , o las p por  |*   todo los que esta en el 
    diccionarion  hack """ 

    word = word.lower()
    word_hack = [hack[i] for i in word]
    print(("").join(word_hack))


if __name__=="__main__":

    word = input("Ingrese la palabra a encryptar: ")
    hackleet(word)




