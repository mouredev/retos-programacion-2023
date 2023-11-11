"""
Comentarios:

- El enunciado no menciona que los objetos tengan tamaño. Si no lo tienen,
  la probabilidad de cruzarse es cero, excepto que sus vectores de velocidad
  sean colineares, y su velocidad relativa sea negativa. Voy a asumir que
  los puntos tienen un tamaño finito, definido como el resto de variables.

Desarrollo matemático:

Definamos las posiciones los objetos en un momento t como:

 p1(t) = (x1(t), y1(t))
 p2(t) = (x2(t), y2(t))

 Nos puede resultar útil definir:

 dx(t) = x2(t) - x1(t)
       = x2(0) + v2x * t - (x1(0) + v1x) * t
       = x2(0) - x1(0) + (v2x - v1x) * t
       = dx(0) + dvx * t
 dy(t) = y2(t) - y1(t)
       = dy(0) + dvy * t

La distancia entre ambos objetos en un instante cualquiera será:

D(t) = sqrt((x2(t)-x1(t))**2 + (y2(t)-y1(t))**2)

Encontrar el mínimo de D(t) equivaldrá a encontrar el mínimo de D(t)**2 (siendo D
siempre positivo), y es más fácil de calcular:

D(t)**2 = (x2(t)-x1(t))**2 + (y2(t)-y1(t))**2
        = dx(t)**2 + dy(t)**2

El mínimo de esa función (respecto al tiempo) se hallará igualando su derivada
(respecto al tiempo) a cero:

[D(t)**2]' =  2 * dx(t) * [dx(t)]' + 2 * dy(t) * [dy(t)]'
         0 = dx(t) * dx(t)' + dy(t) * dy(t)'

Las derivadas de dx(t) y dy(t), usando las ecuaciones del segundo bloque arriba:

dx(t)' = [dx(0) + dvx * t]'
       = dvx
dy(t)' = dvy

Por tanto:
0 = dx(t) * dvx + dy(t) * dvy
  = (dx(0) + dvx * t) * dvx + (dy(0) + dvy * t) * dvy
  = t * (dvx**2 + dvy**2) + dx(0) * dvx + dy(0) * dvy

Y finalmente:

t = (-dx(0) * dvx - dy(0) * dvy) / (dvx**2 + dvy**2)
"""
import math
from dataclasses import dataclass


EPSILON = 10**-9


@dataclass
class Position:
    x: float
    y: float

    def distance_to(self, other: 'Position') -> float:
        dx = other.x - self.x
        dy = other.y - self.y

        return math.sqrt(dx**2 + dy**2)


@dataclass
class Velocity:
    x: float
    y: float


@dataclass
class MovingObject:
    radius: float
    position: Position
    velocity: Velocity

    def position_after_time(self, t: float) -> Position:
        x = self.position.x + t * self.velocity.x
        y = self.position.y + t * self.velocity.y

        return Position(x=x, y=y)


@dataclass
class Result:
    time: float
    distance: float
    position1: Position
    position2: Position
    we_have_collision: bool = False


def calculate_closest_time(object1: MovingObject, object2: MovingObject) -> float:
    """
    Given two objects moving in a 2D plane, say when they will be closest to each other.
    See mathematical procedure at the top of this file for an explanation.

    Args:
        object1 (MovingObject): first moving object.
        object2 (MovingObject): second moving object.

    Return:
        Time, as a float.
    """
    dx0 = object2.position.x - object1.position.x
    dvx = object2.velocity.x - object1.velocity.x
    dy0 = object2.position.y - object1.position.y
    dvy = object2.velocity.y - object1.velocity.y

    return (-dx0 * dvx - dy0 * dvy)/(dvx**2 + dvy**2)


def calculate_collision(object1: MovingObject, object2: MovingObject) -> Result:
    """
    Given two objects moving in a 2D plane, say if, when and where
    they will meet.
    The objects are considered to meet if their closest approach is
    closer than the sum of their radii.

    Args:
        object1 (MovingObject): first moving object.
        object2 (MovingObject): second moving object.

    Return:
        A Result object, with all the data we want.
    """
    t = calculate_closest_time(object1, object2)

    # Closest distance:
    p1 = object1.position_after_time(t)
    p2 = object2.position_after_time(t)

    d = p1.distance_to(p2)

    we_have_collision = d <= (object1.radius + object2.radius)
    return Result(time=t, distance=d, position1=p1, position2=p2, we_have_collision=we_have_collision)


if __name__ == "__main__":
    # Example:
    print("Example:")
    o1 = MovingObject(radius=0.1, position=Position(0, 0), velocity=Velocity(0, 0))
    o2 = MovingObject(radius=0.1, position=Position(1, 0), velocity=Velocity(-1, 0))
    r = calculate_collision(o1, o2)
    print(o1)
    print(o2)
    print(r)

    # Test #1:
    assert r.we_have_collision is True
    assert abs(r.time - 1.0) < EPSILON
    print("\nTest #1 - pass")

    # Test #2:
    o1.velocity.y = 0.25
    o2.velocity = Velocity(-0.25, 0.25)
    r = calculate_collision(o1, o2)
    assert r.we_have_collision is True
    assert abs(r.time - 4.0) < EPSILON
    print("Test #2 - pass")

    # Test #3:
    o1.velocity.y = 0.25
    o2.velocity = Velocity(-0.125, 0.125)
    r = calculate_collision(o1, o2)
    assert r.we_have_collision is False
    assert abs(r.time - 4.0) < EPSILON
    assert abs(r.distance - math.sqrt(0.5)) < EPSILON
    print("Test #3 - pass")

    # Test #4:
    o1.velocity = Velocity(0, 1)
    o2.velocity = Velocity(0, -1)
    r = calculate_collision(o1, o2)
    assert r.we_have_collision is False
    assert abs(r.time) < EPSILON
    assert abs(r.distance - 1.0) < EPSILON
    print("Test #4 - pass")
