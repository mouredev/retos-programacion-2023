from random import randint, choice


def init():
    MAPS = {
        1: [
            ["🚪", "⬜️", "⬜️", "⬜️"],
            ["⬜️", "👻", "⬜️", "⬜️"],
            ["⬜️", "⬜️", "⬜️", "👻"],
            ["⬜️", "⬜️", "🍭", "⬜️"]
        ],
        2: [
            ["🚪", "⬜️", "⬜️", "⬜️"],
            ["👻", "⬜️", "⬜️", "⬜️"],
            ["⬜️", "⬜️", "⬜️", "🍭"],
            ["⬜️", "⬜️", "👻", "⬜️"]
        ],
        3: [
            ["⬜️", "⬜️", "⬜️", "🍭"],
            ["⬜️", "👻", "⬜️", "⬜️"],
            ["⬜️", "⬜️", "👻", "⬜️"],
            ["🚪", "⬜️", "⬜️", "⬜️"]
        ],
        4: [
            ["⬜️", "👻", "⬜️", "⬜️"],
            ["🍭", "⬜️", "⬜️", "⬜️"],
            ["⬜️", "⬜️", "👻", "⬜️"],
            ["⬜️", "⬜️", "🚪", "⬜️"]
        ],
        5: [
            ["⬜️", "⬜️", "👻", "⬜️"],
            ["👻", "⬜️", "⬜️", "⬜️"],
            ["⬜️", "⬜️", "🍭", "⬜️"],
            ["⬜️", "⬜️", "🚪", "⬜️"]
        ],
        6: [
            ["⬜️", "⬜️", "👻", "🍭"],
            ["⬜️", "⬜️", "⬜️", "⬜️"],
            ["🚪", "⬜️", "⬜️", "⬜️"],
            ["⬜️", "⬜️", "⬜️", "👻"]
        ],
        7: [
            ["⬜️", "⬜️", "👻", "⬜️"],
            ["⬜️", "⬜️", "⬜️", "🍭"],
            ["🚪", "⬜️", "⬜️", "⬜️"],
            ["⬜️", "⬜️", "⬜️", "👻"]
        ],
        8: [
            ["⬜️", "⬜️", "👻", "⬜️"],
            ["🍭", "⬜️", "⬜️", "⬜️"],
            ["⬜️", "⬜️", "⬜️", "🚪"],
            ["⬜️", "⬜️", "👻", "⬜️"]
        ],
        9: [
            ["⬜️", "⬜️", "🚪", "⬜️"],
            ["👻", "⬜️", "⬜️", "⬜️"],
            ["⬜️", "⬜️", "⬜️", "👻"],
            ["⬜️", "⬜️", "⬜️", "🍭"]
        ],
        10: [
            ["⬜️", "👻", "⬜️", "⬜️"],
            ["⬜️", "⬜️", "⬜️", "🚪"],
            ["👻", "⬜️", "⬜️", "⬜️"],
            ["⬜️", "⬜️", "⬜️", "🍭"]
        ]
    }

    print("\nBienvenido a la Mansión Encantada!\n" +
          "Para salir deberás responder preguntas en cada habitación.\n" +
          "Al resolver correctamente un enigma, podrás desplazarte a la\n" +
          "siguiente habitación.\n" +
          "La partida acabará cuando llegues a la sala de los dulces.\n")

    GAME_MAP = MAPS[randint(1, len(MAPS))]
    main(GAME_MAP)


