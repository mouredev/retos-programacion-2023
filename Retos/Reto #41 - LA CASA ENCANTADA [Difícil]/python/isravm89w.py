import random
from enum import Enum


class Direction(Enum):
    UP = "Arriba"
    DOWN = "Abajo"
    LEFT = "Izquierda"
    RIGHT = "Derecha"


class Position:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, __value: object) -> bool:
        return __value.x == self.x and __value.y == self.y

    def __str__(self) -> str:
        return f"{self.x, self.y}"


class Riddle:
    content: str
    possible_answers: list[str]

    def __init__(self, content: str, possible_answers: list[str]) -> None:
        self.content = content
        self.possible_answers = possible_answers
    
    def __str__(self) -> str:
        return " ".join(self.possible_answers)


class HalloweenHouse:
    riddles: list[Riddle]
    current_room: Position
    door_position: Position
    candies_position: Position
    width: int
    height: int

    def __init__(self, width: int = 4, height: int = 4) -> None:

        # Initialize house dimentions
        self.width = width
        self.height = height
        # Initialize door and candies postions
        self.door_position = self.__generate_door_position()
        self.candies_position = self.__generate_candies_position()
        # Set curent_room same as the door position
        self.current_room = Position(self.door_position.x, self.door_position.y)

        self.riddles = [
            Riddle(
                "Tiene famosa memoria, gran tamaño y dura piel y la nariz más grandota, que en el mundo pueda haber", 
                ["el elefante", "elefante"]
                ),
            Riddle(
                "En rincones y entre ramas mis redes voy construyendo, para que moscas incautas, en ellas vayan cayendo", 
                ["la araña", "araña"]
                ),
            Riddle(
                "Camino sin tener patas, a cuestas llevo mi casa. Por donde mi cuerpo pasa queda un hilillo de plata.", 
                ["el caracol", "caracol"]
                ),
            Riddle(
                "Por un caminito, va caminando un bicho. El nombre del bicho ya te lo he dicho.", 
                ["la vaca", "vaca"]
                ),
            Riddle(
                "Si me tumbas, soy todo. Si me cortas por la cintura, me quedo en nada.",
                ["el ocho", "ocho", "8", "el 8"]
                ),
            Riddle("Tengo orejas largas y una cola diminuta. Si echamos una carrera, gano sin disputa.",
                ["el conejo", "conejo"]
                ),
            Riddle(
                "No es un ser vivo, pero tiene cinco dedos ¿Qué es?", 
                ["un guante", "guante"]
                ),
            Riddle(
                "Si me das de comer viviré más, pero si me das de beber moriré. ¿Qué soy?", 
                ["el fuego", "fuego"]
                ),
            Riddle(
                "¿Qué es completamente tuyo, pero solo lo usan los demás?", 
                ["mi nombre", "el nombre", "nombre"]
                ),
            Riddle(
                "Atraviesa ciudades y campos, pero nunca se mueve de lugar ¿Qué es?", 
                ["el camino", "un camino", "autopista", "carretera"]
                ),
            Riddle(
                "Sin luz no existo, pero si me da la luz me muero. ¿Quién soy?", 
                ["la sombra", "sombra"]
                ),
            Riddle(
                "Oro parece y plata no es, quien no lo adivine tonto es.", 
                ["platano", "plátano", "el platano", "el plátano", "banana", "la banana"]
                ),
            Riddle(
                "No tengo cabeza, pero sí cuello.", 
                ["una botella", "botella", "la botella"]
                ),
            Riddle(
                "Un caballo blanco entró en el Mar Negro. ¿Cómo salió?", 
                ["mojado"]
                ),
            Riddle(
                "¿Cuál es la mujer que siempre sabe donde está su marido?",
                ["la viuda", "viuda"]
                ),
            Riddle(
                "¿Qué se moja al secar?", 
                ["la toalla", "toalla"]
                ),
        ]
    
    def __generate_door_position(self):
        return self.__generate_position()

    def __generate_candies_position(self):
        position = self.__generate_position()
        while position == self.door_position:
            position = self.__generate_position()

        return position

    def __generate_position(self) -> Position:
        return Position(random.randint(1, self.width), random.randint(1, self.height))
    
    def __get_riddle(self) -> Riddle:
        return random.choice(self.riddles)
    
    def __get_available_options(self):
        """
        Check for available movements
        """
        available_options = []
        if self.current_room.x > 1:
            available_options.append(Direction.LEFT)
        if self.current_room.x < self.width:
            available_options.append(Direction.RIGHT)
        if self.current_room.y > 1:
            available_options.append(Direction.UP)
        if self.current_room.y < self.height:
            available_options.append(Direction.DOWN)
        
        return available_options
    
    def __is_a_ghost_in_the_room(self) -> bool:
        """
        Calculate if there is a ghost in the room (10% of the times)
        """

        # Calculate 10% of the rooms to get numbers of possible rooms to be a ghost
        possible_rooms = self.height * self.width
        ghost_rooms = round((possible_rooms * 0.1))
        # Generate a list simulating rooms(1 - have a ghost, 0 - don't)
        generated_rooms_with_ghosts = [1] * ghost_rooms + [0] * (possible_rooms - ghost_rooms)
        # Make list some ramdom
        random.shuffle(generated_rooms_with_ghosts)
        # Get a random element and return if there is a ghost or not
        return bool(random.choice(generated_rooms_with_ghosts))
    
    def __process_menu_options(self) -> Direction:
        """
        Draw options menu and return a valid selected direction
        """

        # Get available options and print each one with a generated option number
        options = self.__get_available_options()
        options_len = len(options)
        option_and_number = {}
        print("Seleciona a que habitación deseas ir:")
        for index in range(0, options_len):
            option_number = index+1
            # Associate generated option number with the option
            option_and_number[option_number] = options[index].value
            print(f"{option_number} - {options[index].value}")
        
        # Add the option to exit at any time
        print("0 - Salir del juego")

        try:
            direction = int(input())
            if direction == 0:
                print("Hasta pronto!!")
                exit()

            if direction < 0 or direction > options_len:
                print("Seleccione una opción válida")
                self.__process_menu_options()

            return option_and_number.get(direction)
        except ValueError:
            print("Inserte un número válido")
            self.__process_menu_options()
    
    def __process_current_room(self):

        if self.current_room == self.candies_position:
            print("FELICIDADES!!! Haz encontrado los dulces!!!!")
            exit()

        if self.current_room == self.door_position:
            print("Haz llegado a la puerta nuevamente!!!")
            return
        
        riddles_to_pass = 1
        if self.__is_a_ghost_in_the_room():
            print("Te haz encontrado con un fantasma. Deberas responder un acertijo adicional para poder avanzar.")
            riddles_to_pass += 1

        alredy_asked = []
        while riddles_to_pass > 0:
            print(f"Acertijos restantes: {riddles_to_pass}")
            current_riddle = self.__get_riddle()
            if current_riddle in alredy_asked:
                continue
            
            print(current_riddle.content)
            alredy_asked.append(current_riddle)

            answer = input()
            while answer not in current_riddle.possible_answers:
                print("Respuesta incorrecta. Intentalo nuevamente.")
                answer = input()
            print("Correcto!")
            riddles_to_pass -= 1

    def start_game(self):
        print("BIENVENIDOS A LA CASA ENCANTADA")

        while True:
            # Get direction to go
            direction = self.__process_menu_options()
            # Move to the room
            self.__move(direction=direction)
            # Check current room
            self.__process_current_room()
            print("-------------------------------------")

    def __move(self, direction: Direction):
        if direction == Direction.DOWN.value:
            self.current_room.y += 1
        if direction == Direction.UP.value:
            self.current_room.y -= 1
        if direction == Direction.RIGHT.value:
            self.current_room.x += 1
        if direction == Direction.LEFT.value:
            self.current_room.x -= 1

if __name__ == "__main__":

    halloween_house = HalloweenHouse()
    halloween_house.start_game()
