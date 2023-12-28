"""
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
"""
import string
import random
# Esta funcion pregunta es simplemente para ahorrar repetir líneas en las preguntas finales. La llamaré luego.
def pregunta(var):
    respuesta = input(
        f"¿Deseas la contraseña tenga {var} incluid@s ? Responde únicamente si o no. ")
    if respuesta == "si":
        return respuesta
    elif respuesta == "no":
        return respuesta
    else:
        print("Respuesta incorrecta. Solo se admite si o no. Repitiendo pregunta: ")
        respuesta = pregunta(var)
    return respuesta


# Aquí se hace el algoritmo. Dependiendo de las condiciones habrá un string total con todo lo elegido. De momento está ordenado.
# Con el string total, se elegirá una posición random por cada dígito de contraseña.
def generador_contraseñas(length, mayus, num, simbol):
    contraseña = ""
    stringtotal = ""
    stringtotal += string.ascii_letters if mayus == "si" else string.ascii_lowercase
    stringtotal += string.digits if num == "si" else ""
    stringtotal += string.punctuation if simbol == "si" else ""
    for i in range(length):
        contraseña += stringtotal[random.randint(0, len(stringtotal))]
    print(f"Tu contraseña es: {contraseña}")


# Aquí llama a todo en general, solo admite entre 8 y 16 de longitud y llama a la función "pregunta" por cada condición.
def llamar_a_funcion():
    length = int(input("Introduce la longitud de la contraseña. "))
    if length >= 8 and length <= 16:
        mayus = pregunta("Mayúsculas")
        num = pregunta("Números")
        simbol = pregunta("Simbol")
        generador_contraseñas(length, mayus, num, simbol)
    else:
        print("El tamaño tiene que ser entre 8 y 16. Introduce de nuevo.")
        llamar_a_funcion()


llamar_a_funcion()
