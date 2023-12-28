# # Reto #6: Piedra, Papel, Tijera, Lagarto, Spock
# #### Dificultad: Media | Publicación: 06/02/23 | Corrección: 13/02/23

# ## Enunciado

# ```
# /*
#  * Crea un programa que calcule quien gana más partidas al piedra,
#  * papel, tijera, lagarto, spock.
#  * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
#  * - La función recibe un listado que contiene pares, representando cada jugada.
#  * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
#  *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
#  * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
#  * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
#  */
# ```


def game(players):
  p1_points = 0
  p2_points = 0
  tie_count = 0
  msj = ""
  win_moves= {
  "🗿": ["✂️", "🦎"],
  "📄": ["🗿", "🖖"],
  "✂️" : ["📄","🦎"],
  "🦎": ["📄","🖖"],
  "🖖": ["✂️","🗿"]  
  }  
  
  for move in players:      
    if len(move) < 2: 
      return "Este juego es para 2 personas"
    
    elif move[0] == move[1]:
      
      tie_count+=1
      
    elif move[0] in win_moves[move[1]]:
      
      p2_points+=1
      
      
    else:
      
      p1_points+=1
      
  if p1_points > p2_points:
    msj="Jugador 1 es el ganador"
  elif p1_points == p2_points:
    msj="El juego esta empatado"
  else:
    msj="Jugador 2 es el ganador"
  
  return msj
    
        
        
        
        
         
    
print(game([("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]))
print(game([("🦎","🖖"), ("✂️","🦎"), ("📄","🗿")]))
print(game([ ("✂️","🦎"), ("📄","🗿")]))