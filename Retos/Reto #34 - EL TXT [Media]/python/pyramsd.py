def crear_o_abrir_fichero():
    try:
        with open("text.txt", "r") as archivo:
            contenido = archivo.read()
            if contenido:
                print("El archivo ya existe y contiene el siguiente texto:")
                print(contenido)
            else:
                print("El archivo ya existe pero está vacío.")
    except FileNotFoundError:
        with open("text.txt", "w") as archivo:
            print("Se ha creado un nuevo archivo 'text.txt'.")

def escribir_en_fichero():
    accion = input("¿Deseas continuar escribiendo en el archivo o borrar su contenido y empezar de nuevo? (C/B): ").strip().lower()
    if accion == 'c':
        with open("text.txt", "a") as archivo:
            while True:
                texto = input("Introduce el texto que deseas agregar (presiona Enter para finalizar):\n")
                if not texto:
                    break
                archivo.write(texto + "\n")
            print("Texto agregado correctamente.")
    elif accion == 'b':
        with open("text.txt", "w") as archivo:
            print("Contenido anterior del archivo ha sido eliminado. Puedes empezar a escribir desde cero.")
    else:
        print("Opción no válida. Por favor, ingresa 'C' para continuar escribiendo o 'B' para borrar el contenido.")

if __name__ == "__main__":
    crear_o_abrir_fichero()
    escribir_en_fichero()
