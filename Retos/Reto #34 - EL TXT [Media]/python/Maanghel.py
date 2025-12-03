"""
Crea un programa capaz de interactuar con un fichero TXT.
IMPORTANTE: El fichero TXT NO debe subirse como parte de la corrección.
Únicamente el código.

- Si no existe, debe crear un fichero llamado "text.txt".
- Desde el programa debes ser capaz de introducir texto por consola y guardarlo
    en una nueva línea cada vez que se pulse el botón "Enter".
- Si el fichero existe, el programa tiene que dar la opción de seguir escribiendo
    a continuación o borrar su contenido y comenzar desde el principio.
- Si se selecciona continuar escribiendo, se tiene que mostrar por consola
    el texto que ya posee el fichero. 
"""

import os

def main() -> None:
    """
    Programa para interactuar con un fichero TXT.

    returns:
        None
    """
    filename = "text.txt"

    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            pass
        print(f'Se ha creado el fichero "{filename}". Puedes comenzar a escribir:')
    else:
        print(f'El fichero "{filename}" ya existe.')
        choice = input("¿Deseas (c)ontinuar escribiendo o (b)orrar el contenido y comenzar de nuevo? (c/b): ").strip().lower()
        
        if choice == 'c':
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()
                print("Contenido actual del fichero:")
                print(content)
            print("Puedes continuar escribiendo:")
        elif choice == 'b':
            with open(filename, "w", encoding="utf-8") as f:
                pass
            print("El contenido del fichero ha sido borrado. Puedes comenzar a escribir:")
        else:
            print("Opción no válida. Saliendo del programa.")
            return

    with open(filename, "a", encoding="utf-8") as f:
        while True:
            try:
                line = input()
                f.write(line + "\n")
            except KeyboardInterrupt:
                print("\nSaliendo del programa.")
                break


if __name__ == "__main__":
    main()
