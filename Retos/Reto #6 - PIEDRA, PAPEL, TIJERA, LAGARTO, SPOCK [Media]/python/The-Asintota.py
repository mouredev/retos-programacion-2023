'Reto #6: PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK'
'''
Crea un programa que calcule quien gana más partidas al piedra,
papel, tijera, lagarto, spock.

- El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
- La función recibe un listado que contiene pares, representando cada jugada.
- El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
"✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
- Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
- Debes buscar información sobre cómo se juega con estas 5 posibilidades.
'''

def play_now(movimientos:list)->str:
  '''
  Esta función analiza los movimientos de los dos jugadores y decide al ganador.
  
  El ganador será el mejor jugador en tres movimientos, si en los tres movimientos empatan
  gana quien haga el siguiente punto. El ganador de un movimiento se decide siguiendo las
  siguientes reglas:
    
    -tijera > lagarto.
    -tijera > papel.
    -papel > spock.
    -papel > piedra.
    -piedra > tijera.
    -piedra > lagarto.
    -lagarto > papel.
    -lagarto > spock.
    -spock > piedra.
    -spock > tijera.
  
  Args:
    -movimientos (list): Es una lista que contiene los movimientos de los jugadores. Se espera que cada
    elemento sea una tupla y que hayan más de tres.
  
  Return:
    -resultado (str): Es el ganador del duelo.
  '''
  
  diccionario = {
    'tijera':['lagarto', 'papel'],
    'papel':['spock', 'piedra'],
    'piedra':['tijera', 'lagarto'],
    'lagarto':['spock', 'papel'],
    'spock':['tijera', 'piedra']
  }
  contador = []
  
  for element in movimientos:

    if element[0] == element[1]:
      continue
    elif element[1] in diccionario.get(element[0]):
      contador.append('Player 1')
    else:
      contador.append('Player 2')

  if contador.count('Player 1') > contador.count('Player 2'):
    return 'Gana el Player 1.'
  else:
    return 'Gana el Player 2.'

# Elementos de prueba
lista0 = [("piedra","tijera"), ("tijera","piedra"), ("papel","tijera")]
lista1 = [("piedra","lagarto"), ("lagarto","lagarto"), ("lagarto","papel")]
lista2 = [("lagarto","lagarto"), ("piedra","piedra"), ("papel","papel"), ("spock", "papel")]
print(play_now(lista2))