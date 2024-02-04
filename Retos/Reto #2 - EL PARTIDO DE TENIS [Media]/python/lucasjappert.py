from enum import Enum

class Players(Enum):
    P1 = "P1"
    P2 = "P2"
class StateOptions(Enum):
    OptionLove = "Love"
    Option15  = 15
    Option30  = 30
    Option40  = 40
    OptionVentaja = "Ventaja"
    OptionWin = "Win"

inputs_for_test: list[list[Players]] = []

def _check_result(p1_state: StateOptions, p2_state: StateOptions):
    if p1_state == StateOptions.OptionWin:
        return print("Ha ganado el P1")
    if p2_state == StateOptions.OptionWin:
        return print("Ha ganado el P2")
    
    if p1_state == StateOptions.Option40 and p2_state == StateOptions.Option40:
        return print("Deuce")
    
    if p1_state == StateOptions.OptionVentaja:
        return print("Ventaja P1")
    
    if p2_state == StateOptions.OptionVentaja:
        return print("Ventaja P2")
    
    print(f"{p1_state.value} - {p2_state.value}")
    
def _get_next_state(current_player_state: StateOptions, enemy_player_state: StateOptions):
    result: StateOptions = None
    if current_player_state == StateOptions.OptionLove: result = StateOptions.Option15
    if current_player_state == StateOptions.Option15: result = StateOptions.Option30
    if current_player_state == StateOptions.Option30: result = StateOptions.Option40
    if current_player_state == StateOptions.Option40:
        aux = [StateOptions.Option40, StateOptions.OptionVentaja]
        if enemy_player_state in aux: result = StateOptions.OptionVentaja
        else: result = StateOptions.OptionWin
    if current_player_state == StateOptions.OptionVentaja: result = StateOptions.OptionWin

    # if result == StateOptions.OptionVentaja and enemy_player_state == StateOptions.OptionVentaja:
    #         p1_state = StateOptions.Option40
    #         p2_state = StateOptions.Option40

    return result

def _print_tenis_game(points_by_player: list[Players]):
    p1_state: str | int = StateOptions.OptionLove
    p2_state: str | int = StateOptions.OptionLove


    for point_win in points_by_player:
        # Seteo estados
        if point_win == Players.P1: 
            p1_state = _get_next_state(p1_state, p2_state)

        if point_win == Players.P2: 
            p2_state = _get_next_state(p2_state, p1_state)

        # Valido estados
        if p1_state == StateOptions.OptionVentaja and p2_state == StateOptions.OptionVentaja:
            p1_state = StateOptions.Option40
            p2_state = StateOptions.Option40

        _check_result(p1_state, p2_state)

        if p1_state == StateOptions.OptionWin or p2_state == StateOptions.OptionWin:
            break
        
    if StateOptions.OptionWin not in [p1_state, p2_state]:
        print("------- LOS DATOS DE ENTRADA NO LOGRAN FINALIZAR EL PARTIDO")

def _get_score(points: int):
    if points == 0: return "Love"
    if points == 1: return 15
    if points == 2: return 30
    if points == 3: return 40

def _check_result_1(p1_points: int, p2_points):
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
        
def _print_tenis_game_1(points_by_player: list[Players]):
    p1_points: int = 0
    p2_points: int = 0

    for point_win in points_by_player:
        if point_win == Players.P1:
            p1_points += 1
        if point_win == Players.P2:
            p2_points += 1

        if _check_result_1(p1_points, p2_points): return True

    print("------- LOS DATOS DE ENTRADA NO LOGRAN FINALIZAR EL PARTIDO")

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
    if _print_tenis_game_1(input) == False:
        print("------- LOS DATOS DE ENTRADA NO LOGRAN FINALIZAR EL PARTIDO")


