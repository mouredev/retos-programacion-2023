import random

lista_participantes =[]
cont = True
print("-"*21)
print("Bienvenido a ADVIENTO")
while cont: 
    print("-"*21)
    print("1. Añadir participante")
    print("2. Remover participante")
    print("3. Mostrar participantes")
    print("4. Lanzar Sorteo")
    print("0. Salir")
    print("-"*21)
    opcion = input("Seleccione una opcion: ")
    if opcion == "0":
        cont = False
        break
    if opcion == "1":
        nombre = input("Ingrese nombre: ")
        if nombre in lista_participantes:
            print("Nombre ya esta registrado")
        else:
            lista_participantes.append(nombre)
            print(f'{nombre} agregado correctamente')
    if opcion == "2":
        if len(lista_participantes) != 0:
            nombre = input("Ingrese nombre: ")
            if not nombre in lista_participantes:
                print("Nombre no esta registrado")
            else:
                lista_participantes.remove(nombre)
                print(f'{nombre} removido correctamente')
        else:
            print("No hay participantes cargados")
    if opcion == "3":
        if len(lista_participantes) != 0:
            for participante in lista_participantes:
                print(participante)    
        else:
            print("Lista de participantes vacia")
    if opcion == "4":
        if len(lista_participantes) != 0:
            ganador = lista_participantes[random.randint(0, len(lista_participantes)-1)]
            print(f"¡¡El ganador es {ganador}!!\n¡¡Felicitaciones!!")
            lista_participantes.remove(ganador)
        else:
            print("No hay participantes")
