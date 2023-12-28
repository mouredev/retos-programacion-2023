"""
/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */
"""
def puntaje(puntos):
    if len(puntos) == 1:
        return puntos.append(15)    
    if len(puntos) == 2:
        return puntos.append(30)
    if len(puntos) == 3:
        return puntos.append(40)
    if len(puntos) == 4:
        return puntos.append('Ventaja')
    if len(puntos) == 5:
        return puntos.append('fin')

def buscar_ganador(punto_P1, punto_P2, jugador):
    if len(punto_P1) == 4 and len(punto_P2) == 4:
        return (False,"Deuce") 
    if len(punto_P1) == 5 and len(punto_P2) == 4:
        return (False, f"Ventaja {jugador}")
    if len(punto_P1) == 5 and len(punto_P2) == 5:
        punto_P1.pop(4)
        punto_P2.pop(4)
        return (False, "Douce")
    if len(punto_P1) == 6 and len(punto_P2) == 4:
        return (True, f"Ha ganado el {jugador}")
    if len(punto_P1) == 5 and len(punto_P2) < 4:
        return (True, f"Ha ganado el {jugador}")
    return (False, f"{punto_P1[len(punto_P1)-1]} - {punto_P2[len(punto_P2)-1]}")

def juego(secuencia):
    punto_P1 = ['Love']
    punto_P2 = ['Love']
    resultado = []
    for jugador in secuencia:
        if jugador == 'P1':
            puntaje(punto_P1)
            resultado = buscar_ganador(punto_P1, punto_P2, jugador)
            if resultado[0]:
                print(resultado[1])
                break
            else:
                print(resultado[1])
        else:
            puntaje(punto_P2)
            resultado = buscar_ganador(punto_P2, punto_P1, jugador)
            if resultado[0]:
                print(resultado[1])
                break
            else:
                print(resultado[1])
        

def main():
    secuencia = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']
    juego(secuencia)

if __name__ == "__main__":
    main()
