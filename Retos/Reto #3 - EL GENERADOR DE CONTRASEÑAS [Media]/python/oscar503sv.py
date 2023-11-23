import random
import string

def generar_contrasena(longitud, usa_mayusculas, usa_numeros, usa_simbolos):
    caracteres = string.ascii_letters if usa_mayusculas else string.ascii_lowercase
    caracteres += string.digits if usa_numeros else ''
    caracteres += string.punctuation if usa_simbolos else ''
    
    if not (usa_mayusculas or usa_numeros or usa_simbolos):
        print("Debes habilitar al menos una de las opciones: mayúsculas, números o símbolos.")
        return
    
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def main():
    print("Generador de contraseñas aleatorias")
    
    while True:
        try:
            longitud = int(input("Longitud de la contraseña (entre 8 y 16): "))
            if 8 <= longitud <= 16:
                break
            else:
                print("La longitud debe estar entre 8 y 16.")
        except ValueError:
            print("Ingrese un número válido.")
    
    usa_mayusculas = input("¿Incluir letras mayúsculas? (Sí/No): ").strip().lower() == 'si'
    usa_numeros = input("¿Incluir números? (Sí/No): ").strip().lower() == 'si'
    usa_simbolos = input("¿Incluir símbolos? (Sí/No): ").strip().lower() == 'si'
    
    contrasena = generar_contrasena(longitud, usa_mayusculas, usa_numeros, usa_simbolos)
    
    if contrasena:
        print(f"Tu contraseña generada es: {contrasena}")
    else:
        print("No se pudo generar una contraseña válida.")

if __name__ == "__main__":
    main()
