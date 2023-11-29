"""
¿Conoces el calendario de aDEViento de la comunidad (https://adviento.dev)?
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
 */
"""







import random
listaparticipantes = list()

def adeviento():
    
    what_you_wanna_do = input("que quieres hacer ")

    if what_you_wanna_do == "add":
        Añadido = input("nombre del añadido: ")
        if len(listaparticipantes) == 0:
            listaparticipantes.append(Añadido)
            print(listaparticipantes)
        else:
            for i in range(0, len(listaparticipantes)):
                print(i)
                print(len(listaparticipantes))
                name = listaparticipantes[i]
                if Añadido == name:
                    print("ese nombre ya esta añadido")
                    adeviento()
                    
            
            listaparticipantes.append(Añadido)
            print(listaparticipantes)

        adeviento()

    elif what_you_wanna_do == "eliminate":
        elim = input("nombre del eliminado: ")
        if len(listaparticipantes) == 0:
            print("no hay nadie participando")
        else:
          for i in range(0, len(listaparticipantes)):
             print(i)
             name = listaparticipantes[i]
             print(name)
             if elim == name:
                 listaparticipantes.remove(listaparticipantes[i])
                 adeviento()
            
          print("ese nombre no existe")
        
        adeviento()

    elif what_you_wanna_do == "sort":
        if len(listaparticipantes) == 1:
            print("no hay suficientes participantes, añadelos")
        else:
           sorteo = random.randint(0,len(listaparticipantes) - 1)
           print(sorteo)
           ganador = listaparticipantes[sorteo]
           print(f"EL GANADOR DEL SORTEO {ganador}")
           listaparticipantes.remove(listaparticipantes[sorteo])

        adeviento()
    elif what_you_wanna_do == "close":
        print("OK closing up")
        iniciador()
    else:
        print("ese no es un comando")
        adeviento()
        
def iniciador():
    Abrir = input("quieres abrir el programa' Y/N ")
    if Abrir == "Y":
        adeviento()
    elif Abrir == "N":
        print( ":(")

                

iniciador()