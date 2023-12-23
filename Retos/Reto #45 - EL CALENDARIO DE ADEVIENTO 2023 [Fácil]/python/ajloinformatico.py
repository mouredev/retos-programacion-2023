import os
import random

"""
/*
 * ¿Conoces el calendario de aDEViento de la comunidad (https://adviento.dev)?
 * 24 días, 24 regalos sorpresa relacionados con desarrollo de software.
 * Desde el 1 al 24 de diciembre.
 *
 * Crea un programa que simule el mecanismo de participación:
 * - Mediante la terminal, el programa te preguntará si quieres añadir y borrar
 *   participantes, mostrarlos, lanzar el sorteo o salir.
 * - Si seleccionas añadir un participante, podrás escribir su nombre y pulsar enter.
 * - Si seleccionas añadir un participante, y este ya existe, avisarás de ello.
 *   (Y no lo duplicarás)
 * - Si seleccionas mostrar los participantes, se listarán todos.
 * - Si seleccionas eliminar un participante, podrás escribir su nombre y pulsar enter.
 *   (Avisando de si lo has eliminado o el nombre no existe)
 * - Si seleccionas realizar el sorteo, elegirás una persona al azar 
 *   y se eliminará del listado.
 * - Si seleccionas salir, el programa finalizará.
 */
"""

APP_NAME = """
#######################################
              Lottery

            by infolojo
          https:://infolojo.es
        Antonio José Lojo Ojeda
#######################################
"""

class Competitor:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class ErrorMessages:
    def __init__(self):
        self.no_competitors: str = "There are not registered competitors yet"
        self.id_type_error: str = "Error: I think that was not an id"
        self.not_found: str = "Competitor not found"
        self.empty_name: str = "Competitor name can not be empty"
        self.duplicated: str = "We have a competitor registered with this name"
    
class Lottery:
    def __init__(self, competitors: list = list(), lastId = 0):
        self.commands: str = """
Please select a command (id or name):
    0. commands
    1. add
    2. remove
    3. list
    4. Play
    5. exit
        """
        self.currentLottery: int = 0
        self.lastId: int = lastId
        self.app_name: str = APP_NAME
        self.error_manager: ErrorMessages = ErrorMessages()
        self.competitors: list = competitors

    # region main class methods
    def start(self):
        self.start

    def clear(self):
        # uncomment by checking your or
        # clear windows screen
        os.system('CLS')
        # clear linux screen
        # os.system('clear')

    def add(self, competitor: Competitor):
        self.competitors.append(competitor)

    def remove(self, idOrName: str):
        id: int = -1
        name: str = ""
        
        try:
            id = int(idOrName)
        except:
            name = idOrName.lower().capitalize()
        
        for competitor in self.competitors:
            if competitor.id == id or name == competitor.name:
                print(competitor.name + " has been removed")
                self.competitors.remove(competitor)
                return
        
        print(self.error_manager.not_found)
            
    def are_competitors_empty(self): 
        if (len(self.competitors) == 0):
            print(self.error_manager.no_competitors)
            return True
        return False
    
    def check_if_exists(self, name: str):
        for competitor in self.competitors:
            if competitor.name == name:
                print(self.error_manager.duplicated)
                return True
        return False
    # endregion main class methods

    # region menu actions
    def print_commands(self):
        print(self.commands)

    def print_competitors(self):
        if self.are_competitors_empty():
            return
        
        print("Registered competitors:\n")
        for competitor in self.competitors:
            print(str(competitor.id) + "-" + competitor.name)

    def create_new_user(self, id: int):
        name: str = input(">>> Input new competitor name: ").lower().capitalize()
        if name == "":
            print(self.error_manager.empty_name)
            return
        if self.check_if_exists(name):
            return

        new_competitor = Competitor(id, name)
        self.add(new_competitor)
        print(f"\n {name} has been added")

    def remove_competitor(self):
        if self.are_competitors_empty():
            return
        
        print(f">>> Input id or  name competitor that you want to remove:\n")
        self.print_competitors()
        competitorToRemove: str = input("\n>>> ")
        self.remove(competitorToRemove)

    def play(self):
        if self.are_competitors_empty():
            return
        winner = random.choice(self.competitors)
        print(f"The winner of {self.currentLottery} is {winner.name}")        
        self.currentLottery += 1

    def exit(self):
        print("\n Thanks for using and See you soon \n")
        exit(-1)

    # endregion menu actions

    # region main loop
    def start(self):
        self.clear()
        print(APP_NAME)
        self.print_commands()
        while (True):  
            userInput: str = input("\n>>> Select one option ")

            if userInput == "0" or userInput == "commands":
                self.clear()
                self.print_commands()

            elif userInput == "1" or userInput == "add":
                self.clear()
                self.lastId += 1
                self.create_new_user(self.lastId)
            
            elif userInput == "2" or userInput == "remove":
                self.clear()
                self.remove_competitor()

            elif userInput == "3" or userInput == "list":
                self.clear()
                self.print_competitors()

            elif userInput == "4" or userInput == "play":
                self.clear()
                self.play()

            elif userInput == "5" or userInput == "exit":
                self.clear()
                self.exit()

            else:
                self.clear()
                print("not a valid input")

            print("\n-Remmember 0 to print commands-")
    # endregion main loop
        

def seeder():
    return Lottery(
        [
            Competitor(
                1,
                "Juan"
            ), 
            Competitor(
                2,
                "Maria"
            ),
            Competitor(
                3,
                "Alicia"
            ),
            Competitor(
                4,
                "Toni"
            ),
            Competitor(
                5,
                "Euge"
            )
        ],
        5
    )

    
if __name__ == "__main__":
    # If you want to use mock uncomment this and comment next app = Lottery() 
    # app = seeder()
    app = Lottery()
    app.start()
