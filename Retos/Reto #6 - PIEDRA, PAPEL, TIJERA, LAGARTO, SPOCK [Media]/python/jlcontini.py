# Reto #6: Piedra, Papel, Tijera, Lagarto, Spock
#### Dificultad: Media | Publicación: 06/02/23 | Corrección: 13/02/23

## Enunciado

"""
```
/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */
```
#### Tienes toda la información extendida sobre los retos de programación semanales en **[retosdeprogramacion.com/semanales2023](https://retosdeprogramacion.com/semanales2023)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.
"""

"""
# Logica del juego en texto: 
Las tijeras cortan el papel, el papel envuelve la piedra, la piedra aplasta al lagarto, el lagarto envenena a Spock, Spock aplasta las tijeras, las tijeras decapitan al lagarto, el lagarto devora el papel, el papel desaprueba a Spock, Spock desintegra la piedra y, como siempre, la piedra aplasta las tijeras.
"""

# Asignación de números a las opciones
# tijera: 1, papel: 2, piedra: 3, lagarto: 4, spock: 5

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
  print(f"\ndef game_logic")
  
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
  
  print("def play_game")
  
  game_winner = ""
    
  # Assign element to player
  P1 = str(game_values[0])
  P2 = str(game_values[1])
  
  print(f"P1= {P1} , P2= {P2}")
  
  if P1 == P2:
    game_winner = "Tie"
  else:
    
    # order elements in list
    print("game_values original: ", game_values)
    game_sort = game_values.copy()
    game_sort.sort()
    print("game_values    .sort: ", game_sort)
    
    result = str(game_logic(game_sort))
    
    print(f"\nvuelvo a def play_game\nresult: {result} (wins)")
    print(f"'result' me devuelve el elemento que prevalece por lógica (gana) en valor numerico del 1 al 5")
    
    if result == P1:
      game_winner = "P1"
    elif result == P2:
      game_winner = "P2"
    else:
      
      print("No se pudo igualar a P1 ni a P2.")
      
  print("game_winner: ", game_winner)
  
  return game_winner


def check_winner_games(games_list):
  print("def check_winner_games")
  print(f"series of games:\n{games_list}\n")
  
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
  
  print(winner)
  
  return winner



def main():
  print("\nmain\n")
  
  # Elementos "✂️", "📄", "🗿", "🦎", "🖖"
  
  games_list = [("✂️", "✂️"), ("🦎", "✂️"), ("📄", "🗿",), ("🗿", "🖖"), ("🦎", "📄"), ("📄", "🖖"), ("🖖", "🦎"), ("🗿", "🦎"), ("📄", "✂️")]
  # games_list = [["🗿","✂️"]]
  
  # Ejemplo.
  # games_list = [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]
  # Resultado esperado: "Player 2".
                
  winner = check_winner_games(games_list)
  
  print(f"\n{winner}")
  print(f"\nEl ganador de los partidos es {winner}\n")
  


if __name__ == "__main__":
  main()
