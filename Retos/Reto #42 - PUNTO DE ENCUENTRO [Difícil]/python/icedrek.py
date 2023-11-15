"""
 * Crea una función que calcule el punto de encuentro de dos objetos en movimiento
 * en dos dimensiones.
 * - Cada objeto está compuesto por una coordenada xy y una velocidad de desplazamiento
 *   (vector de desplazamiento) por unidad de tiempo (también en formato xy).
 * - La función recibirá las coordenadas de inicio de ambos objetos y sus velocidades.
 * - La función calculará y mostrará el punto en el que se encuentran y el tiempo que tardarn en lograrlo.
 * - La función debe tener en cuenta que los objetos pueden no llegar a encontrarse.   
 """


class Object:
    def __init__(self, position, move_vector) -> None:
        self.initial_position = position
        self.move_vector = move_vector

    def position_in_time(self, t):
        movement = [(t * _) for _ in self.move_vector]
        return [(v1 + v2) for v1, v2 in zip(self.initial_position, movement)]


def calculate_colision(ob1: Object, ob2: Object):
    (x1, y1) = ob1.initial_position
    (xv1, yv1) = ob1.move_vector

    (x2, y2) = ob2.initial_position
    (xv2, yv2) = ob2.move_vector

    tx = division(x1 - x2, xv2 - xv1)
    ty = division(y1 - y2, yv2 - yv1)

    colision = None
    t = None

    if tx == ty:
        t = tx
        colision = ob1.position_in_time(t)
    elif tx == None and ty != None:
        if ob1.position_in_time(ty) == ob2.position_in_time(ty):
            t = ty
            colision = ob1.position_in_time(t)
    elif tx != None and ty == None:
        if ob1.position_in_time(tx) == ob2.position_in_time(tx):
            t = tx
            colision = ob1.position_in_time(t)

    if colision == None:
        print("NO HAY COLISION")
    else:
        print(f"Colision en t={t} en posicion {colision}")


def division(x, y):
    try:
        result = x / y

    except ZeroDivisionError:
        result = None

    return result


if __name__ == "__main__":
    ob1 = Object((0, 0), (1, 1))  # posicion_inicial, vector_de_movimiento
    ob2 = Object((0, 3), (1, -1))

    calculate_colision(ob1, ob2)
