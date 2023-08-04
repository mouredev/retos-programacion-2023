# Reto #2: EL PARTIDO DE TENIS
#### Dificultad: Media | Publicación: 09/01/23 | Corrección: 16/01/23
## Enunciado
# * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
# * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
# * gane cada punto del juego.
# *
# * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
# * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
# *   15 - Love
# *   30 - Love
# *   30 - 15
# *   30 - 30
# *   40 - 30
# *   Deuce
# *   Ventaja P1
# *   Ha ganado el P1
# * - Si quieres, puedes controlar errores en la entrada de datos.
# * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.

PLAY1=''
PLAY2=''
N=1
PUNTAJE1=''
PUNTAJE2=''
PUNTAJE_TOTAL=[]
REPETIR='yes'

def empate(PLAY1,PLAY2,PUNTAJE_TOTAL):
    repetir1='yes'
    repetir2='yes'
    while repetir1=='yes':
        puntaje1='LOVE'
        puntaje2='LOVE'
        while repetir2=='yes':
            win=winner(PLAY1,PLAY2,N)
            if win==PLAY1:
                if puntaje1=='1':
                    PUNTAJE_TOTAL.append("Ganador del juego es "+PLAY1)
                    repetir2='no'
                    repetir1='no'
                else:
                    puntaje1='1'
                    if puntaje1==puntaje2:
                        PUNTAJE_TOTAL.append("Deuce (empate)")
                        repetir2='no'
                        repetir1='yes'
                    else:
                        PUNTAJE_TOTAL.append("Ventaja jugador "+PLAY1)
                        repetir2='yes'
            else:
                if puntaje2=='1':
                    PUNTAJE_TOTAL.append("Ganador del juego es "+PLAY2)
                    repetir2='no'
                    repetir1='no'
                else:
                    puntaje2='1'
                    if puntaje1==puntaje2:
                        PUNTAJE_TOTAL.append("Deuce (empate)")
                        repetir2='no'
                        repetir1='yes'
                    else:
                        PUNTAJE_TOTAL.append("Ventaja jugador "+PLAY2)
                        repetir2='yes'
    return


def winner(play1, play2, n):
    print("Inicia "+str(n)+ " juego...¿quien lo gano?.. "+ PLAY1 +' o '+ PLAY2)
    print("Ingrese el nombre del jugador ganador.. "+ PLAY1 +' o '+ PLAY2)
    ganador=input()
    ganador=ganador.upper()
    while ganador != play1 and ganador !=play2:
        print("Nombre"+ganador+" es incorrecto...")
        print("Ingresar el nombre correcto del ganador: "+play1 +' o '+play2)
        ganador=input()
        ganador=ganador.upper()
    return ganador

def names():
    print("Ingresa el nombre del jugador:")
    play=input()
    play=play.upper()
    return play

#*************INICIO DEL JUEGO******************
print("**BIENVENIDO AL JUEGO DE TENIS**")
#Registar nombres de los jugadores:
while PLAY1==PLAY2:
    PLAY1=names()
    PLAY2=names()
    if PLAY1==PLAY2:
        print("**Los nombres no deben ser iguales, ingrese de nuevo los nombres**")

win=winner(PLAY1,PLAY2,N) # se guarda el nombre del ganador en la variable win

if PLAY1==win:
    PUNTAJE1='15'
    PUNTAJE2='LOVE'
    N=N+1
else:
    PUNTAJE1='LOVE'
    PUNTAJE2='15'
    N=N+1

PUNTAJE_TOTAL.append(PUNTAJE1 +' - '+ PUNTAJE2)

win=winner(PLAY1,PLAY2,N) # se guarda el nombre del ganador en la variable win

if PLAY1==win:
    if PUNTAJE1=='LOVE':
        PUNTAJE1='15'
    else:
        PUNTAJE1='30'
    N=N+1
else:
    if PUNTAJE2=='LOVE':
        PUNTAJE2='15'
    else:
        PUNTAJE2='30'
    N=N+1

PUNTAJE_TOTAL.append(PUNTAJE1 +' - '+ PUNTAJE2)

win=winner(PLAY1,PLAY2,N) # se guarda el nombre del ganador en la variable win

if PLAY1==win:
    if PUNTAJE1=='LOVE':
        PUNTAJE1='15'
    else:
        if PUNTAJE1=='15':
            PUNTAJE1='30'
        else:
            PUNTAJE1='40'
    N=N+1
else:
    if PUNTAJE2=='LOVE':
        PUNTAJE2='15'
    else:
        if PUNTAJE2=='15':
            PUNTAJE2='30'
        else:
            PUNTAJE2='40'
    N=N+1

PUNTAJE_TOTAL.append(str(PUNTAJE1) +' - '+ str(PUNTAJE2))


while REPETIR=='yes':
    win=winner(PLAY1,PLAY2,N) # se guarda el nombre del ganador en la variable win
    if PLAY1==win:
        if PUNTAJE1=='40':
            if PUNTAJE2=='40':
                PUNTAJE_TOTAL.append("Deuce (empate)")
                empate(PLAY1,PLAY2,PUNTAJE_TOTAL)
                REPETIR='no'
            else:
                PUNTAJE_TOTAL.append("Ganador del juego es "+PLAY1)
                REPETIR='no'
        else:
            if PUNTAJE1=='LOVE':
                PUNTAJE1='15'
                PUNTAJE_TOTAL.append(str(PUNTAJE1) +' - '+ str(PUNTAJE2))
                REPETIR='yes'
            else:
                if PUNTAJE1=='15':
                    PUNTAJE1='30'
                    PUNTAJE_TOTAL.append(str(PUNTAJE1) +' - '+ str(PUNTAJE2))
                    REPETIR='yes'
                else:
                    PUNTAJE1='40'
                    if PUNTAJE2=='40':
                        PUNTAJE_TOTAL.append("Deuce (empate)")
                        empate(PLAY1,PLAY2,PUNTAJE_TOTAL)
                        REPETIR='no'
                    else:
                        PUNTAJE_TOTAL.append(str(PUNTAJE1) +' - '+ str(PUNTAJE2))
                        REPETIR='yes'
        N=N+1
    else:
        if PUNTAJE2=='40':
            if PUNTAJE1=='40':
                PUNTAJE_TOTAL.append("Deuce (empate)")
                empate(PLAY1,PLAY2,PUNTAJE_TOTAL)
                REPETIR='no'
            else:
                PUNTAJE_TOTAL.append("Ganador del juego es "+PLAY2)
                REPETIR='no'
        else:
            if PUNTAJE2=='LOVE':
                PUNTAJE2='15'
                PUNTAJE_TOTAL.append(str(PUNTAJE1) +' - '+ str(PUNTAJE2))
                REPETIR='yes'
            else:
                if PUNTAJE2=='15':
                    PUNTAJE2='30'
                    PUNTAJE_TOTAL.append(str(PUNTAJE1) +' - '+ str(PUNTAJE2))
                    REPETIR='yes'
                else:
                    PUNTAJE2='40'
                    if PUNTAJE1=='40':
                        PUNTAJE_TOTAL.append("Deuce (empate)")
                        empate(PLAY1,PLAY2,PUNTAJE_TOTAL)
                        REPETIR='no'
                    else:
                        PUNTAJE_TOTAL.append(str(PUNTAJE1) +' - '+ str(PUNTAJE2))
                        REPETIR='yes'
        N=N+1


print("Resumen de puntuacion:")
for i in PUNTAJE_TOTAL:
    print(i)
