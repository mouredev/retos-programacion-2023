from typing import List


steps = ["Love", 15, 30, 40, "Duece", "Ventaja"]

def win_check(p1: int, p2: int) -> bool:
    if (p1 - p2) >= 2:
        print("Ha ganado el P1")
        return True
    if (p2 - p1) >= 2:
        print("Ha ganado el P2")
        return True
    return False


def tenis(sequence: List[str]):
    p1, p2 = 0, 0
    for step in sequence:
        if step.lower() not in ["p1", "p2"]:
            print("Movimiento invalido")
            continue
        if step.lower() == 'p1':
            p1 += 1
        else:
            p2 += 1
    
        if p1 == p2 == 3:
            print("Deuce")
            continue

        if (p1 > 3) or (p2 > 3):
            if win_check(p1, p2):
                break
            elif p1 > p2:
                print("Ventaja P1")
            else:
                print("Ventaja P2")
            continue

        print(f'{steps[p1]} - {steps[p2]}')


tenis(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1'])
