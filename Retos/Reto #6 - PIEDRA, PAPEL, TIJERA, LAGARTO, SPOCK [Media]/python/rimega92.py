# Crea un programa que calcule quien gana más partidas al piedra,
# papel, tijera, lagarto, spock.
# - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
# - La función recibe un listado que contiene pares, representando cada jugada.
# - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
#   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
# - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
# - Debes buscar información sobre cómo se juega con estas 5 posibilidades.

def piedra_papel_tijera_lagarto_spock(lista):
   def get_winner(play1, play2):
      if play1 == play2:
         return 'Tie'
      elif (play1, play2) in [('🗿', '✂️'), ('🗿', '🦎'), ('📄', '🗿'), ('📄', '🖖'), ('✂️', '🖖'), ('✂️', '🦎'), ('🦎', '🖖'), ('🦎', '📄'), ('🖖', '🗿'), ('🖖', '✂️')]:
         return 'Player 1'
      else:
         return 'Player 2'

   player1 = 0
   player2 = 0
   for i in lista:
      winner = get_winner(i[0], i[1])
      if winner == 'Player 1':
         player1 += 1
      elif winner == 'Player 2':
         player2 += 1

   if player1 > player2:
      return 'Player 1'
   elif player2 > player1:
      return 'Player 2'
   else:
      return 'Tie'

print(piedra_papel_tijera_lagarto_spock([('🗿','✂️'), ('✂️','🗿'), ('📄','✂️')]))
print(piedra_papel_tijera_lagarto_spock([('🗿','🦎'), ('🦎','🗿'), ('📄','🦎')]))
print(piedra_papel_tijera_lagarto_spock([('🗿','🖖'), ('🖖','🗿'), ('📄','🖖')]))
print(piedra_papel_tijera_lagarto_spock([('🗿','📄'), ('📄','🗿'), ('📄','📄')]))