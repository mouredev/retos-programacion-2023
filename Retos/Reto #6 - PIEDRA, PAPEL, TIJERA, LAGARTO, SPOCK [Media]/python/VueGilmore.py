'''
Reto #6: PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK

Dificultad: MEDIA

Crea un programa que calcule quien gana más partidas al piedra,
papel, tijera, lagarto, spock.
- El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
- La función recibe un listado que contiene pares, representando cada jugada.
- El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
  "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
- Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
- Debes buscar información sobre cómo se juega con estas 5 posibilidades.
'''

def calcular_ganador(player1, player2):
    if player1 == "🗿":
        if player2 == "🗿":
            return "Tie"
        elif player2 == "📄":
            return "Player 2"
        elif player2 == "✂️":
            return "Player 1"
        elif player2 == "🦎":
            return "Player 1"
        elif player2 == "🖖":
            return "Player 2"
    elif player1 == "📄":
        if player2 == "🗿":
            return "Player 1"
        elif player2 == "📄":
            return "Tie"
        elif player2 == "✂️":
            return "Player 2"
        elif player2 == "🦎":
            return "Player 2"
        elif player2 == "🖖":
            return "Player 1"
    elif player1 == "✂️":
        if player2 == "🗿":
            return "Player 2"
        elif player2 == "📄":
            return "Player 1"
        elif player2 == "✂️":
            return "Tie"
        elif player2 == "🦎":
            return "Player 1"
        elif player2 == "🖖":
            return "Player 2"
    elif player1 == "🦎":
        if player2 == "🗿":
            return "Player 2"
        elif player2 == "📄":
            return "Player 1"
        elif player2 == "✂️":
            return "Player 2"
        elif player2 == "🦎":
            return "Tie"
        elif player2 == "🖖":
            return "Player 1"
    elif player1 == "🖖":
        if player2 == "🗿":
            return "Player 1"
        elif player2 == "📄":
            return "Player 2"
        elif player2 == "✂️":
            return "Player 1"
        elif player2 == "🦎":
            return "Player 2"
        elif player2 == "🖖":
            return "Tie"


# Test
print(calcular_ganador("🗿","✂️"))
print(calcular_ganador("✂️","🗿"))
print(calcular_ganador("📄","✂️"))
print(calcular_ganador("🖖","🦎"))
print(calcular_ganador("🦎","🗿"))
