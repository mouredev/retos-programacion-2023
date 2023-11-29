import random

floor = ["_", "🌲", "🏁", "💥"]
cars = ["🚗", "🚙"]


def race(large: int):

    # Se crea una pista aleatoria para cada auto
    def create_path(large: int, player: int) -> list:

        # Se le añade la meta como primer elemento
        path = [floor[2]]
        trees = 0

        for i in range(1, large-1):
            if trees < 3:
                if random.randint(1, 8) == 2:
                    path.append(floor[1])
                    trees += 1
                    continue
            path.append(floor[0])

        if trees == 0:
            path[random.randint(1, large-1)] = floor[1]

        # Agregar un auto (player 0: auto rojo, player 1: auto verde)
        path.append(cars[player])

        return path

    # Obtener una lista de la carrera
    path1 = create_path(large, 0)
    path2 = create_path(large, 1)

    # Variables útiles
    position1 = large - 1
    position2 = large - 1
    last_piece1 = floor[0]
    last_piece2 = floor[0]
    count1 = 0
    count2 = 0
    turn1 = True
    turn2 = True

    # Convertir la lista en un string para mostrar en pantalla
    show_path1 = "".join(x for x in path1)
    show_path2 = "".join(x for x in path2)

    # Mostrar el inicio de la carrera
    print(show_path1)
    print(show_path2)

    # Iniciar la carrera
    while path1[0] != cars[0] and path2[0] != cars[1]:
        # Si ningún auto esta en la meta se mantiene el ciclo

        # Movimiento
        if count1 != 0:
            count1 -= 1
            move1 = 0
            path1[position1] = floor[1]
            turn1 = False
        else:
            move1 = random.randint(1, 3)

        if count2 != 0:
            count2 -= 1
            move2 = 0
            path2[position2] = floor[1]
            turn2 = False
        else:
            move2 = random.randint(1, 3)

        # Reemplazar la pieza anterior
        path1[position1] = last_piece1
        path2[position2] = last_piece2

        # Reemplazar la pieza actual
        position1 -= move1
        position2 -= move2
        if position1 < 0:
            position1 = 0
        if position2 < 0:
            position2 = 0

        last_piece1 = path1[position1]
        last_piece2 = path2[position2]

        # Revisar si ocurrió algún choque
        if last_piece1 == floor[1] and last_piece2 == floor[1] and turn1 == True and turn2 == True:
            path1[position1] = floor[3]
            path2[position2] = floor[3]
            count1 = 1
            count2 = 1
            turn1 = True
            turn2 = True

        elif last_piece1 == floor[1] and turn1 == True:
            path1[position1] = floor[3]
            path2[position2] = cars[1]
            count1 = 1
            turn1 = True

        elif last_piece2 == floor[1] and turn2 == True:
            path1[position1] = cars[0]
            path2[position2] = floor[3]
            count2 = 1
            turn2 = True

        else:
            path1[position1] = cars[0]
            path2[position2] = cars[1]
            turn1 = True
            turn2 = True

        # Actualizar la carrera
        show_path1 = "".join(x for x in path1)
        show_path2 = "".join(x for x in path2)

        print(show_path1)
        print(show_path2)

    if path1[0] == cars[0] and path2[0] == cars[1]:
        print("Empate")
    elif path1[0] == cars[0]:
        print("Gana el auto 1")
    else:
        print("Gana el auto 2")


race(30)
