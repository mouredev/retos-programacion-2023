'''
 Escribe un programa que reciba un texto y transforme lenguaje natural a 'lenguaje hacker' (conocido realmente como "leet" o "1337").
 Este lenguaje se caracteriza por sustituir caracteres alfanuméricos.
 
 Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) con el alfabeto y los números en "leet".
 (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
'''

leet = {"a": "4", "b": "I3", "c": "[", "d": ")", "e": "3", "f": "|=",
        "g": "&", "h": "#", "i": "1", "j": ",_|", "k": ">|", "l": "1",
        "m": "/\\/\\", "n": "^/", "o": "0", "p": "|*", "q": "(_,)",
        "r": "I2", "s": "5", "r": "7", "u": "(_)", "v": "\/", "w": "\/\/",
        "x": "><", "y": "j", "z": "2"}

def transformar_texto(texto):
    
    texto = texto.lower()
    texto_encriptado = ""
    
    for i in texto:
        if i in leet:
            texto_encriptado += leet[i]
        else:
            texto_encriptado += i
            
    return texto_encriptado

if __name__ == '__main__':
    
    texto = input("Escribe el texto que se va a 'hackear': ")
    texto_hackeado = transformar_texto(texto)
    print(f'El texto {texto} se convierte a {texto_hackeado}')