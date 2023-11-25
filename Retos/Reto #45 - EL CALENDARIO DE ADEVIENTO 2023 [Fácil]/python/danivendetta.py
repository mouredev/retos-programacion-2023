from random import randint
from pprint import pprint

participantes = []
def menu():
    print("Opciones:")
    print("1: Añadir participante")
    print("2: Eliminar participante")
    print("3: Listar participantes")
    print("4: Realizar sorteo")
    print("5: Salir")

    op = input("Selecciona una opción: ")
    while op not in ["1", "2", "3", "4", "5"]:
        print(f'{op} no es una opción válida, vuelve a intentarlo!')
        op = input("Selecciona una opción: ")

    return op

def add_participante(participante: str):
    if participante in participantes:
        print(f'{participante} ya está en la lista de participantes')
    else:
        participantes.append(participante)
        print(f'{participante} añadido a la lista de participantes')

def del_participante(participante: str):
    if participante not in participantes:
        print(f'{participante} no está en la lista de participantes')
    else:
        participantes.remove(participante)
        print(f'{participante} eliminado de la lista de participantes')

def list_participantes():
    pprint(participantes)

def realizar_sorteo():
    if len(participantes) == 0:
        print("Primero debes añadir usuarios a la lista de participantes")
    else:
        ganador = participantes[randint(0, len(participantes)-1)]
        print(f'El participante ganador ha sido: {ganador}')
        del_participante(ganador)

if __name__ == "__main__":
    op = menu()
    while op != "5":
        if op == "1":
            print("1: Añadir participante")
            participante = input("Participante: ")
            add_participante(participante)
            op = menu()
        elif op == "2":
            print("2: Eliminar participante")
            participante = input("Participante: ")
            del_participante(participante)
            op = menu()
        elif op == "3":
            print("3: Listar participantes")
            list_participantes()
            op = menu()
        elif op == "4":
            print("4: Realizar sorteo")
            realizar_sorteo()
            op = menu()
        else:
            print("5: Salir")

    print("Exit!!")





