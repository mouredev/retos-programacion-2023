"""
 * ¿Conoces el calendario de aDEViento de la comunidad (https://adviento.dev)?
 * 24 días, 24 regalos sorpresa relacionados con desarrollo de software.
 * Desde el 1 al 24 de diciembre.
 *
 * Crea un programa que simule el mecanismo de participación:
 * - Mediante la terminal, el programa te preguntará si quieres añadir y borrar
 *   participantes, mostrarlos, lanzar el sorteo o salir.
 * - Si seleccionas añadir un participante, podrás escribir su nombre y pulsar enter.
 * - Si seleccionas añadir un participante, y este ya existe, avisarás de ello.
 *   (Y no lo duplicarás)
 * - Si seleccionas mostrar los participantes, se listarán todos.
 * - Si seleccionas eliminar un participante, podrás escribir su nombre y pulsar enter.
 *   (Avisando de si lo has eliminado o el nombre no existe)
 * - Si seleccionas realizar el sorteo, elegirás una persona al azar 
 *   y se eliminará del listado.
 * - Si seleccionas salir, el programa finalizará.
"""
import random
def aDEVinteo():
    name_list = []
    name = ""
    print("Bienvenidos a sistema de participacion aDEViemto\naqui tenemos las opciones de ingresar [y/o] eliminar participantes-[1], ver la lista de los mismos-[2] o lazar el sorteo-[3]\ncualquier otra opcion cerrara el programa.")
    orden = (input("ingrese su opcion basado en los numero: "))
    
    if orden == "1":
        participants_text =  open("participants.text", "r+")
        work_line = participants_text.readlines()
        print(f"estos son los participantes actuales: {work_line}")

        print("vas a ingresar un nuevo participante[I] o vas a eliminar[D] un participante.")
        respont = input(":")

        if respont == "i":
            print("ingrese los nombre a ingresar en la lista separados una coma [,]: ")
            insertion = input(":")
            for index in insertion:
                if index != ",":
                    name += index
                else:
                    name_list.append(name)
                    name = ""
            name_list.append(name)
            name = ""

        elif respont == "d":
            name_list = work_line
            print("escriba el nombres a retirar separados por un espacio: ")
            insertion = input()
            for index in insertion:
                if index != " ":
                    name += index
                else:
                    name_list.remove(name+"\n")
                    name = ""
            name_list.remove(name+"\n")
            name = ""
        else:
            print("Obcion no valida, el programa se reiniciara para eviar errores")
            aDEVinteo()
        complete_list = work_line.extend(index for index in name_list if index not in work_line) 
        print(f"la lista de participante actual es: {complete_list}")

        participants_text =  open("participants.text", "w")
        for name in complete_list:
            participants_text.write(name + "\n")
        participants_text.close()

    elif orden == "2":
        participants_text = open("participants.text")
        name_list = participants_text.readlines()
        name_list_temp=[]
        for index in name_list:
            name_list_temp.append(index.replace("\n", ""))
        print(f"la lista de participante es: {name_list_temp}")
        participants_text.close()

    elif orden == "3":
        participants_text =  open("participants.text", "r+")
        work_line = participants_text.readlines()
        result = random.choice(work_line) 
        print(f"EL GANADOR EN EL SORTEO aDEViento es: {result}\nEste se eliminara del listado para las siguientes rifas")
        work_line.remove(result)
        participants_text =  open("participants.text", "w")

        for index in work_line:
            participants_text.write(index)
        participants_text.close()
    else:
        exit()
aDEVinteo()
