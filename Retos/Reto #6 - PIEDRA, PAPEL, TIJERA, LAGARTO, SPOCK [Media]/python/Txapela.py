#!/usr/bin/env python

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
# Inicio de la función
def round(game):

  modelwins = {"🗿":["✂️","🦎"] , "📄":["🗿","🖖"] , "✂️":["📄","🦎"] , "🦎":["📄","🖖"] , "🖖":["✂️","🗿"]}
  player_1 = 0
  player_2 = 0
  tie = 0

#Inicio del bucle "for" para recorrer posiciones y comparar valores
  for i in game:
    
    if i[0] == i[1]:
      tie += 1
    elif i[0] in modelwins[i[1]]:
      player_2 += 1
    else:
      player_1 += 1
  
# Impresión de resultados
  if player_1 > player_2:
    print ("PLAYER-1 WINS.")
  elif player_1 < player_2:
    print ("PLAYER-2 WINS.")
  else:
    print ("TIED GAME")

# Games
round([("🗿","✂️"), ("✂️","🦎"), ("📄","✂️")])   #Player-1 wins
round([("🗿","✂️"), ("✂️","🗿"), ("🗿","🗿")])   #Tie
round([("🗿","🖖"), ("🦎","🖖"), ("🦎","🗿")])   #Player-2 wins
round([("✂️","✂️"), ("🦎","🖖"), ("🦎","✂️"), ("🦎","🦎")])   #Tie
round([("🗿","✂️"), ("✂️","🦎"), ("📄","✂️"), ("🗿","✂️"), ("✂️","🦎"), ("📄","✂️")])   #Player-1 wins
