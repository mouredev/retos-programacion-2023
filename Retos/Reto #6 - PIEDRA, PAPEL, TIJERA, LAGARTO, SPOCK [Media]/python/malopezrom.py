# /*
# * Crea un programa que calcule quien gana más partidas al piedra,
# * papel, tijera, lagarto, spock.
# * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
# * - La función recibe un listado que contiene pares, representando cada jugada.
# * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
# *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
# * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
# * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
# */

# Opciones de juego
options = {"🗿", "📄", "✂️", "🦎", "🖖"}

# Resultado de la jugada
# 0 = empate
# 1 = gana player 1
# 2 = gana player 2
resultado = {0, 1, 2}

# Matriz de combinaciones posibles
combinaciones = { # piedra
                "🗿": {"🗿": 0, "📄": 2, "✂️": 1, "🦎": 1, "🖖": 2},
                # papel
                "📄": {"🗿": 1, "📄": 0, "✂️": 2, "🦎": 2, "🖖": 1},
                # tijera
                "✂️": {"🗿": 2, "📄": 1, "✂️": 0, "🦎": 1, "🖖": 2},
                # lagarto
                "🦎": {"🗿": 2, "📄": 1, "✂️": 2, "🦎": 0, "🖖": 1},
                # spock
                "🖖": {"🗿": 1, "📄": 2, "✂️": 1, "🦎": 2, "🖖": 0}
                }


# Clase que representa un juego
# list = lista de jugadas
# player1 = nombre del jugador 1
# player2 = nombre del jugador 2
class Game:
    def __init__(self, list, player1, player2):
        self.list = list
        self.player1 =player1
        self.player2 = player2


# /**
# * Funcion que busca el ganador si lo hay de una lista de jugadas
# * @ param listOfGame Listado de jugadas
# * @ return Resultado de la jugada
# * @ see Result
# */
def found_winner(game:Game):
    player1 = game.list.count(lambda: resultado[1])
    player2 = game.list.count(lambda: resultado[2])
    if player1 > player2:
        return game.player1
    elif player1 < player2:
        return game.player2
    else:
        return 0


# /**
# * Funcion que evalua una partida de piedra, papel, tijera
# * @ param game objeto que representa un juego con los jugadores y las jugadas de cada uno
# * @ return String con el nombre del jugador o empate en el que no hay ningun ganador
# */
def evaluate_game(game: Game) -> resultado:
    player1 = 0
    player2 = 0
    for i in game.list:
        if i[0] in options and i[1] in options:

            if combinaciones[i[0]][i[1]] == 1:
                player1 += 1
            elif combinaciones[i[0]][i[1]] == 2:
                player2 += 1
            else:
                player1 += 0
                player2 += 0

    if player1 > player2:
        return game.player1
    elif player1 < player2:
        return game.player2
    else:
        return "Empate"




#################### casos de prueba ####################

game1 = Game([["🗿", "✂️"],
             ["✂️", "🗿"],
             ["🦎", "✂️"],
             ["🗿", "📄"],
             ["📄", "🗿"],
             ["🗿", "🗿"],
             ["🖖", "🦎"],
             ["🖖", "✂️"]], "Player 1", "Player 2")
print("El resultado es : " + evaluate_game(game1))

game1 = Game([["🗿", "✂️"],
              ["🦎", "✂️"],
              ["🖖", "🗿"],
              ["🖖", "🖖"]], "Player 1", "Player 2")
print("El resultado es : " + evaluate_game(game1))

game1 = Game([["🖖", "🦎"],
              ["🦎", "🖖"],
              ["🖖", "🖖"]], "Player 1", "Player 2")
print("El resultado es : " + evaluate_game(game1))
