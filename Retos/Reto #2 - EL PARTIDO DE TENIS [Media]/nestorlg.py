import random

list_points = ["Love", "15", "30", "40"]

def tennisMatch(sequence):
    print("¡Comienza el partido!")
    points_p1 = 0
    points_p2 = 0
    
    for p in sequence:
        if (p == "P1"): # Punnto para P1
            points_p1 += 1
            
            # Si los dos jugadores van empate y tienen 3 puntos o mas (a partir de '40')
            # Printeamos 'Deuce'
            if (points_p1 == points_p2 and points_p1 >= 3):
                print("Deuce")
            
            # Si ambos jugadores tienen menos de 4 puntos (desde 'Love' hasta '40')
            # Printeamos la puntuacion indicada en la lista de puntuaciones del principio
            elif (points_p1 < 4 and points_p2 < 4):
                print(list_points[points_p1] + " - " + list_points[points_p2])
            
            # Si P1 tiene 3 puntos ('40') y P2 tiene menos de 2 puntos (desde 'Love' hasta '30'),
            # o P2 tiene mas de 3 puntos ('40') y P1 tiene 2 puntos mas que P2 ('Ventaja P1')
            # Printeamos 'Ha ganado el P1' y salimos del bucle
            elif (points_p1 == 4 and points_p2 < 3 or points_p1 > points_p2 + 1 and points_p2 >= 3):
                print("Ha ganado el P1")
                break
            
            # Si P1 tiene solo un punto mas que P2, printeamos 'Ventaja P1'
            elif (points_p1 == points_p2 + 1):
                print("Ventaja P1")
            
            # Cualquier otro caso seria un error
            else:
                print("ERROR")
                
        elif (p == "P2"): # Punto para P2
            points_p2 += 1
            
            # Si los dos jugadores van empate y tienen 3 puntos o mas (a partir de '40')
            # Printeamos 'Deuce'
            if (points_p1 == points_p2 and points_p2 >= 3):
                print("Deuce")
            
            # Si ambos jugadores tienen menos de 4 puntos (desde 'Love' hasta '40')
            # Printeamos la puntuacion indicada en la lista de puntuaciones del principio
            elif (points_p2 < 4 and points_p1 < 4):
                print(list_points[points_p1] + " - " + list_points[points_p2])
            
            # Si P2 tiene 3 puntos ('40') y P1 tiene menos de 2 puntos (desde 'Love' hasta '30'),
            # o P1 tiene mas de 3 puntos ('40') y P2 tiene 2 puntos mas que P1 ('Ventaja P2')
            # Printeamos 'Ha ganado el P2' y salimos del bucle
            elif (points_p2 == 4 and points_p1 < 3 or points_p2 > points_p1 + 1 and points_p1 >= 3):
                print("Ha ganado el P2")
                break
            
            # Si P2 tiene solo un punto mas que P1, printeamos 'Ventaja P2'
            elif (points_p2 == points_p1 + 1):
                print("Ventaja P2")
            
            # Cualquier otro caso seria un error
            else:
                print("ERROR")
                
        else:
            print("ERROR")
            break
        

tennisMatch(["P1", "P2", "P1", "P1", "P1"])
tennisMatch(["P2", "P1", "P1", "P2", "P1", "P2", "P2", "P2"])
tennisMatch(["P1", "P2", "P2", "P2", "P1", "P2"])
tennisMatch(["P1", "P1", "P1", "P2", "P2", "P2", "P1", "P2", "P1", "P1"])
tennisMatch(["P1", "P1", "P2", "P1", "P2", "P2", "P1", "P2", "P1", "P2", "P2", "P2"])
