# Reto #6: Piedra, Papel, Tijera, Lagarto, Spock Dificultad: Media | Publicación: 06/02/23 | Corrección: 13/02/23
## Enunciado
# * Crea un programa que calcule quien gana más partidas al piedra,
# * papel, tijera, lagarto, spock.
# * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
# * - La función recibe un listado que contiene pares, representando cada jugada.
# * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
# *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
# * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
# * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.

def jugadas(cadena):
    play1=0
    play2=0
    for i in cadena:
        if i[0]=="🗿":
            if i[1]=="🦎" or i[1]=="✂️":
                play1+=1
            else:
                play2+=1
        elif i[0]=="📄":
            if i[1]=="🖖" or i[1]=="🗿":
                play1+=1
            else:
                play2+=1
        elif i[0]=="✂️":
            if i[1]=="📄" or i[1]=="🦎":
                play1+=1
            else:
                play2+=1
        elif i[0]=="🦎":
            if i[1]=="📄" or i[1]=="🖖":
                play1+=1
            else:
                play2+=1
        elif i[0]=="🖖":
            if i[1]=="✂️" or i[1]=="🗿":
                play1+=1
            else:
                play2+=1
    if play1>play2:
        res='Player 1'
    elif play1<play2:
        res='Player 2'
    else:
        res='Tie'
    return res

JUGADA1=jugadas([("🗿", "✂️"), ("✂️", "🗿"), ("📄", "✂️")])
JUGADA2=jugadas([("🦎", "🖖"), ("🗿", "📄")])
JUGADA3=jugadas([("✂️", "🦎"), ("🖖", "📄"), ("🗿", "✂️")])
JUGADA4=jugadas([("📄", "🦎"), ("✂️", "📄"), ("🗿", "🖖")])

print("El ganador es: ", JUGADA1)
print("El ganador es:", JUGADA2)
print("El ganador es: ", JUGADA3)
print("El ganador es: ", JUGADA4)
