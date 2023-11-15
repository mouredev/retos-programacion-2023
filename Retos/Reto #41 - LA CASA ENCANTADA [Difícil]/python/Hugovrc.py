import random

def casa_encantada():
    preguntas = (("cuando se celebra el halloween?", "31 de octubre"),
                ("Qué bebida es popular en las fiestas de Halloween?","sangre de vampiro"),
                ("Qué película de terror es un clásico para ver en Halloween?","el resplandor"),
                ("Que actividad hacen los niños el dia de Halloween?","pedir dulces"),
                ("Por que se tallan calabazas en forma de caras espeluznantes?","para alejar a los espiritus malignos"),
                ("De dónde proviene la celebración de Halloween?", "de una festividad celta llamada Samhain"))
    
    habitaciones = [["🚪","⬜","⬜","⬜"],
                    ["⬜","👻","⬜","⬜"],
                    ["⬜","⬜","⬜","👻"],
                    ["⬜","⬜","⬜","🍭"]]
    
    #for row in habitaciones:
    #    print("".join(map(str,row)))

    posicion = encontrar_elemento(habitaciones, "🚪")
    posicion_fila = posicion[0]
    posicion_columna = posicion[1]
    pos = []

    while True:
        num = len(preguntas)
        num_preg = random.randint(0,num-1)
        num_preg2 = random.randint(0, num-1)

        primera_pregunta, primera_resp = preguntas[num_preg]
        if num_preg2 != num_preg:
            segunda_pregunta, segunda_resp = preguntas[num_preg2]

        pos = habitaciones[posicion_fila][posicion_columna] 
        if pos == "⬜":
            print("---Deberas responder esta pregunta para poder avanzar---")
            respuesta = input(f"{primera_pregunta}: ")
            while respuesta != primera_resp:
                print("respuesta incorrecta!!")
                respuesta = input(f"{primera_pregunta}: ")
                
        elif pos == "👻":
            print("---Deberas responder dos preguntas para poder avanzar---")
            respuesta1 = input(f"{primera_pregunta}: ")
            respuesta2 = input(f"{segunda_pregunta}: ")
            while respuesta1 != primera_resp or respuesta2 != segunda_resp:
                print("--- respuesta incorrecta!!")
                respuesta1 = input(f"{primera_pregunta}: ")
                respuesta2 = input(f"{segunda_pregunta}: ")
        elif pos == "🍭":
            print("--- Felicidades haz encontrado la salida ---")
            break
        
        movimiento = input("-- Hacia donde deseas desplazarte(norte/sur/este/oeste): ")

        if movimiento == "norte" and posicion_fila > 0:
            posicion_fila -= 1
        elif movimiento == "sur" and posicion_fila < 3:
            posicion_fila += 1
        elif movimiento == "oeste" and posicion_columna > 0:
            posicion_columna -= 1
        elif movimiento == "este" and posicion_columna < 3:
            posicion_columna += 1
        else:
            print(f"no se puede desplazar hacia el {movimiento}")

def encontrar_elemento(habitaciones, elemento):
    posicion = []

    for fila in range(4):
        for columna in range(4):
            if habitaciones[fila][columna] == elemento:
                posicion = [fila, columna]
                break
    return posicion
    
    

    
casa_encantada()
