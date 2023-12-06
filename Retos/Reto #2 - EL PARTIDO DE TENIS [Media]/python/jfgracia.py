 #
 # Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 # El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 # gane cada punto del juego.
 # 
 # - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 # - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 #   15 - Love
 #   30 - Love
 #   30 - 15
 #   30 - 30
 #   40 - 30
 #   Deuce
 #   Ventaja P1
 #   Ha ganado el P1
 # - Si quieres, puedes controlar errores en la entrada de datos.   
 # - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 #

# Recalcula los puntajes nuevos
# Regresa ambos puntajes en forma de arreglo
def new_scores(scores : [int,int], player_1_wins_point : bool) -> [] :

    # Extraer los marcadores
    # El jugador A sera el que anoto el tanto
    player_A_score = scores[0] if player_1_wins_point else scores[1]
    player_B_score = scores[1] if player_1_wins_point else scores[0]

    # Si ya hay un ganador, no se hace nada
    if player_A_score == 5 or player_B_score == 5 :
        return scores

    # Todas las formas de ganar
    if player_A_score == 3 and player_B_score < 3 : # Tiene 40 sin empate y anota
        player_A_score = 5 
    elif player_A_score == 4 : # Esta en ventaja y anota
        player_A_score = 5 # Gana
    # Caso especial, el jugador B tiene ventaja y anota jugador A
    elif player_A_score == 3 and player_B_score == 4 :
        player_B_score = 3 # Se regresan ambos a 40 "Deuce"
    # Cualquier otra cosa
    else :
        player_A_score += 1
    

    return [player_A_score, player_B_score] if player_1_wins_point else [player_B_score, player_A_score]

score_enum = { 0: "Love", 
               1: 15,
               2: 30,
               3: 40,
               4: "Advantage", # Caso especial
               5: "Win"}

sequence = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]

# Empezamos...
scores = [0,0]
print("Love All")

for point in sequence :

    scores = new_scores(scores,point == "P1")

    if scores[0] == 3 and scores[1] == 3 :
        print("Deuce")
    elif scores[0] == scores[1] :
        print(score_enum[scores[0]]," All")
    elif scores[0] == 4 :
        print("Ventaja P1")
    elif scores[1] == 4 :
        print("Ventaja P2")
    elif scores[0] == 5 :
        print("Gana P1")
    elif scores[1] == 5 :
        print("Gana P2")
    else :
        print(score_enum[scores[0]]," - ",score_enum[scores[1]])

