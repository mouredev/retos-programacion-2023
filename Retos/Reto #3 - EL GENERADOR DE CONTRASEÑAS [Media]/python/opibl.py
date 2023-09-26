import random
import string


def generar_contraseña(longitud_contraseña,cantidad_letras,cantidad__numeros,cantidad_simbolos):

    contraseña = []
    l = 0
    n = 0
    s = 0
    f = 0
    faltantes = longitud_contraseña - (cantidad__numeros + cantidad_letras + cantidad_simbolos)
        
    while(l < cantidad_letras):
        letra = random.choice(string.ascii_letters).upper()
        contraseña.append(letra)
        l = l + 1

    while(n < cantidad__numeros):
        numero = str(random.randint(0, 9))
        contraseña.append(numero)    
        n = n + 1

    while(s < cantidad_simbolos):
        simbolos = random.choice(string.punctuation)
        contraseña.append(simbolos)    
        s = s + 1

    while(f < faltantes):
        relleno = random.choice(string.ascii_letters).lower()
        contraseña.append(relleno)  
        f = f + 1

    random.shuffle(contraseña)
    texto = "".join(contraseña)
    print(texto)


longitud_contraseña = int(input("ingresa el largo de la contraseña (de 8 a 16)"))
while (1):
    if longitud_contraseña < 8 or longitud_contraseña > 16:
        longitud_contraseña = int(input("Igresa un numero valido (de 8 a 16)"))
    else:
        break    

cantidad_letras = int(input("¿cuantas letras mayusculas quieres? "))
cantidad__numeros = int(input("¿cuantos numeros quieres? "))
cantidad_simbolos = int(input("¿cuantos simbolos quieres? "))
suma = cantidad_letras + cantidad__numeros + cantidad_simbolos

if(suma > longitud_contraseña):
    print("Lo siento los parametros no son validos")
    exit(0)


generar_contraseña(longitud_contraseña,cantidad_letras,cantidad__numeros,cantidad_simbolos)
