def main():
    archivo = "text.txt"
    
    # Verificar si el archivo existe
    archivo_existe = False
    try:
        with open(archivo, 'r'):
            archivo_existe = True
    except FileNotFoundError:
        archivo_existe = False
    
    # Si el archivo no existe, crearlo
    if not archivo_existe:
        with open(archivo, 'w'):
            pass
    
    # Dar opciones al usuario
    while True:
        print("Opciones:")
        print("1. Escribir nuevo texto")
        print("2. Continuar escribiendo desde el final")
        print("3. Borrar contenido y comenzar desde el principio")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            texto = input("Introduzca el texto a guardar: ")
            with open(archivo, 'a') as f:
                f.write(texto + '\n')
            print("Texto guardado.")
        elif opcion == '2':
            with open(archivo, 'a') as f:
                texto = input("Continúe escribiendo desde el final: ")
                f.write(texto + '\n')
                print("Texto guardado.")
        elif opcion == '3':
            with open(archivo, 'w'):
                pass
            print("Contenido borrado. Puede comenzar a escribir desde el principio.")
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
