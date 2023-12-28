import random
participante:list = []

nombre:str
apellido:str

while True:
    print("Presione las siguientes teclas según corresponda: ")
    print("A - para agregar participante")
    print("E - para eliminar participante")
    print("L - para listar todos los participantes")
    print("C - comenzar sorteo")
    print("S - para salir")
    print()
    opcion = input("A - E - L - C - S").upper()
    if opcion == "S":
        break
    if opcion == "A":
        nombre = input("Cual es tu nombre? ").upper()
        apellido = input("Cual es tu apellido? ").upper()
        if [nombre,apellido] in participante:
            print()
            print("Ya estas participando!!!")
            print()
        else:
            participante.append([nombre,apellido])
            print()
            print(nombre,apellido,"has sido incorporado satisfactoriamente, Muchas suerte!!!")
            print()
    if opcion == "E":
        nombre = input("Cual es tu nombre? ").upper()
        apellido = input("Cual es tu apellido? ").upper()
        if [nombre,apellido] in participante:
            participante.remove([nombre,apellido])
            print()
            print(nombre,apellido," ha sido eliminado de la lista")
            print()
        
        else:
            print()
            print(nombre,apellido," no esta en la lista")
            print()

    if opcion == "C":
        ganador =random.choice(participante)
        participante.remove([ganador[0], ganador[1]])
        print("El ganador es ",ganador[0], ganador[1])
    if opcion == "L":
        print()
        print(participante)
        print()
