##
## Crea un programa que calcule quien gana más partidas al piedra,
## papel, tijera, lagarto, spock.
## - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
## - La función recibe un listado que contiene pares, representando cada jugada.
## - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
##   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
## - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
## - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
##/

def calcular_ganador(partidas):
    reglas = {
        ("🗿", "✂️"): "Player 1",
        ("✂️", "🗿"): "Player 2",
        ("🗿", "📄"): "Player 2",
        ("📄", "🗿"): "Player 1",
        ("📄", "✂️"): "Player 2",
        ("✂️", "📄"): "Player 1",
        ("✂️", "🦎"): "Player 2",
        ("🦎", "✂️"): "Player 1",
        ("🦎", "🖖"): "Player 2",
        ("🖖", "🦎"): "Player 1",
        ("🖖", "🗿"): "Player 2",
        ("🗿", "🖖"): "Player 1",
        ("📄", "🦎"): "Player 2",
        ("🦎", "📄"): "Player 1",
        ("🖖", "📄"): "Player 2",
        ("📄", "🖖"): "Player 1",
        ("✂️", "🖖"): "Player 2",
        ("🖖", "✂️"): "Player 1",
    }

    score_player_1 = 0
    score_player_2 = 0

    for jugada in partidas:
        if jugada[0] == jugada[1]:
            continue  # Empate, no cambia el marcador

        ganador = reglas.get(tuple(sorted(jugada)))
        if ganador == "Player 1":
            score_player_1 += 1
        elif ganador == "Player 2":
            score_player_2 += 1

    if score_player_1 > score_player_2:
        return "Player 1"
    elif score_player_2 > score_player_1:
        return "Player 2"
    else:
        return "Tie"

# Ejemplo de uso:
partidas = [("🗿", "✂️"), ("✂️", "🗿"), ("📄", "✂️")]
resultado = calcular_ganador(partidas)
print(resultado)