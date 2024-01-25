# # Reto #2: EL PARTIDO DE TENIS
# #### Dificultad: Media | Publicación: 09/01/23 | Corrección: 16/01/23

# ## Enunciado

# ```
# /*
#  * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
#  * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
#  * gane cada punto del juego.
#  * 
#  * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
#  * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#  *   15 - Love
#  *   30 - Love
#  *   30 - 15
#  *   30 - 30
#  *   40 - 30
#  *   Deuce
#  *   Ventaja P1
#  *   Ha ganado el P1
#  * - Si quieres, puedes controlar errores en la entrada de datos.   
#  * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
#  */
# ```
# #### Tienes toda la información extendida sobre los retos de programación semanales en **[retosdeprogramacion.com/semanales2023](https://retosdeprogramacion.com/semanales2023)**.

# Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

# > Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.


juego = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
puntuacion = {0:"Love", 1:"15", 2:"30", 3:"40"}



def juegoTennis(juego):
    resta=0
    contadorp1=0
    contadorp2=0

    for i in juego:
        if i=="P1":
            contadorp1+=1
        
        if i=="P2":
            contadorp2+=1


        if contadorp1<3 or contadorp2<3:
            print(f"{puntuacion[contadorp1]} - {puntuacion[contadorp2]}")  
        elif contadorp1==3 and contadorp2==3:
            print("Deuce")
        elif contadorp1>3 or contadorp2>3:
            resta = contadorp1-contadorp2
            if resta==0:
                print("Deuce")
            elif resta==1:
                print("Ventaja P1")
            elif resta==2:
                print("Ganador P1")
            elif resta==-1:
                print("Ventaja P2")
            elif resta==-2:
                print("Ganador P2")

juegoTennis(juego)


juego1 = ["P1", "P2", "P2", "P1", "P1", "P2", "P1", "P2","P2","P2"]

juegoTennis(juego1)