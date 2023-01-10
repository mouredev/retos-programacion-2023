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

def puntuaciones_del_juego(lista_de_puntos):
    jugadores = {'P1':0,
                 'P2':0}
    for i in lista_de_puntos:
        if i.upper() == 'P1':
            jugadores[i.upper()] +=1
        elif i.upper() == 'P2':
            jugadores[i.upper()] +=1
            
    return list((jugadores['P1'], jugadores['P2']))
    
    
def imprimir_resultados(marcador):
    lista_de_marcador = ['love','15', '30', '40']
    return f'P1 {lista_de_marcador[marcador[0]]} - P2 {lista_de_marcador[marcador[1]]}'



""" for i in range(len(puntuaciones_del_juego(["P1", "P1"]))):
    print(imprimir_resultados(puntuaciones_del_juego(["P1", "P1"]))) """
    
print(imprimir_resultados(puntuaciones_del_juego(["P1", "P1", "P2"])))