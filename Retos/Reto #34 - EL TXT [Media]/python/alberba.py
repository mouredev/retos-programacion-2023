from pathlib import Path

def input_to_txt():
    if Path.is_file(Path("./text.txt")):
        borrar_fichero = s_n_to_bool(input("El fichero ya existe. ¿Desea borrarlo? (s/n): "))
        if borrar_fichero:
            with open("text.txt", "w") as file:
                text = input()
                # Acaba cuando se introduce una línea vacía
                while text:
                    file.write("\n" + text)
                    text = input()
        else:
            print(file.read())
            with open("text.txt", "a") as file:
                text = input()
                # Acaba cuando se introduce una línea vacía
                while text:
                    file.write("\n" + text)
                    text = input()
    else:
        with open("text.txt", "w") as file:
            text = input()
            # Acaba cuando se introduce una línea vacía
            while text:
                file.write("\n" + text)
                text = input()
    


def s_n_to_bool(respuesta: str)-> bool:

    if respuesta == "s":
        return True
    elif respuesta == "n":
        return False
    else: 
        print("Valor incorrecto. Se asigna el valor por defecto (n)")
        return False
    

input_to_txt()