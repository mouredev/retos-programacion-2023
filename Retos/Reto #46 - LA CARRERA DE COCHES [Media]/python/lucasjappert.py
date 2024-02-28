'''
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
'''

MAX_NUMBER_OF_TREES_BY_TRACK = 10
TRACK_LENGTH: int = 50
SLEEP_IN_SECONDS_TO_USE_IN_THE_WHILE_LOOP: float = 0.2

from enum import Enum
import os
import time
import random

class Car:
    def __init__(self, texture: str, position: int, id: int):
        self.texture = texture
        self.position = position
        self.missed_turn = False
        self.id = id

    def update(self, trees_positions_of_track1: list[int]):
        if self.missed_turn:
            self.missed_turn = False
            return
        
        self.position -= random.randint(1, 3)
        if self.position < 0: self.position = 0

        self.missed_turn = self.position in trees_positions_of_track1

class Textures(Enum):
    tree = "🌲"
    car1 = "🚙"
    car2 = "🚗"
    road_part = "_"
    explotion = "💥"
    flag = "🏁"

def _get_random_positions_of_trees():
    trees_positions: list[int] = []
    while MAX_NUMBER_OF_TREES_BY_TRACK > len(trees_positions):
        random_position = random.randint(1, TRACK_LENGTH-2)
        if random_position not in trees_positions:
            trees_positions.append(random_position)
    return trees_positions

def _get_part_of_track(car: Car, part_of_track_index: int, trees_positions: list[int]):
    if car.position == part_of_track_index == 0: return car.texture

    if part_of_track_index == 0: return Textures.flag.value

    if part_of_track_index in trees_positions:
        if car.position == part_of_track_index: return Textures.explotion.value
        return Textures.tree.value

    if car.position == part_of_track_index: return car.texture

    return Textures.road_part.value

def _print_results(car1: Car, car2: Car):
    separator = "##################################################"
    if car1.position == 0 == car2.position:
        return print(f"{separator}\n La carrera ha finalizado con un EMPATE \n{separator}")

    if car1.position == 0: return print(f"{separator}\n Ha ganado el AUTO {car1.texture} \n{separator}")
    if car2.position == 0: return print(f"{separator}\n Ha ganado el AUTO {car2.texture} \n{separator}")

def _print_track_car(car: Car, trees_positions_of_track: list[int]):
    text_track = ""
    for track_index in range(TRACK_LENGTH):
        text_track += _get_part_of_track(car, track_index, trees_positions_of_track)
    print(text_track)

def start_race():
    car1 = Car(Textures.car1.value, TRACK_LENGTH - 1, 1)
    car2 = Car(Textures.car2.value, TRACK_LENGTH - 1, 2)
    trees_positions_of_track1 = _get_random_positions_of_trees()
    trees_positions_of_track2 = _get_random_positions_of_trees()
            
    while (0 not in [car1.position, car2.position]):
        os.system("cls")

        car1.update(trees_positions_of_track1)
        car2.update(trees_positions_of_track2)

        _print_track_car(car1, trees_positions_of_track1)
        _print_track_car(car2, trees_positions_of_track2)

        time.sleep(SLEEP_IN_SECONDS_TO_USE_IN_THE_WHILE_LOOP)

    _print_results(car1, car2)

start_race()