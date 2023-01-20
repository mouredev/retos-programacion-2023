import random
import string
import numbers

def genera_contraseña(configuracion):
    simbolo = False
    mayusculas = False
    numero = False
    if "s" in configuracion:
        simbolo = True
    if "m" in configuracion:
        mayusculas = True
    if "n" in configuracion:
        numero = True
    longitud = int((((configuracion.replace("s", "")).replace("m", "")).replace("n", "")).replace("l", ""))
    if longitud > 9 and longitud < 17:
        contador = 0
        contraseña = ""
        while contador <= longitud:
            añadido = False
            prueba = random.randint(0, 3)
            match prueba:
                case 0:
                    if numero:
                        contraseña+= random.choice("123456789")
                        añadido = True
                case 1:
                    if simbolo:
                        contraseña+= random.choice(string.punctuation)
                        añadido = True  
                case 2:
                    if mayusculas:
                        contraseña+= random.choice(string.ascii_uppercase)
                        añadido = True
                case 3:
                    contraseña+= random.choice(string.ascii_lowercase)
                    añadido = True
                case _:
                    hola = "hola"
            if añadido:
                contador += 1
    else:
        contraseña = "Introduzca un número entre 10 y 16"        
    return contraseña


print(genera_contraseña("l16mns"))