import os

nombre_archivo = "text.txt"

# Función para manejar la opción uno del menú "1 : ¿Quieres Crear o Modificar?"
def opcion_uno():
    try:
        if os.path.isfile(nombre_archivo):
            respuesta = input("+++ El archivo existe, ¿deseas modificarlo? (si/no): ")
            if respuesta.lower() == "si":
                # Leer el contenido actual del archivo
                with open(nombre_archivo, "r") as archivo:
                    contenido_actual = archivo.read()
                print("|--------------------------------|")
                print("| +++ Muestrame el Contenido +++ |")
                print("|--------------------------------|")
                print(contenido_actual)
             
                # Agregar nuevo contenido al archivo
                with open(nombre_archivo, "a") as archivo:
                    print("|-----------------------------------|")
                    print("| +++ Escribe \"exit\" para salir +++ |")
                    print("|-----------------------------------|")
                    while True:
                        contenido = input("Escribe a continuación y presiona Enter para Guardar: ")
                        if contenido == "exit":
                            break
                        archivo.write(f"{contenido}\n")
            else:
                respuesta.lower() == "no"
                print("+++ Hasta luego")
                
        else:
            print(f"El archivo '{nombre_archivo}' no existe. Creando uno nuevo...")
            # Creando nuevo archivo
            with open(nombre_archivo, "x") as archivo:
                print("|-----------------------------------|")
                print("| +++ Escribe \"exit\" para salir +++ |")
                print("|-----------------------------------|")
                while True:
                    contenido = input("Escribe a continuación y presiona Enter para Guardar: ")
                    if contenido == "exit":
                        break
                    archivo.write(f"{contenido}\n")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Función para manejar la opción dos del menú "2 : ¿Quieres Borrar el archivo?"
def opcion_dos():
    try:
        if os.path.exists(nombre_archivo):
            print("El archivo ya existe. Escribe \"delete\" para eliminar: ")
            text = input()
            # Confirma que quieres borrar el archivo
            if text == "delete":
                os.remove(nombre_archivo)
                print("+++ Archivo eliminado con éxito +++")
            else:
                print("+++ No se realizó ninguna acción +++")
        else:
            print("+++ El archivo no existe. +++")
    except Exception as e:
        print(f"Error inesperado: {e}")
    
# Diccionario de opciones para vincular números con funciones
opciones = {
    "1": opcion_uno,
    "2": opcion_dos,
}

# Función para mostrar el menú
def mostrar_menu():
    print("1 : ¿Quieres Crear o Modificar?")
    print("2 : ¿Quieres Borrar el archivo?")
    print("3 : Salir para finalizar.")
    
mostrar_menu()

# Bucle principal que maneja las opciones del menú
while True:
    opcion = input("Escribe una opción: ")
    
    if opcion == "3":
        print("+++ Hasta luego")
        break
    elif opcion in opciones:
        opciones[opcion]()
    else:
        print("+++ Opción no válida, lee la pantalla")

    mostrar_menu()