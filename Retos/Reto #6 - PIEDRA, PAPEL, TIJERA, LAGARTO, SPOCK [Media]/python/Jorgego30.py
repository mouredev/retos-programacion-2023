#  * Crea un programa que calcule quien gana más partidas al piedra,
#  * papel, tijera, lagarto, spock.
#  * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
#  * - La función recibe un listado que contiene pares, representando cada jugada.
#  * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
#  *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
#  * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
#  * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.

p1_points=0
p2_points=0

jugada1=input()
jugada2=input()

if (jugada1==jugada2):
    p1_points=p2_points
elif (jugada1=="🗿" and (jugada2=="✂️" or jugada2=="🦎")):
    p1_points=1
elif (jugada1=="📄" and (jugada2=="🗿" or jugada2=="🖖")):
    p1_points=1
elif (jugada1=="✂️" and (jugada2=="📄" or jugada2=="🦎")):
    p1_points=1
elif (jugada1=="🦎" and (jugada2=="📄" or jugada2=="🖖")):
    p1_points=1
elif (jugada1=="🖖" and (jugada2=="✂️" or jugada2=="🗿")):
    p1_points=1
elif (jugada2=="🗿" and (jugada1=="✂️" or jugada1=="🦎")):
    p2_points=1
elif (jugada2=="📄" and (jugada1=="🗿" or jugada1=="🖖")):
    p2_points=1
elif (jugada2=="✂️" and (jugada1=="📄" or jugada1=="🦎")):
    p2_points=1
elif (jugada2=="🦎" and (jugada1=="📄" or jugada1=="🖖")):
    p2_points=1
elif (jugada2=="🖖" and (jugada1=="✂️" or jugada1=="🗿")):
    p2_points=1

if (p1_points>p2_points):
    print("Player 1")
elif(p2_points>p1_points) :
    print("Player 2")
else :
    print("Tie")
    