import time
import random


FINISH = "🏁"
ROAD = "_"
TREE = "🌲"
BLUE_CAR = "🚙"
RED_CAR = "🚗"
CRASH = "💥"
MAX_TRACK_LENGTH = 25


def random_tree_positions(track_length: int) -> tuple[int, ...]:
    """
    Produce a set of tree positions, at random. This set will be suitable
    for the 'tree_positions' argument of a Lane object.

    Args:
        track_length (int): length of the Lane where the trees will be placed.

    Return:
        A tuple of 1 to 3 integers, denoting the position of the trees.
    """
    n_trees = random.randrange(1, 3)

    if n_trees > track_length:
        n_trees = track_length

    positions = []
    available_positions = list(range(1, track_length+1))
    for _ in range(n_trees):
        pos = random.choice(available_positions)
        positions.append(pos)
        available_positions.remove(pos)

    return tuple(positions)


class Lane:
    """
    Class with info and methods for a single lane (the circuit for one car).
    """

    def __init__(self, car: str, length: int, tree_positions: tuple[int, ...]):
        self.car = car
        self.length = length
        self.tree_positions = tree_positions
        self.car_position = 0
        self.lane = []
        self.crashed = False

        self.refresh()

    def refresh(self) -> None:
        self.lane = [FINISH]
        self.lane.extend([ROAD]*self.length)
        for tree_pos in self.tree_positions:
            self.lane[self.length-tree_pos+1] = TREE

        if self.car_position == 0:
            self.lane.append(self.car)
            return

        token = self.car
        if self.car_position in self.tree_positions:
            token = CRASH
            self.crashed = True

        self.lane[self.length-self.car_position+1] = token

    def advance(self) -> None:
        """
        Make the car advance 1 to 3 random tiles.
        If the car hit a tree in the previous round, skip this round.
        """
        if self.crashed:
            self.crashed = False
            return

        self.car_position += random.randrange(1, 3)
        if self.car_position > self.length:
            self.car_position = self.length+1  # finish line

        self.refresh()

    def __str__(self) -> str:
        return "".join(self.lane)


class Race:
    """
    Class with info and methods for a whole race (a collection of Lanes).
    """

    def __init__(self, lanes: tuple[Lane, ...]):
        self.lanes = lanes

    def advance(self) -> None:
        for lane in self.lanes:
            lane.advance()

    @property
    def finished(self) -> bool:
        """
        Return whether the Race is finished or not. This happens when at least
        one of the cars has arrived at the last road tile in its Lane.
        """
        for lane in self.lanes:
            if lane.car_position == lane.length+1:
                return True

        return False

    def print_who_won(self) -> None:
        """
        Print who won, of if there was a tie.
        """
        if not self.finished:
            print("The race has not finished yet!")
            return

        winners = []
        for lane in self.lanes:
            if lane.car_position > lane.length:
                winners.append(lane.car)

        if len(winners) == 1:
            print(f"{winners[0]} won!")
        else:
            print(f"The following cars were tied for the win: {', '.join(winners)}")

    def __str__(self) -> str:
        return "\n".join([str(e) for e in self.lanes])


def main():
    length = random.randrange(1, MAX_TRACK_LENGTH)

    blue_lane = Lane(car=BLUE_CAR, length=length, tree_positions=random_tree_positions(length))
    red_lane = Lane(car=RED_CAR, length=length, tree_positions=random_tree_positions(length))
    race = Race(lanes=(blue_lane, red_lane))

    print("Initial:")
    print(race)
    time.sleep(1)

    turn = 1
    while not race.finished:
        print(f"Turn {turn}:")
        race.advance()
        print(race)

        turn += 1
        time.sleep(1)

    race.print_who_won()


if __name__ == "__main__":
    main()
