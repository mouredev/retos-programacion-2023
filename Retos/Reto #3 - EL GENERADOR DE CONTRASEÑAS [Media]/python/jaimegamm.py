import random
import string

def generar_contrasena(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos):
    caracteres = string.ascii_letters if incluir_mayusculas else string.ascii_lowercase
    caracteres += string.digits if incluir_numeros else ''
    caracteres += string.punctuation if incluir_simbolos else ''

    if len(caracteres) == 0:
        print("Error: Debes incluir al menos un tipo de caracter en la contraseña.")
        return None

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def main():
    print("Generador de Contraseñas Aleatorias")
    longitud = int(input("Longitud de la contraseña (entre 8 y 16): "))
    incluir_mayusculas = input("¿Incluir letras mayúsculas? (si/no): ").lower() == 'si'
    incluir_numeros = input("¿Incluir números? (si/no): ").lower() == 'si'
    incluir_simbolos = input("¿Incluir símbolos? (si/no): ").lower() == 'si'

    if 8 <= longitud <= 16:
        contrasena = generar_contrasena(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos)
        if contrasena:
            print("Contraseña generada: ", contrasena)
    else:
        print("Error: La longitud de la contraseña debe estar entre 8 y 16.")

if __name__ == "__main__":
    main()