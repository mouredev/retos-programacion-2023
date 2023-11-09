"""
# Reto #6: Piedra, Papel, Tijera, Lagarto, Spock
#### Dificultad: Media | Publicación: 06/02/23 | Corrección: 13/02/23
## Enunciado
```
/*
 * Crea un programa que calcule quien gana más partidas al piedra, papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel), "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */
```
"""

"""
* * * * * * * * * * * * 
Solución Reto #6
Se plantearon varias pasos para resolverlo, quedo un poco extenso, y al final se vieron elementos no tan necesarios. Se hizo un 'camino largo'.

Se recibe una coleccion de pares de elementos. 
Se crea un nuevo par, asignando un str(numero) a cada elemento gráfico y se los une en un list
Se comparan pares de strings con una coleccion de pares dict del cual se devuelve un único valor (str) que resulta el que prevalece.
Con este valor se obtiene el elemento ganador del partido individual y se suma en una variable.
Finalizada la sumatoria el ganador es devuelto como 'Player 1', 'Player 2' o 'Tie'.

# Logica del juego en texto: 
# Las tijeras cortan el papel, el papel envuelve la piedra, la piedra aplasta al lagarto, el lagarto envenena a Spock, Spock aplasta las tijeras, las tijeras decapitan al lagarto, el lagarto devora el papel, el papel desaprueba a Spock, Spock desintegra la piedra y, como siempre, la piedra aplasta las tijeras.
"""

# Asignacion de numeros a las opciones graficas en un diccionario
game_options: dict = {
"✂️": 1,
"📄": 2,
"🗿": 3,
"🦎": 4,
"🖖": 5
}

print(f"\nDiccionario 'game_options'\n{game_options}")


def assign_game_key_values(game) -> list:
  # Assign key value to game graphic elements
  game_key_values = []
  counter = 0
  
  for element in game:
    counter += 1
    if counter < 3:
      
      for key in game_options:
        if key == element:
          game_key_values.append(game_options[key])
        else:
          continue
          
    else:
      return IOError("The game has too many elements (more than 2)")
  
  print(f"\ngame: {game}\ngame_key_values: {game_key_values}")
  
  return game_key_values


# Lógica para ganar el juego
def game_logic(game_values: list) -> str:
  result = ""
  
  if game_values[0] == game_values[1]:
    result = 0
  elif game_values in [[1, 2], [1, 4]]:   # suman 3 y 5 # restan -1 1 // -3 3
    result = 1
  elif game_values in [[2, 3], [2, 5]]: # suman 5 y 7 # restan -1 1 // -3 3
    result = 2
  elif game_values in [[3, 4], [1, 3]]: # suman 7 y 4 # restan -1 1 // 2 -2
    result = 3
  elif game_values in [[4, 5], [2, 4]]: # suman 9 y 6 # restan 1 -1 // 2- 2
    result = 4
  elif game_values in [[1, 5], [3, 5]]: # suman 6 y 8 # restan 4 -4 // 2 -2
    result = 5
  else:
    IOError("Input Error in game_values at def game_logic.")
  
  game_winner = str(result)
  
  print(f"game_winner: {game_winner}")
  
  return game_winner


def play_game(game_values: list) -> str:
  game_winner = ""
    
  # Assign element to player
  P1 = str(game_values[0])
  P2 = str(game_values[1])
  
  if P1 == P2:
    game_winner = "Tie"
  else:
    
    # order elements in list
    game_sort = game_values.copy()
    game_sort.sort()
    
    result = str(game_logic(game_sort))
    
    if result == P1:
      game_winner = "P1"
    elif result == P2:
      game_winner = "P2"
      
  return game_winner


def check_winner_games(games_list):  
  P1 = 0
  P2 = 0
  game_count = 0
  
  for each_game in games_list:
    
    game_with_key_values = assign_game_key_values(each_game)
    game_winner = play_game(game_with_key_values)
    
    if game_winner == "P1":
      P1 += 1
    elif game_winner == "P2":
      P2 += 1
    elif game_winner == "Tie":
      pass
  
    game_count += 1
    print(f"Game {game_count}: {each_game}\nP1: {P1} - P2: {P2}\n")
  
  if P1 == P2:
    winner = "Tie"
  elif P1 > P2:
    winner = "Player 1"
  else:
    winner = "Player 2"
  
  return winner



def main():
    
  games_list = [("✂️", "✂️"), ("🦎", "✂️"), ("📄", "🗿",), ("🗿", "🖖"), ("🦎", "📄"), ("📄", "🖖"), ("🖖", "🦎"), ("🗿", "🦎"), ("📄", "✂️")]

  # Ejemplo.
  # games_list = [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]
  # Resultado esperado: "Player 2".
                
  winner = check_winner_games(games_list)
  
  print(f"\nEl ganador de los partidos es {winner}\n")
  


if __name__ == "__main__":
  main()
