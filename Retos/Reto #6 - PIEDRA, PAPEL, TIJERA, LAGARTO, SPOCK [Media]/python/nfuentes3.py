"""/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */"""
from enum import Enum

#Utilizamos la libreria enum para dar valores a los movimientos
class Valores(Enum):
    PIEDRA = "🗿"
    PAPEL = "📃"
    TIJERA = "✂️"
    LAGARTO = "🐊"
    SPOCK = "🖖"

#Definimos la funcion del juego
def game_pptls(game : list[tuple[str,str]]):
    p1_score = 0
    p2_score = 0
    
    for move in game:
        p1_move = move[0]
        p2_move = move[1]
        
        if p1_move != p2_move: #Creamos las condiciones de los movimientos con la suma de puntos
            if (p1_move == "🗿" and p2_move == "✂️") or (p1_move == "📃" and p2_move == "🗿") or (p1_move == "✂️" and p2_move == "📃") or (p1_move == "🐊" and p2_move == "🖖") or (p1_move == "🖖" and p2_move == "🗿"):
                p1_score += 1
            else:
                p2_score += 1

#Definimos los resultados segun su puntuacion
    if p1_score == p2_score:
        print('Tie!')
    elif p1_score > p2_score:
        print('Player 1')
    elif p2_score > p1_score:
        print('Player 2')
        
game_pptls([("📃","🗿"),("✂️","🗿"),("🖖","🗿")])
game_pptls([("🐊","📃"),("🖖","📃"),("✂️","📃")])
game_pptls([("🖖","🐊"),("🖖","🖖"),("🖖","📃"),("🗿","✂️"),("📃","🗿")])