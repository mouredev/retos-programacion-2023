def main():

    try:
        print("Bienvenido al editor de texto")
        print("Escribe 'exit' para salir")
        print()

        # Abrir el archivo en modo lectura para comprobar si existe
        open('text.txt', 'r')

        print("Quieres seguir escribiendo o sobre escribir el texto?")
        print("1. Seguir escribiendo")
        print("2. Sobre escribir")
        option = input("> ")

        match option:
            case "1":
                file = open('text.txt', 'r')
                actual_text = file.read()
                print("Texto actual:")
                print(actual_text)

                file = open('text.txt', 'a')
                print("Escribe el texto:")
                while True:
                    text = input("> ")
                    if text == "exit":
                        file.close()
                        break
                    file.write(text + "\n")

            case "2":
                file = open('text.txt', 'w')
                print("Escribe el texto:")
                while True:
                    text = input("> ")
                    if text == "exit":
                        file.close()
                        break
                    file.write(text + "\n")
    except:
        open('text.txt', 'x')
        file = open('text.txt', 'w')
        print("Escribe el texto:")
        while True:
            text = input("> ")
            if text == "exit":
                file.close()
                break
            file.write(text + "\n")


if __name__ == '__main__':
    main()
