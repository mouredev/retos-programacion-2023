# /*
#  * Crea un programa que simule la competición de dos coches en una pista.
#  * - Los dos coches estarán representados por 🚙 y 🚗. Y la meta por 🏁.
#  * - Cada pista tendrá entre 1 y 3 árboles 🌲 colocados de forma aleatoria.
#  * - Las dos pistas tendrán una longitud configurable de guiones bajos "_".
#  * - Los coches comenzarán en la parte derecha de las pistas. Ejemplo:
#  *   🏁____🌲_____🚙
#  *   🏁_🌲____🌲___🚗
#  * 
#  * El juego se desarrolla por turnos de forma automática, y cada segundo
#  * se realiza una acción sobre los coches (moviéndose a la vez), hasta que
#  * uno de ellos (o los dos a la vez) llega a la meta.
#  * - Acciones:
#  *   - Avanzar entre 1 a 3 posiciones hacia la meta.
#  *   - Si al avanzar, el coche finaliza en la posición de un árbol,
#  *     se muestra 💥 y no avanza durante un turno.
#  *   - Cada turno se imprimen las pistas y sus elementos.
#  *   - Cuando la carrera finalice, se muestra el coche ganador o el empate.
#  */

from enum import Enum
import os
import random
import time

class Textures(Enum):
    EMPTY = "_"
    TREE = "🌲"
    FINISH = "🏁"
    CRASH = "💥"
    CAR1 = "🚙"
    CAR2 = "🚗"

class Car:
    def __init__(self, name: str, texture: str, position: int):
        self.name = name
        self.texture = texture
        self.position = position
        self.crashed = False 

    def move(self, distance: int, trees: list):
        if self.crashed:  
            self.crashed = False
            self.texture = Textures.CAR1.value if self.name == "Car1" else Textures.CAR2.value
            return

        if self.position - distance in trees:
            self.position -= distance
            self.crashed = True
            self.texture = Textures.CRASH.value
            return

        self.position -= distance

class Race:
    def __init__(self, length: int, trees: int):
        self.length = length
        self.trees = random.sample(range(1, length - 1), trees)
        self.car1 = Car("Car1", Textures.CAR1.value, length - 1)
        self.car2 = Car("Car2", Textures.CAR2.value, length - 1)
        self.track1 = [Textures.EMPTY.value] * length
        self.track2 = [Textures.EMPTY.value] * length

    def _generate_track(self):
        self.track1[0] = Textures.FINISH.value
        self.track2[0] = Textures.FINISH.value
        for tree in self.trees:
            self.track1[tree] = Textures.TREE.value
            self.track2[tree] = Textures.TREE.value
    
    def _print_track(self):
        print("Pista 1".center(50, "-") + "\n")
        print("".join(self.track1[:self.car1.position]) + (self.car1.texture) + "".join(self.track1[self.car1.position + 1:]))
        print("Pista 2".center(50, "-") + "\n")
        print("".join(self.track2[:self.car2.position]) + (self.car2.texture) + "".join(self.track2[self.car2.position + 1:]))
        

    def start(self):        
        self._generate_track()
        while self.car1.position >= 0 and self.car2.position >= 0:
            self.car1.move(random.randint(1, 3), self.trees)
            self.car2.move(random.randint(1, 3), self.trees)
            self._print_track()
            time.sleep(0.2)
            os.system('cls')

        if self.car1.position == 0 and self.car2.position == 0:
            return print("Empate")
        if self.car1.position <= 0:
            return print("El auto 1 ganó")
        if self.car2.position <= 0:
            return print("El auto 2 ganó")

race = Race(20, 5)
race.start()
