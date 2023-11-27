import random
import requests


class Rooms:
    EXIT = "🍭"
    GHOST = "👻"
    START = "🚪"
    ROOM = "🔳"


class Directions:
    NORTE = "norte"
    SUR = "sur"
    ESTE = "este"
    OESTE = "oeste"


PISOS_MANSION = 4
X_INICIO, Y_INICIO = [
    random.randint(0, PISOS_MANSION - 1),
    random.randint(0, PISOS_MANSION - 1),
]


def generarEnigma():
    reqUrl = "https://opentdb.com/api.php?amount=1&difficulty=easy&type=multiple"
    response = requests.get(reqUrl, timeout=5).json().get("results", [])[0]
    answers = response["incorrect_answers"]
    correct = response["correct_answer"]
    answers.append(correct)
    question = f"{response['question']}:\t{', '.join(answers)}"
    return {"pregunta": question, "respuesta": correct}


def generarMansion():
    mansion = [[Rooms.ROOM for _ in range(PISOS_MANSION)] for _ in range(PISOS_MANSION)]
    for _ in range(PISOS_MANSION):
        x, y = random.randint(0, PISOS_MANSION - 1), random.randint(
            0, PISOS_MANSION - 1
        )
        mansion[x][y] = Rooms.GHOST
    mansion[X_INICIO][Y_INICIO] = Rooms.START
    mansion[random.randint(0, PISOS_MANSION - 1)][
        random.randint(0, PISOS_MANSION - 1)
    ] = Rooms.EXIT
    for i in mansion:
        print(i)
    return mansion


def resolverEnigma(enigma):
    print(enigma["pregunta"])
    response = input("Tu respuesta: ").lower()
    if response == enigma["respuesta"].lower():
        print("Respuesta correcta.")
        return True
    else:
        print("Respuesta incorrecta.")
        return False


def juego():
    print("¡Encuentra la habitación de los dulces para salir!")
    x, y = X_INICIO, Y_INICIO
    mansion = generarMansion()
    while True:
        room = mansion[x][y]
        if room == Rooms.EXIT:
            print("¡Has encontrado la habitación de los dulces!")
            break

        if room == Rooms.GHOST:
            print("¡Te has encontrado con un fantasma! Debes responder 2 preguntas.")
            enigma = generarEnigma()
            enigmaG = generarEnigma()
            if not resolverEnigma(enigma) or not resolverEnigma(enigmaG):
                print("¡Has fallado!, el fantasma te atrapa.")
                break

        elif room == Rooms.ROOM:
            enigma = generarEnigma()
            while not resolverEnigma(enigma):
                enigma = generarEnigma()
            print("Puedes continuar con tu búsqueda.")

        validDirections = []
        if x > 0:
            validDirections.append(Directions.NORTE)
        if x < PISOS_MANSION - 1:
            validDirections.append(Directions.SUR)
        if y > 0:
            validDirections.append(Directions.OESTE)
        if y < PISOS_MANSION - 1:
            validDirections.append(Directions.ESTE)

        direction = input(
            f"¿A dónde quieres ir? {', '.join(validDirections)}: "
        ).lower()

        if direction in validDirections:
            if direction == Directions.NORTE:
                x -= 1
            elif direction == Directions.SUR:
                x += 1
            elif direction == Directions.ESTE:
                y += 1
            elif direction == Directions.OESTE:
                y -= 1
        else:
            print("Dirección no válida. Has vuelto a entrar en la room.")


if __name__ == "__main__":
    juego()
