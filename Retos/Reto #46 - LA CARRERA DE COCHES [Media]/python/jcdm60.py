# Reto #46: La carrera de coches
#### Dificultad: Media | Publicación: 27/11/23 | Corrección: 04/12/23

## Enunciado

#
# Crea un programa que simule la competición de dos coches en una pista.
# - Los dos coches estarán representados por 🚙 y 🚗. Y la meta por 🏁.
# - Cada pista tendrá entre 1 y 3 árboles 🌲 colocados de forma aleatoria.
# - Las dos pistas tendrán una longitud configurable de guiones bajos "_".
# - Los coches comenzarán en la parte derecha de las pistas. Ejemplo:
#   🏁____🌲_____🚙
#   🏁_🌲____🌲___🚗
# 
# El juego se desarrolla por turnos de forma automática, y cada segundo
# se realiza una acción sobre los coches (moviéndose a la vez), hasta que
# uno de ellos (o los dos a la vez) llega a la meta.
# - Acciones:
#   - Avanzar entre 1 a 3 posiciones hacia la meta.
#   - Si al avanzar, el coche finaliza en la posición de un árbol,
#     se muestra 💥 y no avanza durante un turno.
#   - Cada turno se imprimen las pistas y sus elementos.
#   - Cuando la carrera finalice, se muestra el coche ganador o el empate.
# 

import random
import time

class CarRace:
    EMOJI_TREE = '🌲'
    EMOJI_EXPLOSION = '💥'
    EMOJI_CAR1 = '🚙'
    EMOJI_CAR2 = '🚗'
    EMOJI_FINISH = '🏁'
    MAX_ADVANCEMENT = 3

    def __init__(self, track_length=20):
        self.track_length = track_length
        self.finish_line = 0
        self.track_trees1 = self.generate_trees()
        self.track_trees2 = self.generate_trees()
        self.car1_position = self.track_length - 1
        self.car2_position = self.track_length - 1
        self.race_finished = False

    def generate_trees(self):
        return random.sample(range(1, self.track_length - 1), random.randint(1, min(3, self.track_length - 2)))

    def display_track(self):
        track1 = [self.EMOJI_TREE if i in self.track_trees1 else '_' for i in range(self.track_length)]
        track2 = [self.EMOJI_TREE if i in self.track_trees2 else '_' for i in range(self.track_length)]

        # Modificar el icono en la posición de la meta según el coche que llegue primero
        if self.finish_line == self.car1_position:
            track1[self.finish_line] = self.EMOJI_CAR1
            track2[self.finish_line] = self.EMOJI_FINISH
        elif self.finish_line == self.car2_position:
            track2[self.finish_line] = self.EMOJI_CAR2
            track1[self.finish_line] = self.EMOJI_FINISH
        else:
            track1[self.finish_line] = self.EMOJI_FINISH
            track2[self.finish_line] = self.EMOJI_FINISH

        # Mostrar los árboles y las posiciones de los coches
        track1[self.car1_position] = self.EMOJI_EXPLOSION if self.car1_position in self.track_trees1 else self.EMOJI_CAR1
        track2[self.car2_position] = self.EMOJI_EXPLOSION if self.car2_position in self.track_trees2 else self.EMOJI_CAR2

        print(''.join(track1))
        print(''.join(track2))
        print()


    def cars_turn(self):
        car1_advance = random.randint(1, self.MAX_ADVANCEMENT)
        car2_advance = random.randint(1, self.MAX_ADVANCEMENT)

        new_car1_position = max(self.car1_position - car1_advance, 0)
        if new_car1_position in self.track_trees1:
            car1_advance = 0

        new_car2_position = max(self.car2_position - car2_advance, 0)
        if new_car2_position in self.track_trees2:
            car2_advance = 0

        self.car1_position = new_car1_position
        self.car2_position = new_car2_position

        self.display_track()
        time.sleep(1)

        if self.car1_position <= self.finish_line or self.car2_position <= self.finish_line:
            self.race_finished = True

        return self.race_finished

    def start_race(self):
        print(f"Posición inicial de los coches (Longitud de la Pista: {self.track_length}):")
        self.display_track()

        while not self.race_finished:
            self.race_finished = self.cars_turn()

        if self.car1_position <= self.finish_line and self.car2_position <= self.finish_line:
            print("Es un empate!")
            self.finish_line = min(self.car1_position, self.car2_position)
        elif self.car1_position <= self.finish_line:
            self.finish_line = self.car1_position
        else:
            self.finish_line = self.car2_position

        self.display_track()
        if self.finish_line == self.car1_position and self.finish_line == self.car2_position:
            print("Es un empate!")
        elif self.finish_line == self.car1_position:
            print("El Coche 🚙 ha ganado la carrera!")
        else:
            print("El Coche 🚗 ha ganado la carrera!")

if __name__ == "__main__":
    track_length = int(input("Ingrese la longitud de la pista: "))

    race = CarRace(track_length)
    race.start_race()
