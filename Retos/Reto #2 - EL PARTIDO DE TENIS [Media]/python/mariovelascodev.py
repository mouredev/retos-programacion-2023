def match_tennis(points: list):
    #Declaración de variables
    result = ""
    player1 = 0
    player2 = 0
    game_sequence = {0:"Love", 1:"15", 2:"30", 3:"40", 4:"Ventaja", 5:"Ganador"}
    

    #Controlamos que se introduce un valor iterable
    try:
        #Recorremos la lista introducida por parámetros y convertimos los valores en mayúsculas
        for game in points:
            if game.upper() == "P1":
                player1 += 1
            elif game.upper() == "P2":
                player2 += 1
            else:
                print("La lista solo puede contener valores P1 y P2")
                break

            #Si ambos jugadores empatan a 40 se muestra Deuce
            if game_sequence[player1] == "40" and game_sequence[player2] == "40":
                result += "Deuce\n"
            #Si ambos jugadores llegan a Ventaja se muestra Deuce y 
            #se les reduce un punto a cada jugador    
            elif game_sequence[player1] == "Ventaja" and game_sequence[player2] == "Ventaja":
                result += "Deuce\n"
                player1 -= 1
                player2 -= 1
            #Si un jugador tiene ventaja se muestra el jugador que tiene ventaja
            elif game_sequence[player1] == "Ventaja" or game_sequence[player2] == "Ventaja":
                result += "Ventaja {player}\n".format(player = game)
            #Se muestra el jugador que ha ganado el partido
            elif game_sequence[player1] == "Ganador" or game_sequence[player2] == "Ganador":
                result += "Ha ganador el {player}\n".format(player = game)
                break
            #Muestra el resto del marcador del partido
            else:
                result += game_sequence[player1] +" - "+ game_sequence[player2] +"\n"
            
        return result
    except TypeError:
        print("Introduce una lista")


print(match_tennis(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]))
print(match_tennis(["p1", "p1", "p2", "p2", "p1", "p2", "p2", "p1","p2","p2"]))