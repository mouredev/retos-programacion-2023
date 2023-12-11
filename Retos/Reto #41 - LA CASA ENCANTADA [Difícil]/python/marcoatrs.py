import random


def generate_pos(a: int, b: int) -> tuple[int, int]:
    return (random.randint(a, b), random.randint(a, b))

def generate_house() -> list[list[str]]:
    house = [["⬜️" for _ in range(4)] for _ in range(4)]
    house[0][0] = "🚪"
    occup_roms = [(0, 0)]
    exit_pos = (0, 0)
    while exit_pos in occup_roms:
        exit_pos = generate_pos(1, 3)
    occup_roms.append(exit_pos)
    house[exit_pos[0]][exit_pos[1]] = "🍭"
    return house


def draw_house(house: list):
    for row in house:
        print(f'{"".join(row)}')


def get_valid_pos(pos: list[int, int]) -> list[str]:
    valid_pos = []
    if pos[0] > 0:
        valid_pos.append("norte")
    if pos[0] < 3:
        valid_pos.append("sur")
    if pos[1] < 3:
        valid_pos.append("este")
    if pos[1] > 0:
        valid_pos.append("oeste")
    return valid_pos


def play_game():
    house = generate_house()
    print("Sal de la mansión pero cuidado con las fantasmas")
    pos = [0, 0]
    win = False
    draw_house(house)
    while not win:
        print(f"Estas en {pos}\n")
        valid_pos = get_valid_pos(pos)
        move = input(f"¿A donde te quieres mover? ({'/'.join(valid_pos)}) ").lower()
        if move not in valid_pos:
            continue
        if move == "norte":
            pos[0] = max(0, pos[0] - 1)
        elif move == "sur":
            pos[0] = min(3, pos[0] + 1)
        elif move == "este":
            pos[1] = min(3, pos[1] + 1)
        else:
            pos[1] = max(0, pos[1] - 1)
        if house[pos[0]][pos[1]] == "🍭":
            print("Encontraste los dulces 🍭🍭🍭, ganaste :)")
            win = True
            continue
        questions = 1
        if random.random() <= 0.1:
            print("Encontraste un fantasma, contesta 2 preguntas para pasar 👻")
            house[pos[0]][pos[1]] = "👻"
            draw_house(house)
            questions += 1
        while questions > 0:
            question = generate_question()
            answer = input(f"{question[0]}: ").lower()
            if answer ==  question[1]:
                print("Correcto")
                questions -= 1
            else:
                print("Fallaste, intenta de nuevo 👻")


def generate_question() -> str:
    questions = [
        ("¿Cuantas patas tiene una araña?", "8"),
        ("¿Que lenguage de programacion tiene nombre de serpiente?", "python"),
        ("¿Cuantos lados tiene un rombo", "4"),
        ("¿Cual es el planeta rojo", "marte"),
        ("¿Como esta compuesta es agua?", "h2o"),
        ("¿Cual es el planeta mas cercano al Sol?", "mercurio"),
        ("¿En qué disciplina deportiva juega Leo Messi?", "futbol"),
        ("¿En qué país vivieron los samuráis?", "japon"),
        ("El sol es una estrella. ¿Verdadero o falso?", "verdadero"),
        ("¿Cuantas vocales tiene el abcedario?", "5")
    ]
    return random.choice(questions)


if __name__ == "__main__":
    play_game()
