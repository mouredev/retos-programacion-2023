dictLeet={
    "a":"4","b":"I3","c":"[","d":")","e":"3","f":"|=","g":"&",
    "h":"#","i":"1","j":",|","k":">|","l":"1","m":"/\/\\","n":"^/","o":"0",
    "p":"|*","q":"(,)","r":"I2","s":"5","t":"7","u":"(_)","v":"/","w":"//",
    "x":"><","y":"j","z":"2"
}

def reemplazar_caracteres_especiales(texto : str) -> str:
    dictCaractEspeciales = {'á' : 'a', 'é' :'e','í':'i', 'ó':'o', 'ú':'u', 'ü':'u', 'ñ': 'n'}
    textoSinCaractEspeciales = ""
    for caracter in texto:
        letraLimpia = dictCaractEspeciales.get(caracter.lower())
        if letraLimpia:
            textoSinCaractEspeciales += letraLimpia
        else:
            textoSinCaractEspeciales += caracter
    return textoSinCaractEspeciales

def traducir_a_leet(texto : str) -> str :
    textoLeet = ""
    for caracter in texto:
        letraLeet = dictLeet.get(caracter.lower())
        if letraLeet:
            textoLeet += letraLeet
        else:
            textoLeet += caracter
    return textoLeet
    

if __name__ == "__main__":
    textoIngresado = input("Ingrese un texto: ")
    textoLimpio = reemplazar_caracteres_especiales(textoIngresado)
    textoLeet = traducir_a_leet(textoLimpio)
    print(textoLeet)