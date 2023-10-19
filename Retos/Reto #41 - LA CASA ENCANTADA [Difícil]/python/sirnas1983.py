import random
import time

preguntas = {1 :  ("¿Qué serie de ciencia ficción de Netflix está ambientada en la ciudad ficticia de Hawkins?", "Stranger Things"),
             2 :  ("Mädchen Amick interpreta a Shelly Briggs en el clásico de culto de David Lynch Twin Peaks, pero ¿qué espeluznante drama de Netflix protagoniza actualmente?","Riverdale"),
             3 :  ("En el episodio de Friends 'El de la fiesta de Halloween', ¿qué disfraces memorables, aunque no especialmente espeluznantes, llevaban Ross y Chandler?","Ross era un Spud-nik y Chandler era un conejo de felpa rosa"),
             4 :  ("El 31 de octubre de 1992, la BBC petrificó al Reino Unido con Ghostwatch, un drama guionizado que engañaba a los espectadores haciéndoles creer que era una transmisión en directo desde una casa encantada. ¿Qué veterano locutor, periodista y autor inglés, así como personalidad de la television lo presentó","Michael Parkinson"),
             5 :  ("Ratched, la inquietante serie de Ryan Murphy en Netflix, protagonizada por Sarah Paulson, ¿en qué novela clásica de 1962 está inspirada?","Alguien volo sobre el nido del cuco"),
             6 :  ("¿En qué serie de novelas está basada la serie de terror de Netflix La calle del terror?","RL Stine"),
             7 :  ("¿Cómo se llama la actriz que interpretará a Morticia Addams en la versión de La familia Addams de Tim Burton para Netflix?","Catherine Zeta-Jones"),
             8 :  ("¿Qué película de terror clásica es la precuela de Motel Bates, protagonizada por Freddie Highmore?","Psicosis"),
             9 :  ("¿Cómo se llama la joven que desaparece en Twin Peaks?","Laura Palmer"),
             10 : ("¿Cuál es el apellido de Sabrina, la bruja adolescente?","Spellman"),
             11 :  ("En El retorno de las brujas, ¿cómo se llaman las tres hermanas Sanderson y las actrices que las interpretan?", "Bette Midler como Winifred, Sarah Jessica Parker como Sarah y Kathy Najimy como Mary"),
             12 :  ("¿Qué otra película de terror de los 90 protagonizaron Neve Campbell y Skeet Ulrich, a las que vimos en Scream?","Jovenes y brujas"),
             13 :  ("¿En qué película de terror de 1982 Carol Anne empezó a hablar con el televisor?","Poltergeist"),
             14 :  ("En la adaptación cinematográfica de La maldición de las brujas de Roald Dahl, ¿en qué quiere convertir a los niños la Gran Bruja Mayor interpretada por Anjelica Huston?","Ratones"),
             15 :  ("¿Qué actor interpretó el papel de Hannibal Lecter en la pantalla antes de que Anthony Hopkins lo hiciera suyo?","Brian Cox"),
             16 :  ("¿Qué actriz retoma su icónico papel -que se hizo famoso hace más de dos décadas- en Halloween Kills?","Jamie Lee Curtis"),
             17 :  ("¿Cómo se llama el espeluznante hotel de El resplandor de Stanley Kubrick?","Hotel Overlook"),
             18 :  ("Lo que hacemos en las sombras se basa en las vidas ordinarias y, a veces, banales de...","Los vampiros"),
             19 :  ("¿Cómo se llama el terrorífico payaso que aparece en It, de Stephen King, papel que recientemente ha hecho Bill Skarsgard en la nueva película de 2017?","Pennywise"),
             20 :  ("En Harry Potter y la piedra filosofal, ¿puedes nombrar a la criatura que irrumpe en Hogwarts la noche de Halloween?","Trol de montaña")
             }

def generar_tablero():
    tablero = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]

    pos1 = random.randrange(0,3)
    time.sleep(0.005)
    pos2 = random.randrange(0,3)
    time.sleep(0.005)
    pos3 = random.randrange(0,3)
    time.sleep(0.005)
    pos4 = random.randrange(0,3)
    time.sleep(0.005)
    pos5 = random.randrange(0,3)
    time.sleep(0.005)
    pos6 = random.randrange(0,3)

    tablero[pos1][pos4] = 1
    tablero[pos2][pos5] = 1
    tablero[pos3][pos6] = 2

    return tablero

def preguntar():
    pregunta = random.randrange(1,20)
    print(preguntas[pregunta][0])
    respuesta = input("Ingrese su respuesta: ")
    if respuesta.lower() == preguntas[pregunta][1].lower():
        print("¡¡Correcto!!")
        return True
    else:
        print("¡¡...Incorrecto...!!")
        return False
    
def mover(posicion):
    movimientos_permitidos = []
    if posicion[0] < 3:
        movimientos_permitidos.append(8)
    if posicion[0] > 0:
        movimientos_permitidos.append(2)
    if posicion[1] < 3:
        movimientos_permitidos.append(6)
    if posicion[1] > 0:
        movimientos_permitidos.append(4)
        
    movimientos_permitidos.sort()
    print("REFERENCIA -- 2: abajo, 4: izquierda, 8: arriba, 6: derecha")
    mov = 0
    while mov not in movimientos_permitidos:
        mov = int(input("Seleccione un movimiento.\nLos movimientos permitidos son " + movimientos_permitidos.__str__() + ": "))

    if mov == 2:
        posicion[0] -= 1
    elif mov == 8:   
        posicion[0] += 1
    elif mov == 4:
        posicion[1] -= 1
    elif mov == 6:
        posicion[1] += 1
    return posicion

def posicion_inicial(casillero):
    return [casillero//4, casillero - casillero//4 * 4]

def marcar_posicion(tablero, pos):
    tablero[pos[0]][pos[1]] = "X"
    for row in reversed(tablero):
        print(row)
    return tablero   

def juego():
    titulo = "Bienvenido al juego de la casa embrujada"
    jugando = True

    print("-"*len(titulo))
    print(titulo)
    print("-"*len(titulo))
    print("Reglas: Debes avanzar hasta encontrar la casa de los dulces. Para poder avanzar debes\ncontestar la pregunta correctamente.")
    print("-"*len(titulo))  
    
    casillero_entrada = -1

    while casillero_entrada not in range(0,16):
        casillero_entrada = int(input("Ingrese un numero del 1 al 16.\nEste va a ser tu punto de partida, cuidado con los fantasmas: ")) - 1

    pos = posicion_inicial(casillero_entrada)

    tablero = generar_tablero()
    tablero_visible = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    tablero_visible = marcar_posicion(tablero_visible, pos) 
    
    while jugando:
        if tablero[pos[0]][pos[1]] == 1:
            print("¡Has caido en una celda fantsma! ¡Debes responder correctamente 2 veces para avanzar!")
            if preguntar() and preguntar():
                pos = mover(pos)
        elif tablero[pos[0]][pos[1]] == 2:
            print("¡Has caido en la casa de los dulces! Contesta bien para ganar el juego.... ")
            if preguntar():
                jugando = False
                print("¡¡Felicidades, has ganado!!")
                break
        else:
            print("Responde correctamente para avanzar...")
            if preguntar():
                pos = mover(pos)
        tablero_visible = marcar_posicion(tablero_visible, pos) 

if __name__ == "__main__":    
    juego()    
