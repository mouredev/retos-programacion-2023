scores = ["Love", " 15", "30", "40"]

def finalMatch(List):
    p1 = 0
    p2 = 0
    
    for p in List:
        if p == "P1": p1 += 1
        elif p == "P2": p2 += 1

        if p1 == 3 and p2 == 3: print("Deuce")
        
        elif p1 >= 4 or p2 >= 4:
            diff = p1 - p2
            if diff == 0: print("Deuce")
            elif diff == 1: print("Ventaja P1")
            elif diff == -1: print("Ventaja P2")
            elif diff >= 2: print("Ha ganado el P1")
            
            else: print("Ha ganado P2")

        else: print(f"{scores[p1]} - {scores[p2]}")

finalMatch(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"])
