from random import choice
users = []

while True:
    print("¿Que desea hacer?")
    print("Pulsa A: Añadir nuevo usuario \nPulsa B: para eliminar un participante \nPulsa L: Para listar los participantes \nPulsa S: Para realizar el sorteo \nPulsa E: Para salir del programa" )
    user_choice = input()
    user_choice = user_choice.upper()

    match user_choice:
        case "A":
            name = input("Intorduce el nombre del participante ")
            if users.count(name) > 0:
                print("El usuario ya existe en el sistema ")
            else:
                users.append(name)    
        case "B":
            name = input("Introduzca el usuario a borrar ")
            if users.count(name) > 0:
                users.remove(name)
                print("Usuario "+ name +" eliminado del sistema")
            else:
                print("El usuario no existe en el sistema")    
        case "L":
            for user in users:
                print(user)
        case "S":
            if len(users) > 0:
                user_winner = choice(users)
                print("El ganador del sorteo es: " + user_winner)
                users.remove(user_winner)
            else:
                print("No hay usuarios en el sistema")    
           
        case "E":
            break

