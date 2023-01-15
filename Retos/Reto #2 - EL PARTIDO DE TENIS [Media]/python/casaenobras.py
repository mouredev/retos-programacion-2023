from pwn import log
from time import sleep


def tennis_match(match: list):

    points = ["Love", "15", "30", "40", "win"]
    
    p1_score = 0
    p2_score = 0
    win = False

    process = log.progress("Score")

    process.status(f" {points[p1_score]} - {points[p2_score]}")
    sleep(1)
    
    for point in match:

        if point.upper() == "P1":
            p1_score += 1
        elif point.upper() == "P2":
            p2_score += 1
        else:
            process.status(" La jugada no es válida")
            win = True
            break

        if p1_score >= 3 and p2_score >= 3:
            
            dif_score = p1_score - p2_score

            if dif_score == 0:
                process.status(" Deuce")
                sleep(1)

            elif dif_score == 1 or dif_score == -1:
                if p1_score > p2_score:
                    process.status(" Ventaja P1")
                else:
                    process.status(" Ventaja P2")
                    
                sleep(1)

            elif dif_score == 2 or dif_score == -2:
                if p1_score > p2_score:
                    process.status(" Ganador P1")
                else:
                    process.status(" Ganador P2")
                    
                win = True
                break

        else:
            if points[p1_score] == "win":
                process.status(" Ganador P1")
                win = True
            elif points[p2_score] == "win":
                process.status(" Ganador P2")
                win = True
            else:
                process.status(f" {points[p1_score]} - {points[p2_score]}")
                sleep(1)

    if not win:
        process.status(" No hay ganador con estas jugadas")



tennis_match(["p1", "p2", "p1", "p2", "p1", "p2", "p1", "p2", "p1", "p2", "p1", "p2", "p1", "p1", "p1"])
tennis_match(["p1", "p2", "p2", "p2"])
tennis_match(["p1", "p2", "p2", "p2", "p2"])
tennis_match(["p1", "p2", "p1", "p2", "p1", "p2", "p1", "p2", "p2", "p1", "p1", "p2", "p2", "p2", "p2"])
tennis_match(["p1", "P2", "p1", "p2", "1", "p2", "p1", "p2", "p1", "p2", "p1", "p2", "p1", "p1", "p1"])
