
# Crea un programa que calcule quien gana más partidas al piedra,
# papel, tijera, lagarto, spock.
# - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
# - La función recibe un listado que contiene pares, representando cada jugada.
# - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
#   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
# - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
# - Debes buscar información sobre cómo se juega con estas 5 posibilidades.


class JuegoPiedraPapelTijera:
    def __init__(self):
        self.ganadores = {
            ("piedra", "tijera"): "Jugador 1 gana",
            ("piedra", "lagarto"): "Jugador 1 gana",
            ("papel", "piedra"): "Jugador 1 gana",
            ("papel", "spock"): "Jugador 1 gana",
            ("tijera", "papel"): "Jugador 1 gana",
            ("tijera", "lagarto"): "Jugador 1 gana",
            ("lagarto", "papel"): "Jugador 1 gana",
            ("lagarto", "spock"): "Jugador 1 gana",
            ("spock", "tijera"): "Jugador 1 gana",
            ("spock", "piedra"): "Jugador 1 gana",
            ("piedra", "piedra"): "Empate",
            ("papel", "papel"): "Empate",
            ("tijera", "tijera"): "Empate",
            ("spock", "spock"): "Empate",
            ("lagarto", "lagarto"): "Empate",
        }

    def jugar(self, jugadas):
        resultados = []
        for jugada in jugadas:
            player1, player2 = jugada.split(":")
            resultados.append(self.ganadores.get((player1, player2), "Jugador 2 gana"))
        return resultados


if __name__ == "__main__":
    juego = JuegoPiedraPapelTijera()
    jugadas = [
        "piedra:spock",
        "tijera:tijera",
        "piedra:tijera",
        "lagarto:piedra",
        "spock:lagarto",
    ]
    resultados = juego.jugar(jugadas)

    tot_jugador_1, tot_jugador_2  = 0, 0
    for resultado in resultados:
        print(resultado)
        if resultado == "Jugador 1 gana":
            tot_jugador_1 += 1
        elif resultado == "Jugador 2 gana":
            tot_jugador_2 += 1

    print("--------------")
    if tot_jugador_1 == tot_jugador_2:
        print("Empate!")
    elif tot_jugador_1 > tot_jugador_2:
        print("Jugador 1 gana!")
    else:
        print("Jugador 2 gana!")
