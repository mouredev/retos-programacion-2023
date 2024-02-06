'''
Programa en Python que calcula el ganador del juego:
piedra ('🗿'), papel ('📄'), tijera ('✂️'), lagarto ('🦎') 
o spock ('🖖')

Autor: Aitor Blanco Fernández (blancoaitor003@gmail.com)
Fecha: 06-Feb-2024
'''

def piedra_papel_tijera_lagarto_spock(partidas) -> str:

  '''
  Método que se encarga de calcular el ganador de una partida
  del juego: piedra ('🗿'), papel ('📄'), tijera ('✂️'), lagarto ('🦎')
  o spock ('🖖').

  Explicación del código:
  
    1.- Se define un diccionario de reglas que mapea combinaciones de
  jugadas con resultados.

    2.- Se itera sobre las jugadas, aplicando las reglas y almacenando
  los resultados.

    3.- Se determina el resultando final encontando el elemento más
  comúm en la lista de resultados.

    4.- El método devuelve el resultado final del juego.

  Parámetros:

    - partida: Lista de tuplas que representa el par de
  jugadas.

  Retorna:

    - str: Resultado final del juego ("Player 1", "Player 2" o "Tie").
  '''

  # Definición de reglas con las combinaciones de jugadas con el resultado del juego.
  reglas = {
      ('🗿', '✂️'): 'Player 1', ('✂️', '🗿'): 'Player 2',  # Rock (🗿) crushes scissors (✂️)
    
      ('✂️', '📄'): 'Player 1', ('📄', '✂️'): 'Player 2',  # Scissors (✂️) cuts paper (📄)
    
      ('📄', '🗿'): 'Player 1', ('🗿', '📄'): 'Player 2',  # Paper (📄) coves rock (🗿)
    
      ('🗿', '🦎'): 'Player 1', ('🦎', '🗿'): 'Player 2',  # Rock (🗿) crushes lizard (🦎)
    
      ('🦎', '🖖'): 'Player 1',('🖖', '🦎'): 'Player 2',  # Spock (🖖) smashes scissors (✂️)
    
      ('✂️', '🦎'): 'Player 1', ('🦎', '✂️'): 'Player 2',  # Scissors (✂️) decapitates lizard (🦎)
    
      ('🦎', '📄'): 'Player 1', ('📄', '🦎'): 'Player 2',  # Lizard (🦎) eats paper (📄)
    
      ('📄', '🖖'): 'Player 1', ('🖖', '📄'): 'Player 2',  # Paper (📄) disproves Spock (🖖)
    
      ('🖖', '🗿'): 'Player 1', ('🗿', '🖖'): 'Player 2'  # Spock (🖖) vaporizes rock (🗿)
  }

  # Iteramos sobre cada par de jugadas y determinamos el resultado según las reglas del juego.
  resultados = [reglas.get(partida, "Tie") for partida in partidas]

  # Encontramos el ganador buscando el elemento más común en la lista de resultados.
  resultado_final = max(set(resultados), key=resultados.count)

  # Devolvemos el resultado final del juego.
  return resultado_final

# Ejemplo de uso:
partidas_ejemplo = [("🗿", "✂️"), ("✂️", "🗿"), ("📄", "✂️")]
resultado = piedra_papel_tijera_lagarto_spock(partidas_ejemplo)
print(resultado)
