def main():
    file_name = "text.txt"
    
    try:
        file_exists = True
        try:
            with open(file_name, 'r'):
                pass
        except FileNotFoundError:
            file_exists = False
        
        with open(file_name, 'a' if file_exists else 'w') as file:
            if file_exists:
                print("El archivo ya existe. ¿Deseas borrar su contenido? (Sí: 1, No: 0)")
                choice = int(input())
                if choice == 1:
                    file.close()
                    file = open(file_name, 'w')
                else:
                    print("Contenido actual del archivo:")
                    with open(file_name, 'r') as existing_file:
                        print(existing_file.read())
            
            print("Introduce texto (Presiona Enter para guardar, o escribir 'exit' para salir):")
            while True:
                input_text = input()
                if input_text.lower() == 'exit':
                    break
                file.write(input_text + '\n')
            
            print("Texto guardado en el archivo.")
            
    except Exception as e:
        print("Ocurrió un error:", e)

if __name__ == "__main__":
    main()
