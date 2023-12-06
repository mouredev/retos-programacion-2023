def main():
    file_name = "text.txt"
    while True:
        option = input(
            "\nSeleccione una opcion:\n"
            "\n1. Continuar escribiendo\n"
            "\n2. Borrar el contenido y escribir\n"
            "\n3. Salir\n"
        )

        if option == "1":
            with open(file_name, "a+") as file:
                file.seek(0)
                print(file.read())
                text = input("Ingrese el texto: ")
                file.write(text + "\n")

        elif option == "2":
            with open(file_name, "w") as file:
                text = input("Ingrese el texto: ")
                file.write(text + "\n")
        elif option == "3":
            break
        else:
            print("Opcion no valida, ingrese una nueva opcion")


if __name__ == "__main__":
    main()
