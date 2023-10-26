from typing import NamedTuple, Protocol
import math


type Number = float | int


class Coordinates(NamedTuple):
    x: Number
    y: Number


class Velocity(Coordinates):
    pass


class Object(NamedTuple):
    start_point: Coordinates
    velocity: Velocity


class Objects(NamedTuple):
    object1: Object
    object2: Object


def calculate_diff_coordinates(
    obj1_coords: Coordinates, obj2_coords: Coordinates
) -> Coordinates:
    diff_x = obj2_coords.x - obj1_coords.x
    diff_y = obj2_coords.y - obj1_coords.y

    return Coordinates(x=diff_x, y=diff_y)


def calculate_diff_velocity(obj1_vel: Velocity, obj2_vel: Velocity) -> Velocity:
    diff_vel_x = obj2_vel.x - obj1_vel.x
    diff_vel_y = obj2_vel.y - obj1_vel.y

    return Velocity(x=diff_vel_x, y=diff_vel_y)


def calculate_time_to_intersection(
    diff_coordinates: Coordinates, diff_velocity: Velocity
) -> float:
    time_to_intersection = math.sqrt(
        diff_coordinates.x**2 + diff_coordinates.y**2
    ) / math.sqrt(diff_velocity.x**2 + diff_velocity.y**2)

    return time_to_intersection


def calculate_intersection_point(
    object1: Object, time_to_intersection: float
) -> Coordinates:
    intersection_x = object1.start_point.x + object1.velocity.x * time_to_intersection
    intersection_y = object1.start_point.y + object1.velocity.y * time_to_intersection

    return Coordinates(x=intersection_x, y=intersection_y)


def is_same_direction(diff_velocity: Velocity) -> bool:
    return diff_velocity.x == 0 and diff_velocity.y == 0


def calculate_intersection_point_in_motion(objects: Objects) -> None:
    diff_coordinates: Coordinates = calculate_diff_coordinates(
        objects.object1.start_point, objects.object2.start_point
    )
    diff_velocity: Velocity = calculate_diff_velocity(
        objects.object1.velocity, objects.object2.velocity
    )

    if is_same_direction(diff_velocity):
        print("Los objetos o puntos de encuentro son paralelos y nunca se encuentran.")
        return

    time_to_intersection = calculate_time_to_intersection(
        diff_coordinates, diff_velocity
    )
    intersection_point = calculate_intersection_point(
        objects.object1, time_to_intersection
    )

    print(f"El punto de encuentro es ({intersection_point.x}, {intersection_point.y})")
    print(f"El tiempo que les tomará encontrarse es {time_to_intersection}")


class MotionCalculatorFn(Protocol):
    def __call__(self, objects: Objects) -> None:
        ...


def execute(motion_calculator: MotionCalculatorFn, objects: Objects) -> None:
    motion_calculator(objects=objects)


if __name__ == "__main__":
    object1 = Object(start_point=Coordinates(x=2, y=2), velocity=Velocity(x=2, y=2))
    object2 = Object(start_point=Coordinates(x=2, y=2), velocity=Velocity(x=2, y=2))
    objects = Objects(object1=object1, object2=object2)

    execute(motion_calculator=calculate_intersection_point_in_motion, objects=objects)
