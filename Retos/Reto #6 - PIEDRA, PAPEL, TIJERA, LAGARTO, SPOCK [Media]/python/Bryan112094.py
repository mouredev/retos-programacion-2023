# Crea un programa que calcule quien gana más partidas al piedra,
# papel, tijera, lagarto, spock.
# - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
# - La función recibe un listado que contiene pares, representando cada jugada.
# - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
#   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
# - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
# - Debes buscar información sobre cómo se juega con estas 5 posibilidades.

dicci = {
    "✂️" : [ "📄", "🦎" ],
    "📄" : [ "🗿", "🖖" ],
    "🗿" : [ "🦎", "✂️" ],
    "🦎" : [ "🖖", "📄" ],
    "🖖" : [ "✂️", "🗿" ]
}
resultado = [ "Player 1", "Player 2", "Tie" ]

def juegoPPTLS(secuencia):
    jugador01 = 0
    jugador02 = 0
    for x in secuencia:
        valor = dicci.get(x[0])
        if x[1] in valor:
            jugador01 += 1
        else:
            jugador02 += 1
    
    if jugador01 == jugador02:
        return resultado[2]
    elif jugador01 > jugador02:
        return resultado[0]
    else:
        return resultado[1]

print(juegoPPTLS([("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]))
