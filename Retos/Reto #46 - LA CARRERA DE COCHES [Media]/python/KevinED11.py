import random
from typing import Iterable, Never, Optional
from dataclasses import dataclass
import functools
import time


type StrList = list[str]


class OutOfRangeProbabilityException(Exception):
    pass


def raise_out_of_range_probability_exception(msg: str) -> Never:
    raise OutOfRangeProbabilityException(msg)


def generate_track(length: int) -> StrList:
    return ["_" for _ in range(length)]


def choice_random_position(track: StrList) -> int:
    return random.randint(0, len(track) - 1)


def choice_position_probabilistically(
    track: StrList, probability: int | float = 10
) -> Optional[int]:
    if 0 > probability > 100:
        raise_out_of_range_probability_exception(
            "Probability must be between 0 and 100"
        )

    if probability <= 1:
        probability = probability * 100

    minimum_probability = 0
    maximum_probability = 100
    if random.randint(minimum_probability, maximum_probability) <= probability:
        return choice_random_position(track=track)


@dataclass
class ChoicePositionConfig:
    track: StrList
    probability: int | float = 10
    quantity: int = 3


def choice_positions_probabilistically(config: ChoicePositionConfig) -> list[int]:
    positions = []
    counter = 0
    while len(positions) < config.quantity:
        position = choice_position_probabilistically(
            track=config.track, probability=config.probability
        )
        if position is not None and position not in positions:
            positions += [position]

        counter += 1

    if not positions:
        positions += [choice_random_position(track=config.track)]

    return positions


def insert_trees_into_track(config: ChoicePositionConfig) -> StrList:
    copy_track = [*config.track]

    positions = choice_positions_probabilistically(config=config)

    for position in positions:
        copy_track[position] = "X"

    return copy_track


def insert_car_into_track(track: StrList, symbol: str = "C") -> StrList:
    copy_track = [*track]
    copy_track += [symbol]

    return copy_track


def insert_finish_line_into_track(track: StrList, symbol: str = "F") -> StrList:
    copy_track = [*track]
    copy_track.insert(0, symbol)

    return copy_track


@dataclass
class FinalTrackConfig(ChoicePositionConfig):
    symbol_car: str = "C"
    finish_line: str = "F"


def generate_final_track(config: FinalTrackConfig) -> StrList:
    copy_track = [*config.track]

    track_with_trees = insert_trees_into_track(
        ChoicePositionConfig(
            track=copy_track, quantity=config.quantity, probability=config.probability
        )
    )

    track_with_trees_and_car = insert_car_into_track(
        track=track_with_trees, symbol=config.symbol_car
    )

    track_with_trees_and_car_with_finish_line = insert_finish_line_into_track(
        track=track_with_trees_and_car,
        symbol="F",
    )

    return track_with_trees_and_car_with_finish_line


def stop_game(seconds: int) -> None:
    time.sleep(seconds)


def main() -> None:
    car1: StrList
    car2: StrList
    track = generate_track(length=10)
    config = FinalTrackConfig(
        track=track, quantity=3, probability=100, symbol_car="C", finish_line="F"
    )
    print(generate_final_track(config=config))


if __name__ == "__main__":
    main()
