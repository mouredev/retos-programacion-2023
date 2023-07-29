import random
import string

def generar_contrasena(longitud, mayusculas=True, numeros=True, simbolos=True):
    cadena = string.ascii_letters
    if mayusculas:
        cadena += string.ascii_uppercase
    if numeros:
        cadena += string.digits
    if simbolos:
        cadena += string.punctuation

    if longitud < 8 or longitud > 16:
        raise ValueError("La longitud debe estar entre 8 y 16.")

    return ''.join(random.choice(cadena) for _ in range(longitud))

if __name__ == "__main__":
    try:
        longitud = int(input("Ingrese la longitud deseada para la contraseña (entre 8 y 16): "))
        mayusculas = input("Incluir letras mayúsculas? (Sí/No): ").strip().lower() == 'si'
        numeros = input("Incluir números? (Sí/No): ").strip().lower() == 'si'
        simbolos = input("Incluir símbolos? (Sí/No): ").strip().lower() == 'si'

        contrasena_generada = generar_contrasena(longitud, mayusculas, numeros, simbolos)
        print("Contraseña generada:", contrasena_generada)
    except ValueError as e:
        print("Error:", e)
