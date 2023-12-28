playerScores = {'p1': 0, 'p2': 0}
scoreScale = ["Love","15","30","40"]

def gameScore(points):
    for point in points:
        playerScores[point.lower()]+= 1
        if playerScores["p1"] == playerScores["p2"] and playerScores["p1"] > 0:
            print("Deuce")
        elif playerScores["p1"] > 3 or playerScores["p2"] > 3:
            
            if playerScores["p1"] == playerScores["p2"] - 2:
                print("Ha ganado el P2")
                return()     
            elif playerScores["p2"] == playerScores["p1"] - 2:
                print("Ha ganado el P1")
                return()
            elif playerScores["p1"] == playerScores["p2"] - 1:
                print("Ventaja P2")
                continue  
            elif playerScores["p2"] == playerScores["p1"] - 1:
                print("Ventaja P1")
                continue
        else:
            print(f'{scoreScale[playerScores["p1"]]} - {scoreScale[playerScores["p2"]]} ')


gameScore(("P1", "P1", "P2", "P2", "P1", "P2", "P2", "P2"))