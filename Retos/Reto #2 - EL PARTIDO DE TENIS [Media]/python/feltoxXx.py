# Reto #2: EL PARTIDO DE TENIS

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

def game_resolver(secuencia: list):    

    # Inicializar puntajes
    p1_puntaje = 0
    p2_puntaje = 0
    finished = False
    error = False

    # Mapear puntajes a su representación en el tenis
    puntajes = ["Love", "15","30","40"]

    for punto in secuencia:


        if punto == "P1":
            p1_puntaje += 1
        else:
            p2_puntaje += 1

        if p1_puntaje >= 3 and p2_puntaje >= 3:
            if not finished and abs(p1_puntaje - p2_puntaje) <= 1:
                print("Deuce" if p1_puntaje == p2_puntaje else
                      "Ventaja P1" if p1_puntaje > p2_puntaje else "Ventaja P2")
            else:
                finished = True
        else:
            if p1_puntaje < 4 and p2_puntaje < 4:
                print(f"{puntajes[p1_puntaje]} - {puntajes[p2_puntaje]}")
            else:
                finished = True
    
    if error or not finished:
        print("Los puntos no son correctos o faltan puntos para terminar el partido")
    else:
        print("Ha ganado el P1" if p1_puntaje > p2_puntaje else "Ha ganado el P2")



def main():
    
    secuencia = ["P1", "P1", "P2", "P2", "P2", "P1", "P1", "P2", "P1", "P1"]
    game_resolver(secuencia)

if __name__=="__main__":
    main()
