from random import randint, choice
from typing import List, Dict, Tuple


def init() -> None:
    maps: Dict[int, List[List[str]]] = {
        1: [
            ["🚪", "⬜️", "⬜️", "⬜️"],
            ["⬜️", "👻", "⬜️", "⬜️"],
            ["⬜️", "⬜️", "⬜️", "👻"],
            ["⬜️", "⬜️", "🍭", "⬜️"],
        ],
        2: [
            ["🚪", "⬜️", "⬜️", "⬜️"],
            ["👻", "⬜️", "⬜️", "⬜️"],
            ["⬜️", "⬜️", "⬜️", "🍭"],
            ["⬜️", "⬜️", "👻", "⬜️"],
        ],
        3: [
            ["⬜️", "⬜️", "⬜️", "🍭"],
            ["⬜️", "👻", "⬜️", "⬜️"],
            ["⬜️", "⬜️", "👻", "⬜️"],
            ["🚪", "⬜️", "⬜️", "⬜️"],
        ],
        4: [
            ["⬜️", "👻", "⬜️", "⬜️"],
            ["🍭", "⬜️", "⬜️", "⬜️"],
            ["⬜️", "⬜️", "👻", "⬜️"],
            ["⬜️", "⬜️", "🚪", "⬜️"],
        ],
        5: [
            ["⬜️", "⬜️", "👻", "⬜️"],
            ["👻", "⬜️", "⬜️", "⬜️"],
            ["⬜️", "⬜️", "🍭", "⬜️"],
            ["⬜️", "⬜️", "🚪", "⬜️"],
        ],
        6: [
            ["⬜️", "⬜️", "👻", "🍭"],
            ["⬜️", "⬜️", "⬜️", "⬜️"],
            ["🚪", "⬜️", "⬜️", "⬜️"],
            ["⬜️", "⬜️", "⬜️", "👻"],
        ],
        7: [
            ["⬜️", "⬜️", "👻", "⬜️"],
            ["⬜️", "⬜️", "⬜️", "🍭"],
            ["🚪", "⬜️", "⬜️", "⬜️"],
            ["⬜️", "⬜️", "⬜️", "👻"],
        ],
        8: [
            ["⬜️", "⬜️", "👻", "⬜️"],
            ["🍭", "⬜️", "⬜️", "⬜️"],
            ["⬜️", "⬜️", "⬜️", "🚪"],
            ["⬜️", "⬜️", "👻", "⬜️"],
        ],
        9: [
            ["⬜️", "⬜️", "🚪", "⬜️"],
            ["👻", "⬜️", "⬜️", "⬜️"],
            ["⬜️", "⬜️", "⬜️", "👻"],
            ["⬜️", "⬜️", "⬜️", "🍭"],
        ],
        10: [
            ["⬜️", "👻", "⬜️", "⬜️"],
            ["⬜️", "⬜️", "⬜️", "🚪"],
            ["👻", "⬜️", "⬜️", "⬜️"],
            ["⬜️", "⬜️", "⬜️", "🍭"],
        ],
    }

    print(
        "\nBienvenido a la Mansión Encantada!\n"
        + "Para salir deberás responder preguntas en cada habitación.\n"
        + "Al resolver correctamente un enigma, podrás desplazarte a la\n"
        + "siguiente habitación.\n"
        + "La partida acabará cuando llegues a la sala de los dulces.\n"
    )

    game_map: List[List[str]] = maps[randint(1, len(maps))]
    main(game_map)


