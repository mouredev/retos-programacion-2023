from typing import NamedTuple
import math

EPSILON = 10**-9


class Coordinates(NamedTuple):
    x: float
    y: float


class Velocity(Coordinates):
    pass


class Object(NamedTuple):
    start_point: Coordinates
    velocity: Velocity


class Objects(NamedTuple):
    object1: Object
    object2: Object


def calculate_diff_coordinates(obj1_coords: Coordinates, obj2_coords: Coordinates) -> Coordinates:
    """
    Calculates the difference between the coordinates of two objects.

    Args:
    - obj1_coords (Coordinates): Coordinates of the first object.
    - obj2_coords (Coordinates): Coordinates of the second object.

    Returns:
    - Coordinates: Difference in coordinates (obj2_coords - obj1_coords).
    """
    diff_x = obj2_coords.x - obj1_coords.x
    diff_y = obj2_coords.y - obj1_coords.y
    return Coordinates(x=diff_x, y=diff_y)


def calculate_diff_velocity(obj1_vel: Velocity, obj2_vel: Velocity) -> Velocity:
    """
    Calculates the difference between the velocities of two objects.

    Args:
    - obj1_vel (Velocity): Velocity of the first object.
    - obj2_vel (Velocity): Velocity of the second object.

    Returns:
    - Velocity: Difference in velocity (obj2_vel - obj1_vel).
    """
    diff_vel_x = obj2_vel.x - obj1_vel.x
    diff_vel_y = obj2_vel.y - obj1_vel.y
    return Velocity(x=diff_vel_x, y=diff_vel_y)


def calculate_time_to_intersection(diff_coordinates: Coordinates, diff_velocity: Velocity) -> float:
    """
    Calculates the time it takes for two objects to intersect.

    Args:
    - diff_coordinates (Coordinates): Difference in coordinates between two objects.
    - diff_velocity (Velocity): Difference in velocity between two objects.

    Returns:
    - float: Time to intersection.
    """
    time_to_intersection = math.sqrt(diff_coordinates.x**2 + diff_coordinates.y**2) / math.sqrt(diff_velocity.x**2 + diff_velocity.y**2)
    return time_to_intersection


def calculate_intersection_point(object1: Object, time_to_intersection: float) -> Coordinates:
    """
    Calculates the point where two objects intersect after a certain time.

    Args:
    - object1 (Object): First object information.
    - time_to_intersection (float): Time to intersection.

    Returns:
    - Coordinates: Intersection point.
    """
    intersection_x = object1.start_point.x + object1.velocity.x * time_to_intersection
    intersection_y = object1.start_point.y + object1.velocity.y * time_to_intersection
    return Coordinates(x=intersection_x, y=intersection_y)


def is_same_direction(diff_velocity: Velocity) -> bool:
    """
    Checks if two objects are moving in the same direction.

    Args:
    - diff_velocity (Velocity): Difference in velocity between two objects.

    Returns:
    - bool: True if moving in the same direction, False otherwise.
    """
    return diff_velocity.x == 0 and diff_velocity.y == 0


def calculate_intersection_point_in_motion(objects: Objects) -> None:
    """
    Calculates and prints the meeting point of two moving objects.

    Args:
    - objects (Objects): Information about the two objects.
    """
    diff_coordinates = calculate_diff_coordinates(objects.object1.start_point, objects.object2.start_point)
    diff_velocity = calculate_diff_velocity(objects.object1.velocity, objects.object2.velocity)

    if is_same_direction(diff_velocity):
        print("The objects or meeting points are parallel and will never meet.")
        return

    time_to_intersection = calculate_time_to_intersection(diff_coordinates, diff_velocity)
    intersection_point = calculate_intersection_point(objects.object1, time_to_intersection)
    intersection_x = intersection_point.x
    intersection_y = intersection_point.y

    print(f"The meeting point is ({intersection_x}, {intersection_y})")
    print(f"The time it will take them to meet is {time_to_intersection}")


if __name__ == "__main__":
    object1 = Object(start_point=Coordinates(x=2, y=2), velocity=Velocity(x=2, y=2))
    object2 = Object(start_point=Coordinates(x=2, y=2), velocity=Velocity(x=2, y=2))
    objects = Objects(object1=object1, object2=object2)

    calculate_intersection_point_in_motion(objects=objects)
