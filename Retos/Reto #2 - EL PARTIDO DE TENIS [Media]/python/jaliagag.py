"""
# Reto #2: EL PARTIDO DE TENIS
#### Dificultad: Media | Publicación: 09/01/23 | Corrección: 16/01/23

## Enunciado
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   

#### Tienes toda la información extendida sobre los retos de programación semanales en **[retosdeprogramacion.com/semanales2023](https://retosdeprogramacion.com/semanales2023)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.
"""

#import randint

print('Arranca el partido y como es de esperar')

jugadores = {
    "P1" : "Love",
    "P2" : "Love"
}

comentarios = ["¡Qué gran partido!"]
comentarios_p1 = ["¡Gran punto para P1!"]
comentarios_p2 = ["¡Gran punto para P2!"]

puntos = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]

def suma_puntos(base,player):
    if base == "Love":
        base = "15"
        jugadores[player]=base
        print(player,base)
        return
    elif base == "15":
        base = "30"
        jugadores[player]=base
        print(player,base)
        return
    elif base == "30":
        base = "40"
        jugadores[player]=base
        print(player,base)
        return
    elif base == "40":
        base = "Win"
        jugadores[player]=base
        print(player,base)
        return

for i in puntos:
    #print(jugadores)
    suma_puntos(jugadores[i],i)
    if i == "P1":
        print(comentarios_p1[0])
    elif i == "P2":
        print(comentarios_p2[0])
