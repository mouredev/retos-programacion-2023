# Reto #42: Punto de encuentro
#### Dificultad: Difícil | Publicación: 23/10/23 | Corrección: 30/10/23

## Enunciado

#
# Crea una función que calcule el punto de encuentro de dos objetos en movimiento
# en dos dimensiones.
# - Cada objeto está compuesto por una coordenada xy y una velocidad de desplazamiento
#   (vector de desplazamiento) por unidad de tiempo (también en formato xy).
# - La función recibirá las coordenadas de inicio de ambos objetos y sus velocidades.
# - La función calculará y mostrará el punto en el que se encuentran y el tiempo que tardarn en lograrlo.
# - La función debe tener en cuenta que los objetos pueden no llegar a encontrarse.
#


class MovingObject:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def position_at_time(self, t):
        new_x = self.x + self.vx * t
        new_y = self.y + self.vy * t
        return new_x, new_y

    @staticmethod
    def find_intersection(obj1, obj2):
        x1, y1, vx1, vy1 = obj1.x, obj1.y, obj1.vx, obj1.vy
        x2, y2, vx2, vy2 = obj2.x, obj2.y, obj2.vx, obj2.vy

        delta_x = x2 - x1
        delta_y = y2 - y1
        delta_vx = vx2 - vx1
        delta_vy = vy2 - vy1

        if delta_vx * vy1 == delta_vy * vx1:
            return None  # Los objetos viajan en la misma dirección o a la misma velocidad, no se cruzan

        t = (delta_x * delta_vy - delta_y * delta_vx) / (
            vx1 * delta_vy - vy1 * delta_vx
        )

        if t < 0:
            return None

        x_intersection, y_intersection = obj1.position_at_time(t)
        
        return x_intersection, y_intersection, t


if __name__ == "__main__":
    object1 = MovingObject(0, 0, 2, 1)
    object2 = MovingObject(4, 2, 1, 1)
    result = MovingObject.find_intersection(object1, object2)

    if result is not None:
        x_intersection, y_intersection, time = result
        print(
            f"Los objetos se encuentran en ({x_intersection}, {y_intersection}) después de {time} unidades de tiempo."
        )
    else:
        print("Los objetos no se encuentran.")
