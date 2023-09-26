# /*
#  * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
#  * Podrás configurar generar contraseñas con los siguientes parámetros:
#  * - Longitud: Entre 8 y 16.
#  * - Con o sin letras mayúsculas.
#  * - Con o sin números.
#  * - Con o sin símbolos.
#  * (Pudiendo combinar todos estos parámetros entre ellos)
#  */

import string
import secrets

def password(lenght: int , upperCase : bool, numbers: bool , simbols: bool):

    if lenght < 8: lenght = 8
    if lenght > 16: lenght =16 


    charactesSpecial = string.punctuation
    number = string.digits

    if upperCase:
        alphabet = string.ascii_uppercase
    else:
        alphabet = string.ascii_lowercase

    if numbers:
        alphabet += number
    else:
        alphabet = string.ascii_letters

    if simbols:
        alphabet += charactesSpecial
    else:
        alphabet = string.ascii_letters

    password = ''.join(secrets.choice(alphabet) for i in range(lenght))

    return password
           
                


print(password(7,True,True,True))

print(password(7,True,True,False))
print(password(7,False,True,True))
print(password(7,True,False,True))
