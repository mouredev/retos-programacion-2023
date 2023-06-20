


"""
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
"""

def leet_translator(texto):
    texto = texto.lower()
    leet_dict = {
        'A':'4','B':'I3','C':'[','D':')','E':'3','F':'|=','G':'&','H':'#','I':'1','J':',_|','K':'>|','L':'1','M':'/\/\ ','N':'^/','O':'0',
        'P':'|*','Q':'(_,)','R':'I2','S':'5','T':'7','U':'(_)','V':'\/','W':'\/\/','X':'><',
        'Y':'j','Z':'2','0':'O','1':'I','2':'Z','3':'E','4':'A','5':'S','6':'b','7':'T','8':'B','9':'g'}
    leet_traducido = ""
    
    for letra in texto:
        if letra == ' ': 
            leet_traducido += letra
        for clave,valor in leet_dict.items():
            if letra.lower() == clave.lower():
                leet_traducido += valor

    return(leet_traducido)

print(leet_translator('El Lenguaje Hacker Del Programador'))



