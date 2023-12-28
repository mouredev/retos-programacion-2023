import random

# crear casa
def create_house() -> (list, list):

    house = [list(["⬜️"] * 4) for _ in range(4)]

    if random.choice([True, False]):
        # Columnas
        door = [random.randint(0, 3), random.choice([0, 3])]
    else:
        # Filas
        door = [random.choice([0, 3]), random.randint(0, 3)]

    house[door[0]][door[1]] = "🚪"

    # colocar caramelo
    def generate_candy(door: list) -> list:
        candy = [random.randint(0, 3), random.randint(0, 3)]
        if candy[0] == door[0] and candy[1] == door[1]:
            return generate_candy(door)
        return candy

    candy = generate_candy(door)

    house[candy[0]][candy[1]] = "🍭"

    for row in house:
        print("".join(map(str, row)))

    return house, door


# Mover
def move(position: list) -> list:

    row, col = position[0], position[1]

    movements = "N S E O "

    if row == 0: movements = movements.replace("N ", "")
    if row == 3: movements = movements.replace("S ", "")
    if col == 0: movements = movements.replace("O ", "")
    if col == 3: movements = movements.replace("E ", "")

    movement = input(f'¿Hacia donde te quieres desplazar [ {movements}]?: ').upper()

    if movement in movements:
        if movement == "N": position = [row - 1, col]
        elif movement == "S": position = [row + 1, col]
        elif movement == "E": position = [row, col + 1]
        elif movement == "O": position = [row, col - 1]

        return position

    else:
        print("Seleccione movimiento válido")
        return move(position)


# Crear acertijo
def riddle():
    
    riddles = [("2 x 2" , "4"), ("10 x 11", "110"), ("4 x 4", "16"), ("5 x 5", "25"),
    ("9 x 9", "81"), ("12 x 6", "36"), ("11 x 11", "121"), ("20 x 2", "40"), ("12 x 12", "144"),
    ("33 x 3", "99"), ("5 x 4", "20"), ("5 x 6", "30"), ("6 x 6", "36"), ("7 x 7", "49"),
    ("13 x 2", "26"), ("100 x 100", "10000"), ("42 x 3", "126"), ("36 x 3", "108"), 
    ("10 x 10", "100"), ("Ella no te...", "Ama")]

    current_riddle = riddles[random.randint(0, len(riddles) - 1)]

    while True:
        answer = input(f"{current_riddle[0]}: ")

        if answer.lower() == current_riddle[1].lower():
            print("Respuesta correcta")
            return
        else:
            print("Respuesta incorrecta") 


house, door = create_house()

position = door

print(position)

print("Bienvenidos al juego\nLlega al dulce!!")

while True:
    position = move(position)
    print(position)

    house_room = house[position[0]][position[1]]

    if house_room == "⬜️":
        print("Responde correctamente")
        riddle()

        ghost = random.randint(1, 10) == 1

        if ghost:
            print("👻 Trampa!! Para salir de esta habitación deberás responder otra pregunta más.")
            riddle()
    elif house_room == "🍭":
        print("Encontraste el dulce!!")
        break
