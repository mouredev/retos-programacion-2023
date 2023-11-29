# /*
# * ¿Conoces el calendario de aDEViento de la comunidad (https://adviento.dev)?
# * 24 días, 24 regalos sorpresa relacionados con desarrollo de software.
# * Desde el 1 al 24 de diciembre.
# *
# * Crea un programa que simule el mecanismo de participación:
# * - Mediante la terminal, el programa te preguntará si quieres añadir y borrar
# *   participantes, mostrarlos, lanzar el sorteo o salir.
# * - Si seleccionas añadir un participante, podrás escribir su nombre y pulsar enter.
# * - Si seleccionas añadir un participante, y este ya existe, avisarás de ello.
# *   (Y no lo duplicarás)
# * - Si seleccionas mostrar los participantes, se listarán todos.
# * - Si seleccionas eliminar un participante, podrás escribir su nombre y pulsar enter.
# *   (Avisando de si lo has eliminado o el nombre no existe)
# * - Si seleccionas realizar el sorteo, elegirás una persona al azar 
# *   y se eliminará del listado.
# * - Si seleccionas salir, el programa finalizará.
# */
import random
option=0
participantes=[]
while option!="5": 
    option=input("""
                1. Añadir
                2. Mostrar
                3. Borrar
                4. Lanzar sorteo
                5. Salir
                
    """)
    
   
    if option == "1":
        newparticipant=input("Escribe el nombre del participante")
        if newparticipant in participantes:
            print("El participante ya esta registrado")
        else:
            participantes.append(newparticipant)
    
            
    elif option == "2":
        print("Estos son los participantes: ")
        for each in participantes:
            print(each)
    elif option == "3":
        participant=input("Escribe el nombre del participante a eliminar")
        if participant in participantes:
            participantes.remove(participant)
            print("Participante eliminado")
        else: 
            print("El participante no esta registrado")
    elif option=="4":
        winer= random.choice(participantes)
        print(f"El ganador es: {winer}")
        participantes.remove(winer)
    
