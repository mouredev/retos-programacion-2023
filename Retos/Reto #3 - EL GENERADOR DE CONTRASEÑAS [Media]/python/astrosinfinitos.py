# Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
#  Podrás configurar generar contraseñas con los siguientes parámetros:
# - Longitud: Entre 8 y 16.# -
# Con o sin letras mayúsculas.
# - Con o sin números.
# - Con o sin símbolos
#  (Pudiendo combinar todos estos parámetros entre ellos)

import random
import string


def generar_contraseña():
    """Generar contraseñas aleatorias según los parámetros del usuario."""

    while True:
        try:
            longitud = int(input("Ingrese longitud de contraseña (entre 8 y 16): "))
            if 8 <= longitud <= 16:
                break
            else:
                print("Error: la longitud debe estar entre 8 y 16")
        except ValueError:
            print("Debe ingresar un valor válido")

    while True:
        opcion = input(
            "Elija una opción:\n"
            "1. Solo minúsculas\n"
            "2. Minúsculas y mayúsculas\n"
            "3. Minúsculas y números\n"
            "4. Minúsculas y símbolos\n"
            "5. Combinar todo\n"
            "Ingrese el número de la opción deseada: "
        )
        if opcion in ("1", "2", "3", "4", "5"):
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 5")

    caracteres = string.ascii_lowercase  # Siempre incluimos minúsculas dentro de la contraseña generada

    if opcion == "2":
        caracteres += string.ascii_uppercase
    elif opcion == "3":
        caracteres += string.digits
    elif opcion == "4":
        caracteres += string.punctuation
    elif opcion == "5":
        caracteres += string.ascii_uppercase + string.digits + string.punctuation

    # Generar contraseña hasta que cumpla los requisitos
    while True:
        contrasena = "".join(random.choice(caracteres) for _ in range(longitud))
        cumple_requisitos = True
        if opcion == "2" and not any(c.isupper() for c in contrasena):
            cumple_requisitos = False
        if opcion == "3" and not any(c.isdigit() for c in contrasena):
            cumple_requisitos = False
        if opcion == "4" and not any(c in string.punctuation for c in contrasena):
            cumple_requisitos = False
        if opcion == "5":
            if (
                not any(c.isupper() for c in contrasena)
                or not any(c.isdigit() for c in contrasena)
                or not any(c in string.punctuation for c in contrasena)
            ):
                cumple_requisitos = False
        if cumple_requisitos:
            break

    print("Contraseña generada: ", contrasena)


if __name__ == "__main__":
    generar_contraseña()
