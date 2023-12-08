import random
from time import sleep
"""
/*
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
 *   
 */
"""


RED_CAR = "🚗"
GREEN_CAR = "🚙"
YELLOW_CAR = "🚕"
POLICE_CAR = "🚓"
MOTO = "🏍️"
TREE = "🌲"
DESTROYED_TREE = "🍂"
FINISH = "🏁"
ROAD = "_"
CRASH = "💥"

def create_roads(participants: list, distance: int=20) -> list:
    # Quiero que el código sea escalable ¿Que pasaría si entran más coches...?
    race = []
    for participant in participants: # por cada coche crearemos una carretera esa carretera estará en una lista
        # creo por cada participan una lista que será su road
        road = []
        # Numero de trees random
        random_trees = random.randint(1, 3)
        for i in range(0, distance):
            # le ponemos la acera
            road.append(ROAD) 
        for tree in range(random_trees):
            # Seleccionamos casillas random para arboles
            road_position = random.randint(1, distance-2)
            # ponemos los arbolitos
            road[road_position] = TREE 
        # Ponemos su marquita finish:
        road[0] = FINISH
        # Le ponemos su cochecito
        road[len(road) - 1] = participant
        # Iba a utilizar un namedtuple pero son immutables, así que un dict
        racer = {"car": participant, "road": road, "position": len(road)-1, "status": "go"}
        race.append(racer)
       
    # devolvemos nuestras "carreras"
    return race

def start_race(races):

    winners = []
    while len(winners) == 0:
        for race in races:
            # print(race)
            road = race['road']
            car = race['car']
            if race['status'] == "go":
                # set current position to road cell
                current_position =race['position']
                road[current_position] = ROAD
                new_position = current_position - random.randint(1, 3)
                if new_position <= 0:
                    road[0] = car
                    winners.append(car)
                    race['status'] = "WINNER"
                if road[new_position] == TREE:
                    print(f'{car} se estampa contra un arbol!')
                    race['position'] = new_position
                    race['status'] = CRASH
                    road[new_position] = CRASH
                elif race['status'] == "WINNER":
                    continue
                else:
                    road[new_position] = car
            else:
                print(f'{car} retoma su turno tas volver a la carretera!')
                road[race['position']] = DESTROYED_TREE
                # road[race['position'] +1] = car
                race['status'] = "go"

            race['position'] = new_position
            printable_road = "".join(road)
            print(printable_road)
        sleep(1)

        print("\n")
    print("Resultados:")
    for race in races:
        print("".join(race['road']))
    return winners
def print_winners(winners: list):
    if len(winners) > 1:
        winners_p = " ".join(winners)
        print(f"Empate entre {winners_p}")
    else:
        print(f' El ganador es: {winners[0]}')

if __name__ == "__main__":

    race_events = [
        [RED_CAR, GREEN_CAR],
        [RED_CAR, GREEN_CAR, YELLOW_CAR],
        [RED_CAR, GREEN_CAR, YELLOW_CAR, POLICE_CAR],
        [RED_CAR, GREEN_CAR, YELLOW_CAR, POLICE_CAR, MOTO]
    ]
    carrera = 1
    for participants in race_events:
        print(f'Carrera: {carrera}')
        # participants = [RED_CAR, GREEN_CAR]
        races = create_roads(participants, distance=20)
        print_winners(start_race(races))
        carrera += 1