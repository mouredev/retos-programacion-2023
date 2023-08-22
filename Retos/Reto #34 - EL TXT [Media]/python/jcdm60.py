# Reto #34: El TXT
#### Dificultad: Media | Publicación: 21/08/23 | Corrección: 28/08/23

## Enunciado

#
# Crea un programa capaz de interactuar con un fichero TXT.
# IMPORTANTE: El fichero TXT NO debe subirse como parte de la corrección. 
# Únicamente el código.
# 
# - Si no existe, debe crear un fichero llamado "text.txt".
# - Desde el programa debes ser capaz de introducir texto por consola y guardarlo
#   en una nueva línea cada vez que se pulse el botón "Enter".
# - Si el fichero existe, el programa tiene que dar la opción de seguir escribiendo
#   a continuación o borrar su contenido y comenzar desde el principio.
# - Si se selecciona continuar escribiendo, se tiene que mostrar por consola
#   el texto que ya posee el fichero.  
#

class FileEditor:
    def __init__(self, filename):
        self.filename = filename
        self.file_exists = False

        try:
            with open(self.filename, "r"):
                self.file_exists = True
        except FileNotFoundError:
            pass

        if not self.file_exists:
            with open(self.filename, "w"):
                pass

    def write_text(self, text):
        with open(self.filename, "a") as file:
            file.write(text + "\n")
        print("Texto guardado.")

    def continue_writing(self):
        with open(self.filename, "r") as file:
            existing_text = file.read()
            print("Texto actual en el archivo:\n")
            print(existing_text)

        text = input("\nIntroduce el texto adicional: ")
        
        self.write_text(text)

    def clear_and_start_over(self):
        with open(self.filename, "w"):
            pass
        
        print("Contenido borrado. Puedes empezar a escribir desde el principio.")

    def run_program(self):
        while True:
            
            print("\n1. Escribir nuevo texto")
            
            if self.file_exists:
                print("2. Continuar escribiendo")
                print("3. Borrar contenido y empezar desde el principio")
            print("4. Salir")

            choice = input("Selecciona una opción: ")

            if choice == "1":
                text = input("Introduce el texto: ")
                self.write_text(text)

            elif choice == "2" and self.file_exists:
                self.continue_writing()

            elif choice == "3" and self.file_exists:
                self.clear_and_start_over()

            elif choice == "4":
                print("Saliendo del programa.")
                break

            else:
                print("Opción inválida. Por favor, elige una opción válida.")


def main():
    editor = FileEditor("text.txt")
    editor.run_program()


if __name__ == "__main__":
    main()


