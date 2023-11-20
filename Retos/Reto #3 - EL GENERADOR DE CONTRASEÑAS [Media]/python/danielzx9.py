
'''```
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
```
'''
 
import string
import random

def contra(longitudContra, mayus, numeros, simbol):
    caracteres = string.ascii_lowercase
    if mayus:
        caracteres += string.ascii_uppercase
    if numeros:
        caracteres += string.digits
    if simbol:
        caracteres += string.punctuation

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitudContra))
    return contrasena

def main():
    longitudContra = int(input("Ingrese la longitud que desea para la contraseña (entre 8 y 16): "))
    if not (8 <= longitudContra <= 16):
        print("Longitud no válida. Debe estar entre 8 y 16 caracteres.")
        return

    mayus = input("Incluir letras mayúsculas (si/no): ").lower() == 'si'
    numeros = input("Incluir números (si/no): ").lower() == 'si'
    simbol = input("Incluir símbolos (si/no): ").lower() == 'si'

    contrasena = contra(longitudContra, mayus, numeros, simbol)
    print(f"\nContraseña generada: {contrasena}")

if __name__ == "__main__":
    main()
