from enum import Enum

class Players(Enum):
    P1 = "P1"
    P2 = "P2"

def _get_score(points: int):
    if points == 0: return "Love"
    if points == 1: return 15
    if points == 2: return 30
    if points == 3: return 40

def _check_result(p1_points: int, p2_points):
    if p1_points == 3 == p2_points:
        print("Deuce")
        return False
    
    if p1_points >= 4 or p2_points >= 4:
        if p1_points - p2_points > 1:
            print("Ha ganado el P1")
            return True
        if p2_points - p1_points > 1:
            print("Ha ganado el P2")
            return True
        if p1_points > p2_points:
            print("Ventaja P1")
            return False
        if p2_points > p1_points:
            print("Ventaja P2")
            return False
        print("Deuce")
        return False
    
    print(f"{_get_score(p1_points)} - {_get_score(p2_points)}")
    return False
        
def _print_tenis_game(points_by_player: list[Players]):
    p1_points: int = 0
    p2_points: int = 0

    for point_win in points_by_player:
        if point_win == Players.P1:
            p1_points += 1
        if point_win == Players.P2:
            p2_points += 1

        if _check_result(p1_points, p2_points): return True

    print("------- LOS DATOS DE ENTRADA NO LOGRAN FINALIZAR EL PARTIDO")

inputs_for_test: list[list[Players]] = []
def _set_inputs_for_test():
    inputs_for_test.append([Players.P1, Players.P1, Players.P2, Players.P1, Players.P1])
    inputs_for_test.append([Players.P1, Players.P1, Players.P2, Players.P2, Players.P1, Players.P2, Players.P1, Players.P1])
    inputs_for_test.append([Players.P1, Players.P1, Players.P1, Players.P1, Players.P1, Players.P1, Players.P1, Players.P1])
    inputs_for_test.append([Players.P2, Players.P2, Players.P2, Players.P2, Players.P2, Players.P2, Players.P2])
    inputs_for_test.append([Players.P1, Players.P1, Players.P1, Players.P2, Players.P1, Players.P1, Players.P1, Players.P1])
    inputs_for_test.append([Players.P1, Players.P1, Players.P1, Players.P2, Players.P2, Players.P2, Players.P2, Players.P2])
    inputs_for_test.append([Players.P1, Players.P1, Players.P1, Players.P2, Players.P2, Players.P2, Players.P2, Players.P1, Players.P2, Players.P2])
    inputs_for_test.append([Players.P1, Players.P1, Players.P1, Players.P2, Players.P2, Players.P2, Players.P2, Players.P1, Players.P2, Players.P1, Players.P1, Players.P1])
    inputs_for_test.append([Players.P1])
    inputs_for_test.append([Players.P1, Players.P1, Players.P2])
    inputs_for_test.append([Players.P1, Players.P1, Players.P1, Players.P2, Players.P2, Players.P2, Players.P2, Players.P1, Players.P2, Players.P1, Players.P1])

_set_inputs_for_test()

for input in inputs_for_test:
    inputs = [player.value for player in input]
    print(f"######## COMENZANDO TEST CON ESTOS INPUTS: {inputs}")
    if _print_tenis_game(input) == False:
        print("------- LOS DATOS DE ENTRADA NO LOGRAN FINALIZAR EL PARTIDO")


