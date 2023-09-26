# /*
#  * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
#  * Podrás configurar generar contraseñas con los siguientes parámetros:
#  * - Longitud: Entre 8 y 16.
#  * - Con o sin letras mayúsculas.
#  * - Con o sin números.
#  * - Con o sin símbolos.
#  * (Pudiendo combinar todos estos parámetros entre ellos)
#  */
import random


def cantidad_caracteres():
    return random.randint(8,16)
def generar_simbolos():
    simbolos = "!@#%^&*()_+-=[]{};':\"|,.<>/?`~"
    return random.choice(simbolos)

def generar_letra():
    alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return random.choice(alfabeto)
def generar_numero():
    return random.randint(0,9)

def generar(val):
    contador=0
    my_pass=[]
    for i in range(val):
        if(contador!=val):
            caracter=random.randint(1,3)
            if(caracter==1):
                my_pass.append(str(generar_numero()))
            if(caracter==2):
                my_pass.append(str(generar_simbolos()))
            if(caracter==3):
                my_pass.append(generar_letra())
            contador+=1
    my_string = ''.join(my_pass)

    return my_string



print("Una posible contraseña para ti sería: "+generar(cantidad_caracteres()))


