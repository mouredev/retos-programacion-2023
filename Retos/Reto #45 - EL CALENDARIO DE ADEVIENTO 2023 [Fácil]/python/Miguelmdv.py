
#  * ¿Conoces el calendario de aDEViento de la comunidad (https://adviento.dev)? 24 días, 24 regalos sorpresa relacionados con desarrollo de software. Desde el 1 al 24 de diciembre.

#  * Crea un programa que simule el mecanismo de participación:
#  * - Mediante la terminal, el programa te preguntará si quieres añadir y borrar participantes, mostrarlos, lanzar el sorteo o salir.
#  * - Si seleccionas añadir un participante, podrás escribir su nombre y pulsar enter.
#  * - Si seleccionas añadir un participante, y este ya existe, avisarás de ello. (Y no lo duplicarás)
#  * - Si seleccionas mostrar los participantes, se listarán todos.
#  * - Si seleccionas eliminar un participante, podrás escribir su nombre y pulsar enter. (Avisando de si lo has eliminado o el nombre no existe)
#  * - Si seleccionas realizar el sorteo, elegirás una persona al azar y se eliminará del listado.
#  * - Si seleccionas salir, el programa finalizará.

import random as rd


def calendario(df: set, eliminados: set):
    salir = True
    while salir:
        respuesta = input(
            "1 -> Añadir participante, 2 -> mostrar participantes, 3 -> Eliminar participante, 4 -> Realizar sorteo, 5 -> Salir\
            \n> "
        )

        match respuesta:
            case "1":
                dato = input("Nombre participante: ")
                if dato not in df:
                    df.add(dato)
                else:
                    print("Este participante ya existe")

            case "2":
                if len(df):
                    for i, name in enumerate(df):
                        print(f"{i+1}.{name}")
                else:
                    print("No hay participantes")

            case "3":
                dato = input("Nombre participante: ")
                if dato in df:
                    df.remove(dato)
                    eliminados.add(dato)
                    print(dato, "se ha eliminado correctamente")
                elif dato in eliminados:
                    print("Este participante ya ha sido eliminado")
                else:
                    print("Este participante no existe")

            case "4":
                eliminado = rd.choice(list(df))
                eliminados.add(eliminado)
                df.remove(eliminado)
                print(eliminado, "ha ganado! Y por lo tanto ha sido eliminado")

            case "5":
                salir = False
                print("Adios")

            case _:
                print("Dato no valido")


df = set()
eliminados = set()

calendario(df, eliminados)
