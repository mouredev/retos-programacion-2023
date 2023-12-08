from os import system
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




APP_NAME = """
#######################################
              Race Car

            by infolojo
          https:://infolojo.es
        Antonio José Lojo Ojeda
#######################################
"""




class Car:
    def __init__(self, player: str, car_image: str, pista: int, type: int):
        self.player: str = player
        self.car_image: str = car_image,
        self.pista: int = pista
        self.position: int = pista + 1
        self.crashed: bool = False,
        self.type: int = type

    def get_car_image(self):
        return self.car_image[0]

    def update_position(self, new_position: int):
        self.position = new_position


class Race:
    def __init__(self, player_one: Car, player_two: Car):
        self.current: int
        self.example: str
        self.crash: str = "💥"
        self.tree: str = "🌲"
        self.final: str = "🏁"
        self.cars = (player_one, player_two)
        self.pista_car_one = ""
        self.pista_car_two = ""
        self.initi_config()

    def initi_config(self):
        """Prepare pista with trees and crashes
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        

    def clear_screen(self):
        # uncomment by checking your or
        # clear windows screen
        # os.system('CLS')
        # clear linux screen
        system('clear')

    def get_random_tree_positions(self, size_pista: int): 
        """Get random trees 1 or 3 and random position of each trees
        
        Keyword arguments:
        argument -- description
        Return: array of trees
        """
        number_of_trees = random.randint(1, 3)
        index: int = 0
        trees: list = []

        while (index < number_of_trees):
            index += 1
            trees.append(random.randint(1, size_pista -1))

        return trees


    def build_pist(self, car: Car, pista: str, trees: list):
        i = 0
        while (True):
            if i == 0:
                pista += "🏁"
            
            elif i in trees:
                trees.remove(i)
                pista += self.tree

            elif car.position == i:
                pista += car.get_car_image()
                return pista
            else:
                pista += "_"
            i += 1
        

    def prepare_pista(self):
        car_one_pista: str = self.build_pist(
            car = self.cars[0], 
            pista = self.pista_car_one, 
            trees = self.get_random_tree_positions(
                size_pista = self.cars[0].position
            )
            
        )
        
        car_two_pista: str = self.build_pist(
            car = self.cars[1], 
            pista = self.pista_car_two, 
            trees = self.get_random_tree_positions(
                size_pista = self.cars[1].position
            )
        )

        self.pista_car_one = car_one_pista
        self.pista_car_two = car_two_pista
        
        # TODO SAVE PISTAS ?
        print(f"{self.cars[0].player} - {car_one_pista}")
        print(f"{self.cars[1].player} - {car_two_pista}")


    def check_winners(self):
        winner_found: bool = False
        car_one = self.cars[0]
        car_two = self.cars[1]
        if car_one.position == 1 and car_two.position == 1:
            print(f"{car_one.player} and {car_two.player} are the WINNERS !!")
            winner_found = True

        elif car_one.position == 1:
            print(f"{car_one.player} WINS !!")
            winner_found = True

        elif car_two.position == 1:
            print(f"{car_two.player} WINS !!")
            winner_found = True

        return winner_found
    

    def update_positions(self, type):
        if type == 1:
            self.cars[0].position -= 1
        elif type == 2:
            self.cars[1].position -= 1

    def update_pista(self, type: int, pista: str):
        if type == 1:
            self.pista_car_one = pista
        elif type == 2:
            self.pista_car_two = pista


    def update_crashes(self, type, value: bool):
        if type == 1:
            self.cars[0].crashed = value
        elif type == 2:
            self.cars[1].crashed = value


    def launch_single_round(self, car: Car, pista: str):
        # Prepare data
        pista_list = list(pista)
        next_position = car.position -1

        # Check to skip single round
        if car.crashed == True:
            self.update_crashes(type = car.type, value=False) 

            # print pista
            self.build_and_print_pista(car = car, pista_list = pista_list)
            return
        

        # update pista
        if (pista_list[next_position] == self.tree):
            pista_list[next_position] = self.crash
            self.update_crashes(type = car.type, value = True)
        
        else:
            pista_list[next_position] = car.get_car_image()

        # remove last position    
        pista_list.pop(car.position)
        

        # update cars positions
        self.update_positions(type = car.type)

        # print pista
        self.build_and_print_pista(car = car, pista_list = pista_list)


    def build_and_print_pista(self, car: Car, pista_list: list):
        # build pista
        pista_builded: str = "".join(pista_list)
        
        # print pista
        print(f"{car.player} - {pista_builded}")

        # update pista
        self.update_pista(type = car.type, pista = pista_builded)


    def launch_rounds(self):
        while (True):
            self.clear_screen()
            print(APP_NAME)
            if self.check_winners() == True:
                # finish
                return
            else:
                # print round on pista and check if crash
                self.launch_single_round(self.cars[0], self.pista_car_one)
                self.launch_single_round(self.cars[1], self.pista_car_two)
            sleep(.5)

    
    def start_race(self):
        self.clear_screen()
        print(APP_NAME)
        self.prepare_pista()
        self.launch_rounds()
        
        
if __name__ == "__main__":
    car_one = Car(player = "Crisitian", car_image = "🚙", pista = 10, type = 1)
    car_two = Car(player = "Joaquin", car_image = "🚗", pista = 10, type = 2)
    Race(player_one = car_one, player_two = car_two).start_race()
