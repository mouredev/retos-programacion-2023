import string
import random


def input_bool(tipo: str = None, repetir: bool = False, main: bool = False) -> bool:
    while True:
        if repetir:
            opcion = input("\nIngrese 'y' si quiere que se genere otra vez la contrasena o 'n' para quedarse con la contrasena generada: ")
        elif main:
            opcion = input("\nIngrese 'y' si quiere volver a ejecutar el generador con otros parametros o 'n' para salir del programa: ")
        else:
            opcion = input(f"\nIngrese 'y' para usar {tipo} o 'n' para no usar {tipo}: ")
        if opcion == '':
            print("No ingreso ningun caracter")
            continue
        if opcion not in 'yYnN':
            print("Ingrese unicamente 'y' o 'n'")
            continue
        else:
            return opcion in 'yY'


def input_usuario() -> (int, bool, bool, bool):
    print("\nA continuacion se te presentaran varias preguntas")
    print("Con el objetivo de saber como quieres tu contrasena")

    while True:
        try:
            largo = int(input("\nIngresa la longitud de la contrasena (entre 8 y 16): "))
            if largo < 8 or largo > 16:
                print("Valor ingresado fuera del rango permitido")
                continue
            break
        except Exception:
            print("No ingresaste numeros")
    
    mayus = input_bool('letras mayusculas')
    nums = input_bool('numeros')
    simbol = input_bool('simbolos')

    return largo, mayus, nums, simbol


def generate_password(largo: int, mayus: bool, nums: bool, simbol: bool) -> str:

    base_string = string.ascii_letters if mayus else string.ascii_lowercase  # Agregando letras
    base_string += string.digits if nums else ''  # Agregando numeros
    base_string += string.punctuation if simbol else ''  # Agregando simbolos 

    return ''.join([random.choice(base_string) for _ in range(largo)])


if __name__ == '__main__':
    # Flujo del programa
    print(f"{'#'*15} Password Generator {'#'*15}\n")

    while True:

        largo, mayus, nums, simbol = input_usuario()

        while True:
            password = generate_password(largo, mayus, nums, simbol)
            
            print(f"\nLa contrasena generada es: {password}\n")

            if input_bool(repetir=True):
                continue
            else:
                break
        
        if input_bool(main=True):
            continue
        else:
            break

