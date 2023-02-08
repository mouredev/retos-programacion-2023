"""
Este es el grafo que define las reglas de quien vence a quien en una jugada.
Dentro del diccionario la llave define el objeto y el valor define el conjunto de 
objetos a los que el objeto llave puede eliminar.
"""
rule_graph = {
    '✂️': ['📄', '🦎'],
    '📄': ['🗿', '🖖'],
    '🗿': ['🦎', '✂️'],
    '🦎': ['🖖', '📄'],
    '🖖': ['✂️', '🗿']
}


def play(p1, p2):
    """
    Se encarga de validar cada jagada del juego
    PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK.

    Args:
        p1: (str) Objeto que utilizó el jugador 1 (✂️, 📄, 🗿, 🦎 ó 🖖)
        p2: (str) Objeto que utilizó el jugador 1 (✂️, 📄, 🗿, 🦎 ó 🖖)

    Returns:
        result: (str) Objeto que ganó la jugada definido por las reglas en el grafo de reglas
        o si hubo un empate en dicha jugada
    """
    if p1 == p2:  # si ambos objetos son iguales hay un empate y retorno 0
        return 0
    for value in rule_graph[p1]:
        if p2 == value:  # Si p2 es igual a un objeto al que el objeto p1 es capaz de vencer retorno p1
            return p1
    return p2  # Si p1 no es capaz de vencer a p2 es porque p2 definitivamente vence a p1


def play_game(plays: list = []):
    """
    Define que jugador gana una partida del juego
    PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK.

    Para identificar a cada objeto usted debe emplear la siguiente nomenclatura:
    ✂️ - para tijera,
    📄 - para papel,
    🗿 - para piedra,
    🦎 - para lagarto,
    🖖 - para spock,

    Ej. [('🗿', '✂️'), ('✂️', '🗿'), ('📄', '🖖')]

    Args:
        plays: (list) Es una lista de tuplas que corresponden a cada jugada 

    Returns:
        result: (str) El resultado del juego
    """
    points_p1 = 0  # puntuación inicial del jugador 1
    points_p2 = 0  # puntuación inicial del jugador 2
    for p1, p2 in plays:  # recorriendo la lista de tuplas
        # verificando que objeto gana en la jugada actual
        result = play(p1, p2)
        if result == p1:  # Dependiendo del resultado, aumento el puntaje de un jugador u otro, o de ninguno en caso de empate
            points_p1 += 1
        elif result == p2:
            points_p2 += 1

    if points_p1 > points_p2:
        return 'Player 1'
    elif points_p2 > points_p1:
        return 'Player 2'
    return 'Tie'


result = play_game(
    [("🗿", "✂️"), ("✂️", "🗿"), ("📄", "✂️")])
print(result)
