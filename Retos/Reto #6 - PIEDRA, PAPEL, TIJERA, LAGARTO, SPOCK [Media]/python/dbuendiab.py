# 
# Información acerca del juego:

# https://www.hobbyconsolas.com/reportajes/curiosa-historia-mitico-piedra-papel-tijeras-lagarto-spock-sheldon-big-bang-theory-707343

# Las reglas son muy sencillas, según Sheldon. Las tijeras cortan el papel, el papel envuelve la piedra, 
# la piedra aplasta al lagarto, el lagarto envenena a Spock, Spock aplasta las tijeras, 
# las tijeras decapitan al lagarto, el lagarto devora el papel, el papel desaprueba a Spock, 
# Spock desintegra la piedra y, como siempre, la piedra aplasta las tijeras.

# Si expresamos estas reglas como una matriz, cuyos índices sean 

# 0: tijeras, 1: papel, 2: piedra, 3: lagarto, 4: spock

# tenemos la siguiente secuencia de ganadores:

# Jugador 1:    |  0   1   2   3   4 
# --------------|---------------------
# Jugador 2: 0  |  E  J2  J1  J2  J1
#            1  | J1   E  J2  J1  J2
#            2  | J2  J1   E  J2  J1
#            3  | J1  J2  J1   E  J2
#            4  | J2  J1  J2  J1   E
#
# Esto puede sumarizarse como sigue, siendo j1 y j2 los índices correspondientes a las respectivas apuestas:
#
# Si j1 == j2 -> Empate
# Si j1 y j2 tienen la misma paridad (ambos pares o ambos impares)
#   Si j1 > j2 (parte diagonal superior de la matriz), gana Jugador 1
#   Si j1 < j2 (parte diagonal inferior de la matriz), gana Jugador 2

# Variables para contener los símbolos
piedra  = "🗿" 
papel   = "📄"
tijeras  = "✂️" 
lagarto = "🦎" 
spock   = "🖖"

# Lista de apuestas ordenados por prioridad (tijeras gana a papel, papel a piedra, etc.)
apuestas = [tijeras, papel, piedra, lagarto, spock]


def misma_paridad(j1: int, j2: int) -> bool:
    """Devuelve True si ambos parametros son pares, o impares.
    Devuelve False si uno es par y el otro impar"""
    return j1 % 2 == j2 % 2


def ganador_jugada(apuesta_player_1: str, apuesta_player_2: str) -> str:
    """Dados un par de apuestas, determina el ganador"""

    # Indices de cada apuesta según la matriz de prioridades
    j1 = apuestas.index(apuesta_player_1)
    j2 = apuestas.index(apuesta_player_2)

    # Lógica del juego: si iguales, empate
    if j1 == j2:
        return 'Tie'

    # Si distintos, el ganador depende de la paridad y el orden, como se explica más arriba
    if misma_paridad(j1, j2):
        return 'Player 2' if j1 < j2 else 'Player 1'
    else:
        return 'Player 1' if j1 < j2 else 'Player 2'


def ganador_serie(apuestas: list) -> str:
    """Dada una lista de apuestas, determina qué jugador es el ganador"""

    # Contador de victorias
    victorias: int = 0

    # Cada elemento de 'apuestas' es una tupla (ap1, ap2) de apuestas
    for ap1, ap2 in apuestas:

        # Determina el jugador de la apuesta ganadora
        gana = ganador_jugada(ap1, ap2)

        # Sumamos o restamos una victoria, según el ganador
        if gana == 'Player 1':
            victorias += 1
        elif gana == 'Player 2':
            victorias -= 1
        else:
            pass    # En el caso de empate, no hacemos nada

    # Terminado el bucle, devolvemos el resultado
    if victorias > 0: return 'Player 1'
    if victorias < 0: return 'Player 2'
    return 'Tie'

# Varios intentos
print(ganador_serie([("🗿","✂️")]))                               # Gana Player 1
print(ganador_serie([("🗿","✂️"), ("✂️","🗿")]))                  # Empatan
print(ganador_serie([("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]))    # Gana Player 2
