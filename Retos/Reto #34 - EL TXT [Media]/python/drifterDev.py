import os


def existe_archivo(ruta: str):
    if not os.path.exists(ruta):
        with open(ruta, "w") as archivo:
            archivo.write("")


def leer_contenido(ruta: str) -> str:
    with open(ruta, "r") as archivo:
        return archivo.read()


def escribir_contenido(ruta: str, contenido: str):
    with open(ruta, "w") as archivo:
        archivo.write(contenido)


def main():
    archivo_ruta = "text.txt"
    existe_archivo(archivo_ruta)
    while True:
        opc = input(
            "Opciones del menu: \n1- Escribir nueva linea \n2- Borrar todo el contenido del fichero\n3- Salir\n"
        )
        if opc == "1":
            nuevo_contenido = leer_contenido(archivo_ruta)
            nuevo_contenido += input()
            nuevo_contenido += "\n"
        elif opc == "2":
            nuevo_contenido = ""
        else:
            break
        escribir_contenido(archivo_ruta, nuevo_contenido)


if __name__ == "__main__":
    main()
