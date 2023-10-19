from random import randint, choice


def init():
    maps = {
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

    game_map = maps[randint(1, len(maps))]
    main(game_map)


def main(game_map: list[list]):
    def print_map(player_position):
        display_map = [
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

    def ask_question():
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
        matrix: list[list[str]], target_item: str
    ) -> tuple[int, int]:
        for i, row in enumerate(matrix):
            for j, item in enumerate(row):
                if item == target_item:
                    return i, j

    def get_valid_player_moves(player_position: dict) -> list:
        movement_options = {
            "W": (-1, 0),
            "S": (1, 0),
            "A": (0, -1),
            "D": (0, 1),
        }

        valid_moves = []
        for move, vector in movement_options.items():
            new_position = {
                "x": player_position["x"] + vector[0],
                "y": player_position["y"] + vector[1],
            }
            if 0 <= new_position["x"] < map_size and 0 <= new_position["y"] < map_size:
                valid_moves.append(move)

        chosen_move = ""
        while chosen_move not in valid_moves:
            chosen_move = input(
                "Hacia dónde quieres moverte? (Usa las teclas WASD): "
            ).upper()
            if chosen_move not in valid_moves:
                print("Movimiento inválido. Por favor, elige una dirección válida.")

        movement_vector = movement_options[chosen_move]
        return movement_vector

    def update_player_position(movement_vector, player_position, seen_map):
        player_position["x"] += movement_vector[0]
        player_position["y"] += movement_vector[1]

        seen_map[player_position["x"]][player_position["y"]] = 1

    def check_win(pos: dict, map: list) -> bool:
        win_coords = find_item_in_matrix(map, "🍭")
        player_coords = list(pos.values())

        if win_coords == player_coords:
            return True

    QUESTIONS = {
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

    map_size = len(game_map)
    player_position = None
    seen_map = [[0] * map_size for _ in range(map_size)]

    print_map(player_position)

    confirm = input("¿Quieres entrar? (s/n): ").lower() == "s"
    if confirm:
        door_position = find_item_in_matrix(game_map, "🚪")
        player_position = {"x": door_position[0], "y": door_position[1]}
        seen_map[door_position[0]][door_position[1]] = 1

        win_flag = False

        while not win_flag:
            print_map(player_position)
            if game_map[player_position["x"]][player_position["y"]] == "👻":
                ask_question()
            else:
                ask_question()
            move = get_valid_player_moves(player_position)
            update_player_position(move, player_position, seen_map)
            win_flag = check_win(player_position, game_map)

        print("Has encontrado los dulces! 🍭🍭🍭\n")
    else:
        print("Adios!")


init()
