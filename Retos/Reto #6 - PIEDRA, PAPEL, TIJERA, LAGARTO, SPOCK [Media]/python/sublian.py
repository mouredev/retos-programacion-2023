"""
# Reto #6: Piedra, Papel, Tijera, Lagarto, Spock
#### Dificultad: Media | Publicación: 06/02/23 | Corrección: 13/02/23
## Enunciado
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */
"""

def rock_paper_scissor_lizard_spock(games):
    #declaracion de regla de juego
    game_rules ={"🗿": [ "✂️", "🦎"],
                "📄": [ "🗿", "🖖"],
                "✂️": [ "📄", "🦎"],
                "🦎": [  "📄", "🖖"],
                "🖖": [ "🗿", "✂️"],
                "piedra": ["tijera","lagarto"],
                "tijera": ["papel","lagarto"],
                "papel": ["piedra","spock"],
                "lagarto": ["papel","spock"],
                "spock": ["tijera","piedra"],
                "rock": ["scissor","lizard"],
                "scissor": ["paper","lizard"],
                "paper": ["stone","spock"],
                "lizard": ["papel","spock"],
                "spock": ["scissor","stone"]}
    
    #declaracion de contadores
    player_one, player_two=0,0
        
    for game in games:        
        #lector de cada partida
        player_one_game=game[0]        
        player_two_game=game[1]
        
        if player_one_game!=player_two_game:
            if player_two_game in game_rules[player_one_game]:
                player_one+=1
            else:
                player_two+=1
    
    return "Tie" if player_one==player_two else "Player 1 Win!" if player_one>player_two else "Player 2 Win!"
    
if __name__ == '__main__':

    print(rock_paper_scissor_lizard_spock([("🗿", "📄")]))  
    print(rock_paper_scissor_lizard_spock([("🦎", "🦎")]))  
    print(rock_paper_scissor_lizard_spock([("🗿", "📄"), ("📄", "📄"), ("✂️", "📄"), ("🦎", "📄")]))    
    print(rock_paper_scissor_lizard_spock([("piedra", "tijera"), ("papel","spock"), ("lagarto","papel")]))  
    print(rock_paper_scissor_lizard_spock([("rock", "scissor"), ("paper","spock"), ("lizard","paper")]))  
    print(rock_paper_scissor_lizard_spock([("rock", "rock")]))  