def main(GAME_MAP: list[list]):
    def print_map(player_position):
        length: int = len(GAME_MAP)
        printable_map: list[list] = [[GAME_MAP[i][j]
                                      for j in range(length)] for i in range(length)]

        for i in range(length):
            for j in range(length):
                if seen_map[i][j] == 0:
                    if GAME_MAP[i][j] == "🚪":
                        printable_map[i][j] = "🚪"
                    elif GAME_MAP[i][j] == "👻":
                        printable_map[i][j] = "⬜️"
                    else:
                        printable_map[i][j] = "⬜️"
                elif player_position and (i == player_position["x"] and j == player_position["y"]):
                    printable_map[i][j] = "👤"
                elif GAME_MAP[i][j] == "🚪":
                    printable_map[i][j] = "🚪"
                elif GAME_MAP[i][j] == "👻":
                    printable_map[i][j] = "👻"

        for i in printable_map:
            print("".join(map(str, i)))
        print("")

    def ask_question(*room):
        question, choices = choice(list(QUESTIONS.items()))
        print(f"ENIGMA! {question}")

        for index, answer in enumerate(choices):
            print(f"\t{index + 1}: {answer}")

        correct_answer: int = list(choices.values()).index(1)

        answer = int(input("Respuesta: ")) - 1
        if answer != correct_answer:
            print("Incorrecto!")
            ask_question()
        print("Correcto!")
        if room:
            print("Oh no! Un fantasma te ha atrapado!")
            print("Debes responder otra pregunta para poder salir de la habitación.")
            ask_question()

    def find_in_matrix(map: list, item: str) -> tuple[int, int]:
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == item:
                    return (i, j)

    def player_movement(player_position: dict) -> list:
        MOVEMENT: dict = {
            "Arriba": ("W", [-1, 0]),
            "Abajo": ("S", [1, 0]),
            "Izquierda": ("A", [0, -1]),
            "Derecha": ("D", [0, 1])
        }

        available_moves = MOVEMENT.copy()

        if player_position["x"] == 0:
            del available_moves["Arriba"]
        elif player_position["x"] == 3:
            del available_moves["Abajo"]

        if player_position["y"] == 0:
            del available_moves["Izquierda"]
        elif player_position["y"] == 3:
            del available_moves["Derecha"]

        for move, value in list(available_moves.items()):
            print(f"{value[0]}: {move}")

        valid_moves = [value[0] for value in available_moves.values()]
        selected_move = ""

        while selected_move not in valid_moves:
            selected_move = input(
                "Hacia dónde quieres moverte? (Usa las teclas WASD): ").upper()
            if selected_move not in valid_moves:
                print("Movimiento inválido. Por favor, elige una dirección válida.")

        movement_vector = [
            value[1] for key, value in MOVEMENT.items() if value[0] == selected_move][0]
        return movement_vector

    def update_player_position(movement_vector, player_position, seen_map):
        player_position["x"] += movement_vector[0]
        player_position["y"] += movement_vector[1]

        seen_map[player_position["x"]][player_position["y"]] = 1

    def check_win(pos: dict, map: list) -> bool:
        win_coords = find_in_matrix(map, "🍭")
        player_coords = list(pos.values())

        if win_coords[0] == player_coords[0] and win_coords[1] == player_coords[1]:
            return True

    QUESTIONS: dict = {
        "What is the capital of France?": {
            "Paris": 1,
            "London": 0,
            "Berlin": 0,
            "Madrid": 0
        },
        "Who wrote the play 'Romeo and Juliet'?": {
            "William Shakespeare": 1,
            "Charles Dickens": 0,
            "Jane Austen": 0,
            "Leo Tolstoy": 0
        },
        "What is the chemical symbol for gold?": {
            "Au": 1,
            "Ag": 0,
            "Fe": 0,
            "Cu": 0
        },
        "What is the largest planet in our solar system?": {
            "Jupiter": 1,
            "Mars": 0,
            "Saturn": 0,
            "Venus": 0
        },
        "Who is the 44th President of the United States?": {
            "Barack Obama": 1,
            "George W. Bush": 0,
            "Bill Clinton": 0,
            "Donald Trump": 0
        }
    }

    player_position: list = False
    seen_map: list[list] = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    print_map(player_position)

    confirm: bool = True if input(
        "¿Quieres entrar? (s/n): ") == ("s" or "S") else False
    if confirm:
        door_position = find_in_matrix(GAME_MAP, "🚪")
        player_position = {"x": door_position[0], "y": door_position[1]}
        seen_map[door_position[0]][door_position[1]] = 1

        win_flag: bool = False

        while not win_flag:
            print_map(player_position)
            if GAME_MAP[player_position["x"]][player_position["y"]] == "👻":
                ask_question("ghost")
            else:
                ask_question()
            move = player_movement(player_position)
            update_player_position(move, player_position, seen_map)
            win_flag = check_win(player_position, GAME_MAP)

        print("Has encontrado los dulces! 🍭🍭🍭\n")
    else:
        print("Adios!")


init()
