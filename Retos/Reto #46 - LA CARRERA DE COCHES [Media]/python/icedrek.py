"""
 * Crea un programa que simule la competición de dos coches en una pista.
 * - Los dos coches estarán representados por 🚙 y 🚗. Y la meta por 🏁.
 * - Cada pista tendrá entre 1 y 3 árboles 🌲 colocados de forma aleatoria.
 * - Las dos pistas tendrán una longitud configurable de guiones bajos "_".
 * - Los coches comenzarán en la parte derecha de las pistas. Ejemplo:
 *   🏁____🌲_____🚙
 *   🏁_🌲____🌲___🚗
 * 
 * El juego se desarrolla por turnos de forma automática, y cada segundo
 * se realiza una acción sobre los coches (moviéndose a la vez), hasta que
 * uno de ellos (o los dos a la vez) llega a la meta.
 * - Acciones:
 *   - Avanzar entre 1 a 3 posiciones hacia la meta.
 *   - Si al avanzar, el coche finaliza en la posición de un árbol,
 *     se muestra 💥 y no avanza durante un turno.
 *   - Cada turno se imprimen las pistas y sus elementos.
 *   - Cuando la carrera finalice, se muestra el coche ganador o el empate.
"""

import os
import time
import random


class Player:
    def __init__(self, position, icon):
        self.position = position
        self.icon = icon
        self.crash = False

    def move(self, movement):
        self.position -= movement

        if self.position < 0:
            self.position = 0


def main():
    circuit_size = random.randint(10, 20)

    player_1 = Player(circuit_size + 1, "🚙")
    player_2 = Player(circuit_size + 1, "🚗")

    circuit_1 = make_circuit(circuit_size, player_1.icon)
    circuit_2 = make_circuit(circuit_size, player_2.icon)

    race(circuit_1, circuit_2, player_1, player_2)


def make_circuit(circuit_size: int, car: str):
    circuit = list("🏁")
    tree_counter = 0

    for _ in range(circuit_size):
        stretch = random.randint(0, 100)

        if stretch >= 90:
            tree_counter += 1
            circuit.append("_" if tree_counter > 3 else "🌲")
        else:
            circuit.append("_")

    if tree_counter == 0:
        circuit[-1] = "🌲"

    circuit.append(car)

    return circuit


def race(circuit_1: list, circuit_2: list, player_1: Player, player_2: Player):
    clear_screen()

    print("\nCOMIENZA LA CARRERA!!!")
    draw_circuit(circuit_1)
    draw_circuit(circuit_2)

    while True:
        time.sleep(1)
        clear_screen()

        if player_1.crash:
            player_1.crash = False
            print(f"{player_1.icon} se ha estrellado")
        else:
            move_car(circuit_1, player_1)

        if player_2.crash:
            player_2.crash = False
            print(f"{player_2.icon} se ha estrellado")
        else:
            move_car(circuit_2, player_2)

        draw_circuit(circuit_1)
        draw_circuit(circuit_2)

        if player_1.position == 0 and player_2.position == 0:
            print(f"EMPATE!!!")
            break

        if player_1.position == 0:
            print(f"GANADOR {player_1.icon}")
            break

        if player_2.position == 0:
            print(f"GANADOR {player_2.icon}")
            break


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def draw_circuit(circuit: list):
    for _ in circuit:
        print(_, end="")

    print("\n")


def move_car(circuit: list, player: Player):
    movement = random.randint(1, 3)

    if circuit[player.position] == "💥":
        circuit[player.position] = "🌲"
    else:
        circuit[player.position] = "_"

    player.move(movement)

    if circuit[player.position] == "🌲":
        player.crash = True
        circuit[player.position] = "💥"
    else:
        circuit[player.position] = player.icon

    print(f"{player.icon} avanza {movement} posiciones")


if __name__ == "__main__":
    main()
