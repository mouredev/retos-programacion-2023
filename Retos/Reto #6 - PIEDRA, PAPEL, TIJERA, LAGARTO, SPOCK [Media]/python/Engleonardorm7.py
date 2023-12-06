"""
   Crea un programa que calcule quien gana más partidas al piedra,
   papel, tijera, lagarto, spock.
   - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
   - La función recibe un listado que contiene pares, representando cada jugada.
   - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
     "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
   - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
   - Debes buscar información sobre cómo se juega con estas 5 posibilidades.

"""

entrada = [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]
#entrada = [("🗿","✂️"), ("🗿","✂️"), ("🖖","🦎"),("📄","✂️")]

player1=0
player2=0
for each in entrada:
    
    if each[0] == "🗿" and (each[1] == "✂️" or each[1] == "🦎"):
        player1 += 1
    elif each[0] == "📄" and (each[1] == "🗿" or each[1] == "🖖"):
        player1 += 1
    elif each[0] == "✂️" and (each[1] == "📄" or each[1] == "🦎"):
        player1 += 1
    elif each[0] == "🦎" and (each[1] == "📄" or each[1] == "✂️"):
        player1 += 1
    elif each[0] == "🖖" and (each[1] == "🗿" or each[1] == "✂️"):
        player1 += 1
    elif each[1] == "🗿" and (each[0] == "✂️" or each[0] == "🦎"):
        player2 += 1
    elif each[1] == "📄" and (each[0] == "🗿" or each[0] == "🖖"):
        player2 += 1
    elif each[1] == "✂️" and (each[0] == "📄" or each[0] == "🦎"):
        player2 += 1
    elif each[1] == "🦎" and (each[0] == "📄" or each[0] == "✂️"):
        player2 += 1
    elif each[1] == "🖖" and (each[0] == "🗿" or each[0] == "✂️"):
        player2 += 1

if player1>player2:
    print("Resultado: Player 1")
elif player2>player1:
    print("Resultado: Player 2")
else:
    print("Tie")