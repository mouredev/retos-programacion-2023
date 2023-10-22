import random
import os

# Se carga la informacion inicial para la cuadricula
screen = [["🚪", "⬜️", "⬜️", "⬜️"],
          ["⬜️", "⬜️", "⬜️", "⬜️"],
          ["⬜️", "⬜️", "⬜️", "⬜️"],
          ["⬜️", "⬜️", "⬜️", "⬜️"]]

# Se cargan las tuplas de preguntas y respuestas
preg_rta = [["Como se llama la hija de los locos Adams? ","merlina"],
            ["Que verdura se usa para decorar en Halloween? ","calabaza"],
            ["En que animal se convierte el Conde Dracula? ","murcielago"],
            ["Que mostruo fue armado con partes de distintos humanos? ","frankestein"],
            ["Como se los llama comunmente a los muertos vivos? ","zombies"],
            ["Como se llama el hijo de los locos Adams? ", "pericles"],
            ["Donde vive el Conde Dracula? ", "transilvania"]]

fantasma1 = 0
fantasma2 = 0
salida = 0
# Limpia la pantalla
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Dibuja la mansion       
def dibuja_pantalla(screen):
    clear()
    for row in screen:
        print("".join(map(str, row)))

# Estipula la posicion de los fantasmas y salida aleatoriamente
def aleatorio(fantasma1, fantasma2, salida):
    salida = random.randint(1, 15)
    while True:
        fantasma1 = random.randint(1,15)
        if fantasma1 != salida:
            break
    while True:
        fantasma2 = random.randint(1,15)
        if fantasma2 != salida and fantasma2 != fantasma1:
            break
    
    return (fantasma1, fantasma2, salida)

# Estipula las preguntas aleatoriamente
def pregunta():
    while True:
        sortea_pregunta = random.randint(0,6)
        print(preg_rta[sortea_pregunta][0])
        repuesta = input()
        if preg_rta[sortea_pregunta][1] == repuesta.lower():
            print("Has contestado correctamente")
            break  
        print("Has contestado mal, vuelve a intentarlo") 
    return 

# Hace el movimiento por la mansion
def movimiento(pos):
    while True:
        oeste = "oeste"
        este = "este"
        norte = "norte"
        sur = "sur"
        if pos == 0 or pos == 4 or pos == 8 or pos == 12:
            oeste = "--"
        if pos == 0 or pos == 1 or pos == 2 or pos == 3:
            norte = "--"
        if pos == 12 or pos == 13 or pos == 14 or pos == 15:
            sur = "--" 
        if pos == 3 or pos == 7 or pos == 11 or pos == 15:
            este = "--"

        print(f"Hacia donde te quieres mover? ({norte}, {este}, {oeste}, {sur} o salida)")
        preg_movimiento = input()
        if preg_movimiento.lower() == norte or preg_movimiento.lower() == sur or preg_movimiento.lower() == este or preg_movimiento.lower() == oeste or preg_movimiento.lower() == "salida":
    
            if preg_movimiento.lower() == "norte":
                posicion = pos - 4
                return posicion
            
            elif preg_movimiento.lower() == "sur":
                posicion = pos + 4
                return posicion
            
            elif preg_movimiento.lower() == "oeste":
                posicion = pos - 1
                return posicion
            
            elif preg_movimiento.lower() == "este":
                posicion = pos + 1
                return posicion
            elif preg_movimiento.lower() == "salida":
                exit()
        else:
            posicion = pos
            print("Se ha ingresado un dato erroneo")

# Se inicializa el juego vacio        
dibuja_pantalla(screen)
fantasma1, fantasma2, salida = aleatorio(fantasma1, fantasma2, salida)
posicion = 0
pos_nueva = 0
pos_nueva = movimiento(posicion)

while pos_nueva != salida:
    # Calcula las coordenadas de la posicion
    x = pos_nueva // 4
    y = pos_nueva % 4
    if pos_nueva == fantasma1 or pos_nueva == fantasma2:
        screen[x][y] = "👻"
        dibuja_pantalla(screen)
        print("Te has encontrado un fantasma, desbes responder dos preguntas")
        pregunta()
        pregunta()
    else:
        screen[x][y] = "❓"
        dibuja_pantalla(screen)
        pregunta()
    
    posicion = pos_nueva
    pos_nueva = movimiento(posicion)

screen[salida // 4][salida % 4] = "🍭"
dibuja_pantalla(screen)
print("Ha encontrado el dulce!!!")