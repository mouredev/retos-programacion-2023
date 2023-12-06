def get_score(score):
    scores = {0: "Love", 15: "15", 30: "30", 40: "40"}
    return scores.get(score, str(score))


def get_game_result(score_p1, score_p2):
    if score_p1 >= 40 and score_p2 >= 40:
        if score_p1 == score_p2:
            return "Deuce"
        elif score_p1 - score_p2 == 1:
            return "Ventaja P1"
        elif score_p2 - score_p1 == 1:
            return "Ventaja P2"
    return None


def tennis_game(sequence):
    score_p1 = 0
    score_p2 = 0

    for point in sequence:
        if point == "P1":
            score_p1 += 15
        elif point == "P2":
            score_p2 += 15

        game_result = get_game_result(score_p1, score_p2)
        if game_result:
            print(f"{get_score(score_p1)} - {get_score(score_p2)}")
            print(game_result)
            if game_result.startswith("Ventaja"):
                continue
            else:
                return f"Ha ganado el P1" if score_p1 > score_p2 else f"Ha ganado el P2"

        print(f"{get_score(score_p1)} - {get_score(score_p2)}")

    return f"Ha ganado el P1" if score_p1 > score_p2 else f"Ha ganado el P2"