def main(game_map: List[List[str]]) -> None:
    def print_map(player_position: Dict[str, int]) -> None:
        display_map: List[List[str]] = [
            ["🚪" if game_map[i][j] == "🚪" else "⬜️" for j in range(map_size)]
            for i in range(map_size)
        ]

        for i, row in enumerate(display_map):
            for j, _ in enumerate(row):
                if seen_map[i][j] == 0:
                    if game_map[i][j] == "":
                        display_map[i][j] = "⬜️"
                elif player_position and (i, j) == tuple(player_position.values()):
                    display_map[i][j] = "👤"
                elif game_map[i][j] == "👻":
                    display_map[i][j] = "👻"

        for row in display_map:
            print("".join(map(str, row)))
        print("")

    def ask_question() -> None:
        question, choices = choice(list(QUESTIONS.items()))

        print(f"ENIGMA! {question}")
        for index, answer in enumerate(choices):
            print(f"\t{index + 1}: {answer}")

        correct_answer_index = list(choices.values()).index(1)
        user_answer_index = int(input("Respuesta: ")) - 1

        if user_answer_index != correct_answer_index:
            print("Incorrecto!")
            ask_question()
        else:
            print("Correcto!")
            if game_map[player_position["x"]][player_position["y"]] == "👻":
                print("Oh no! Un fantasma te ha atrapado!")
                print(
                    "Debes responder otra pregunta para poder salir de la habitación."
                )
                ask_question()

    def find_item_in_matrix(
        matrix: List[List[str]], target_item: str
    ) -> Tuple[int, int]:
        for i, row in enumerate(matrix):
            for j, item in enumerate(row):
                if item == target_item:
                    return i, j

    def get_valid_player_moves(player_position: Dict[str, int]) -> List[str]:
        movement_options: Dict[str, Tuple[int, int]] = {
            "W": (-1, 0),
            "S": (1, 0),
            "A": (0, -1),
            "D": (0, 1),
        }

        valid_moves: List[str] = []
        for move, vector in movement_options.items():
            new_position: Dict[str, int] = {
                "x": player_position["x"] + vector[0],
                "y": player_position["y"] + vector[1],
            }
            if 0 <= new_position["x"] < map_size and 0 <= new_position["y"] < map_size:
                valid_moves.append(move)

        chosen_move: str = ""
        while chosen_move not in valid_moves:
            chosen_move = input(
                "Hacia dónde quieres moverte? (Usa las teclas WASD): "
            ).upper()
            if chosen_move not in valid_moves:
                print("Movimiento inválido. Por favor, elige una dirección válida.")

        movement_vector: Tuple[int, int] = movement_options[chosen_move]
        return movement_vector

    def update_player_position(
        movement_vector: Tuple[int, int],
        player_position: Dict[str, int],
        seen_map: List[List[int]],
    ) -> None:
        player_position["x"] += movement_vector[0]
        player_position["y"] += movement_vector[1]

        seen_map[player_position["x"]][player_position["y"]] = 1

    def check_win(pos: Dict[str, int], map: List[List[str]]) -> bool:
        win_coords: Tuple[int, int] = find_item_in_matrix(map, "🍭")
        player_coords: List[int] = list(pos.values())

        if win_coords == player_coords:
            return True

    QUESTIONS: Dict[str, Dict[str, int]] = {
        "What is the capital of France?": {
            "Paris": 1,
            "London": 0,
            "Berlin": 0,
            "Madrid": 0,
        },
        "Who wrote the play 'Romeo and Juliet'?": {
            "William Shakespeare": 1,
            "Charles Dickens": 0,
            "Jane Austen": 0,
            "Leo Tolstoy": 0,
        },
        "What is the chemical symbol for gold?": {"Au": 1, "Ag": 0, "Fe": 0, "Cu": 0},
        "What is the largest planet in our solar system?": {
            "Jupiter": 1,
            "Mars": 0,
            "Saturn": 0,
            "Venus": 0,
        },
        "Who is the 44th President of the United States?": {
            "Barack Obama": 1,
            "George W. Bush": 0,
            "Bill Clinton": 0,
            "Donald Trump": 0,
        },
    }

    map_size: int = len(game_map)
    player_position: Dict[str, int] = {}
    seen_map: List[List[int]] = [[0] * map_size for _ in range(map_size)]

    print_map(player_position)

    confirm: bool = input("¿Quieres entrar? (s/n): ").lower() == "s"
    if confirm:
        door_position: Tuple[int, int] = find_item_in_matrix(game_map, "🚪")
        player_position = {"x": door_position[0], "y": door_position[1]}
        seen_map[door_position[0]][door_position[1]] = 1

        win_flag: bool = False

        while not win_flag:
            print_map(player_position)
            ask_question()
            move: Tuple[int, int] = get_valid_player_moves(player_position)
            update_player_position(move, player_position, seen_map)
            win_flag = check_win(player_position, game_map)

        print("Has encontrado los dulces! 🍭🍭🍭\n")
    else:
        print("Adios!")


init()
