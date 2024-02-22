import random
import time
import os


def race(track_length: int):

    track1, track2 = create_tracks(track_length)

    print_race(track1, track2)

    position1, position2 = len(track1) - 1, len(track2) - 1
    crash1, crash2 = False, False

    while position1 > 0 and position2 > 0:

        time.sleep(0.5)

        track1[position1] = "_"
        track2[position2] = "_"

        position1 -= 0 if crash1 else random.randint(1, 3)
        position2 -= 0 if crash2 else random.randint(1, 3)

        crash1, crash2 = False, False

        position1 = 0 if position1 < 0 else position1
        position2 = 0 if position2 < 0 else position2

        if track1[position1] == "🌲":
            crash1 = True
        if track2[position2] == "🌲":
            crash2 = True

        track1[position1] = "💥" if crash1 else "🚙"
        track2[position2] = "💥" if crash2 else "🚗"

        print_race(track1, track2)

        check_race(position1, position2)


def create_tracks(track_length: int) -> (list, list):

    track = ["_"] * track_length

    def add_trees(track: list) -> list:
        trees = random.randint(1, 3)
        for _ in range(trees):
            position = random.randint(0, len(track) - 1)
            track[position] = "🌲"

        return track

    track1, track2 = add_trees(track.copy()), add_trees(track.copy())

    track1.insert(0, "🏁")
    track1.append("🚙")
    track2.insert(0, "🏁")
    track2.append("🚗")

    return (track1, track2)


def print_race(track1: list, track2: list):
    os.system("cls")
    # os.system("cls") Windows
    print("".join(track1))
    print("".join(track2))
    print("")


def check_race(position1: int, position2: int):
    if position1 == 0 and position2 == 0:
        print("Empate")
    elif position1 == 0:
        
        print("Ha ganado el coche 🚙")
    elif position2 == 0:
        print("Ha ganado el coche 🚗")


race(20)
