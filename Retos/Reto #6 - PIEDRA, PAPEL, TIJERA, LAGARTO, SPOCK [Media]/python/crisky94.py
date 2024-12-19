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

def piedra_papel_tijera_lagarto_spock(partidas):
    reglas = {
        ("🗿", "📄"): "Player 2",
        ("🗿", "✂️"): "Player 1",
        ("🗿", "🦎"): "Player 1",
        ("🗿", "🖖"): "Player 2",
        ("📄", "🗿"): "Player 1",
        ("📄", "✂️"): "Player 2",
        ("📄", "🦎"): "Player 2",
        ("📄", "🖖"): "Player 1",
        ("✂️", "🗿"): "Player 2",
        ("✂️", "📄"): "Player 1",
        ("✂️", "🦎"): "Player 1",
        ("✂️", "🖖"): "Player 2",
        ("🦎", "🗿"): "Player 2",
        ("🦎", "📄"): "Player 1",
        ("🦎", "✂️"): "Player 2",
        ("🦎", "🖖"): "Player 1",
        ("🖖", "🗿"): "Player 1",
        ("🖖", "📄"): "Player 2",
        ("🖖", "✂️"): "Player 1",
        ("🖖", "🦎"): "Player 2"
    }
    resultados = []
    for partida in partidas:
        resultados.append(reglas[partida])
    return resultados

partidas = [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]

resultados = piedra_papel_tijera_lagarto_spock(partidas)

victoria_player1 = resultados.count('Player 1')
victoria_player2 = resultados.count('Player 2')

if victoria_player1 > victoria_player2:
    ganador = 'Player 1'
elif victoria_player1 < victoria_player2:
    ganador = 'Player 2'
else:
    ganador = 'Empate'

print(f'Entrada: {partidas}. Resulado: {ganador}')
