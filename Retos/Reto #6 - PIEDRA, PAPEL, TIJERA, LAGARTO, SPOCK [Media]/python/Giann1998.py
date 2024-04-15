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

def reto_6(tiradas):
    win_1=[
        ("🗿", "✂️"),
        ("🗿", "🦎"),
        ("📄", "🗿"),
        ("📄", "🖖"),
        ("✂️", "📄"),
        ("✂️", "🦎"),
        ("🦎", "📄"),
        ("🦎", "🖖"),
        ("🖖", "✂️"),
        ("🖖", "🗿")
    ]

    win_2=[
        ("✂️", "🗿"),
        ("🦎", "🗿"),
        ("🗿", "📄"),
        ("🖖", "📄"),
        ("📄", "✂️"),
        ("🦎", "✂️"),
        ("🗿", "🦎"),
        ("🖖", "🦎"),
        ("✂️", "🖖"),
        ("🗿", "🖖")
    ]

    p1=0
    p2=0

    for i in tiradas:
        if i in win_1:
            p1+=1
        elif i in win_2:
            p2+=1

    if p1<p2:
        return 'Player 2'
    elif p1>p2:
        return 'Player 1'
    else:
        return 'Tie'

print(reto_6([("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]))
