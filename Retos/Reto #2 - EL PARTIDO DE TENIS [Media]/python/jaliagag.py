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


jugadores = {
    "P1"    : "Love",
    "P2"    : "Love",
}

orden = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]

puntos = ["Love", 15, 30, 40, "Ventaja", "Ha ganado"]

def shout_scores(player_scored):
    actual_pos = puntos.index(jugadores[player_scored])
    if jugadores["P1"] == 40 and jugadores["P2"] == 40:
        print("Deuce")
        jugadores[player_scored] = puntos[actual_pos+1]
        print("Ventaja",player_scored)
    else:
        jugadores[player_scored] = puntos[actual_pos+1]
        if jugadores[player_scored] == "Ha ganado":
            print("Ha ganado",player_scored)
        else:
            print(jugadores["P1"],"-",jugadores["P2"])

for i in orden:
    shout_scores(i)
