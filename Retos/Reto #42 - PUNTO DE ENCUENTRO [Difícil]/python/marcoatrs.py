def objects_collision(coors_a: tuple, coors_b: tuple, speed_a: tuple, speed_b: tuple) -> str:
    if coors_a == coors_b:
        return f"Se encuentra en {coors_a}"

    speed_x = speed_a[0] - speed_b[0]
    speed_y = speed_a[1] - speed_b[1]

    pos_x = coors_b[0] - coors_a[0]
    pos_y = coors_b[1] - coors_a[1]

    if (speed_x == 0) and (speed_y == 0):
        return "No se encuentran"

    x = pos_x / speed_x if speed_x != 0 else 0
    y = pos_y / speed_y if speed_y != 0 else 0

    if x != y:
        return "No se encuentran"

    res_x = coors_a[0] + speed_a[0] * x
    res_y = coors_a[1] + speed_a[1] * y

    return f"Se encuentran en X: {res_x} | Y: {res_y} con tiempo de {x}"


print(objects_collision((0, 0),  (0, 0), (5, -1), (4, 3)))
print(objects_collision((1, 1),  (1, 2), (1, 1), (1, 1)))
print(objects_collision((5, 5),  (10, 10), (1, 1), (-1, -1)))
