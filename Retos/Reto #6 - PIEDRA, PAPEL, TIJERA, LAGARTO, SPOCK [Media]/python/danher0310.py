# # Reto #6: Piedra, Papel, Tijera, Lagarto, Spock
# #### Dificultad: Media | Publicaci贸n: 06/02/23 | Correcci贸n: 13/02/23

# ## Enunciado

# ```
# /*
#  * Crea un programa que calcule quien gana m谩s partidas al piedra,
#  * papel, tijera, lagarto, spock.
#  * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
#  * - La funci贸n recibe un listado que contiene pares, representando cada jugada.
#  * - El par puede contener combinaciones de "馃椏" (piedra), "馃搫" (papel),
#  *   "鉁傦笍" (tijera), "馃" (lagarto) o "馃枛" (spock).
#  * - Ejemplo. Entrada: [("馃椏","鉁傦笍"), ("鉁傦笍","馃椏"), ("馃搫","鉁傦笍")]. Resultado: "Player 2".
#  * - Debes buscar informaci贸n sobre c贸mo se juega con estas 5 posibilidades.
#  */
# ```


def game(players):
  p1_points = 0
  p2_points = 0
  tie_count = 0
  msj = ""
  win_moves= {
  "馃椏": ["鉁傦笍", "馃"],
  "馃搫": ["馃椏", "馃枛"],
  "鉁傦笍" : ["馃搫","馃"],
  "馃": ["馃搫","馃枛"],
  "馃枛": ["鉁傦笍","馃椏"]  
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
    
        
        
        
        
         
    
print(game([("馃椏","鉁傦笍"), ("鉁傦笍","馃椏"), ("馃搫","鉁傦笍")]))
print(game([("馃","馃枛"), ("鉁傦笍","馃"), ("馃搫","馃椏")]))
print(game([ ("鉁傦笍","馃"), ("馃搫","馃椏")]))