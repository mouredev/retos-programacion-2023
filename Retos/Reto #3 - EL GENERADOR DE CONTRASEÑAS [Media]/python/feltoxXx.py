# Reto #3: EL GENERADOR DE CONTRASEÑAS

# 
# Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
# Podrás configurar generar contraseñas con los siguientes parámetros:
# - Longitud: Entre 8 y 16.
# - Con o sin letras mayúsculas.
# - Con o sin números.
# - Con o sin símbolos.
# (Pudiendo combinar todos estos parámetros entre ellos)
#

import argparse
import random
import string

def generar_contrasena(longitud, incluir_mayusculas=True, incluir_numeros=True, incluir_simbolos=True):
    try:
        if 8 <= longitud <= 16:
            caracteres = string.ascii_lowercase  # caracteres en minúsculas

            if incluir_mayusculas:
                caracteres += string.ascii_uppercase  # agregar caracteres en mayúsculas
            if incluir_numeros:
                caracteres += string.digits  # agregar números
            if incluir_simbolos:
                caracteres += string.punctuation  # agregar símbolos

            if not (incluir_mayusculas or incluir_numeros or incluir_simbolos):
                print(f"\nAñade el parámetro -h o --help para conocer las opciones.\n")

            contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
            print(f"Contraseña generada: {contrasena}")
        else:
            raise ValueError("La longitud de la contraseña debe estar entre 8 y 16 caracteres.")
      
    except:
        print("La longitud de la contraseña debe estar entre 8 y 16 caracteres.")

    
    

def main():
    parser = argparse.ArgumentParser(description="Generador de contraseñas aleatorias")
    parser.add_argument("-l", "--longitud", type=int, default=8, help="Longitud de la contraseña")
    parser.add_argument("-m", "--mayusculas", action="store_true", help="Incluir letras mayúsculas")
    parser.add_argument("-n", "--numeros", action="store_true", help="Incluir números")
    parser.add_argument("-s", "--simbolos", action="store_true", help="Incluir símbolos")

    args = parser.parse_args()

    generar_contrasena(args.longitud, args.mayusculas, args.numeros, args.simbolos)

    

if __name__ == "__main__":
    main()
