'''
* Crea un programa que calcule quien gana más partidas al piedra,
* papel, tijera, lagarto, spock.
* - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
* - La función recibe un listado que contiene pares, representando cada jugada.
* - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
*   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
* - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
* - Debes buscar información sobre cómo se juega con estas 5 posibilidades.

    Tijeras✂️ cortan papel📄
    Papel📄 cubre piedra🗿
    Piedra🗿 aplasta lagarto🦎
    Lagarto🦎 envenena Spock🖖
    Spock🖖 destruye tijeras✂️
    Tijeras✂️ decapitan lagarto🦎
    Lagarto🦎 come papel📄
    Papel📄 desaprueba Spock🖖
    Spock🖖 vaporiza piedra🗿
    Piedra🗿 aplasta tijeras✂️
'''


def game(player1, player2):
    if player1 == player2:
        return "Tie"
    
    if player1 in ("✂️", "📄", "🗿", "🦎", "🖖") and player2 in ("✂️", "📄", "🗿", "🦎", "🖖"):
        # Tijeras ✂️
        if player1 == "✂️" and player2 in ("📄", "🦎"):
            return "Player 1"
        elif player2 == "✂️" and player1 in ("📄", "🦎"):
            return "Player 2"
        # Papel 📄
        elif player1 == "📄" and player2 in ("🗿", "🖖"):
            return "Player 1"
        elif player2 == "📄" and player1 in ("🗿", "🖖"):
            return "Player 2"
        # Piedra 🗿
        elif player1 == "🗿" and player2 in ("🦎", "✂️"):
            return "Player 1"
        elif player2 == "🗿" and player1 in ("🦎", "✂️"):
            return "Player 2"
        # Lagarto 🦎
        elif player1 == "🦎" and player2 in ("🖖", "📄"):
            return "Player 1"
        elif player2 == "🦎" and player1 in ("🖖", "📄"):
            return "Player 2"
        # Spock 🖖
        elif player1 == "🖖" and player2 in ("✂️", "🗿"):
            return "Player 1"
        elif player2 == "🖖" and player1 in ("✂️", "🗿"):
            return "Player 2"

    return "Introduce opciones válidas."

# Ejemplos
print(game("✂️", "📄"))
print(game("📄", "🖖"))
print(game("🗿", "🦎"))
print(game("📄", "🦎"))
print(game("🦎", "🦎"))
print(game("Error", "📄"))
