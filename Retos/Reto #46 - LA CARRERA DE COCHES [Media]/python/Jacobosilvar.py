#
#  Crea un programa que simule la competición de dos coches en una pista.
#  - Los dos coches estarán representados por 🚙 y 🚗. Y la meta por 🏁.
#  - Cada pista tendrá entre 1 y 3 árboles 🌲 colocados de forma aleatoria.
#  - Las dos pistas tendrán una longitud configurable de guiones bajos _.
#  - Los coches comenzarán en la parte derecha de las pistas. Ejemplo
#    🏁____🌲_____🚙
#    🏁_🌲____🌲___🚗
#  
#  El juego se desarrolla por turnos de forma automática, y cada segundo
#  se realiza una acción sobre los coches (moviéndose a la vez), hasta que
#  uno de ellos (o los dos a la vez) llega a la meta.
#  - Acciones
#    - Avanzar entre 1 a 3 posiciones hacia la meta.
#    - Si al avanzar, el coche finaliza en la posición de un árbol,
#      se muestra 💥 y no avanza durante un turno.
#    - Cada turno se imprimen las pistas y sus elementos.
#    - Cuando la carrera finalice, se muestra el coche ganador o el empate.
#    
#

import random
from time import sleep

# definicion de variables
META = '🏁'
OBSTACULO = '🌲'
PISTA = '_'
COLISION = '💥'
PLAYER = ['🚙', '🚗']


num_pistas = 10
long_pista = 75

min_obstaculos = 1
max_obstaculos = 3

min_movimiento = 1
max_movimiento = 3


def generar_pista():
    obstaculos, id_player = [], []
  
    for p in range(num_pistas):
        
        num_obstaculos = random.randint(min_obstaculos, max_obstaculos)
        obs = [random.randint(1, long_pista -2) for _ in range(num_obstaculos)]
        obstaculos.append(obs)

        id = p if p <= len(PLAYER) - 1 else random.randint(0, len(PLAYER) - 1)
        id_player.append(id)
        
    return obstaculos, id_player

def dibujar_pista(obstaculos, id_player, player):
    pista = []
    for p in range(num_pistas):
        track = [PISTA for _ in range(long_pista)]
        track[0] = META

        for i in obstaculos[p]:
            track[i] = OBSTACULO

        player_simbol = COLISION if player_position[p] in obstaculos[p] else PLAYER[id_player[p]]
        
        track[player_position[p]] = player_simbol
        
        pista.append(track)
        print(''.join(track))
    
    
    indices = [i for i, x in enumerate(player) if x == min(player)]
    if len(indices) > 1:
        mensaje = f'Empatados los jugadores {indices}'
    else:
        mensaje = f'En cabeza el jugador número {indices[0]}'

    print(f'.....................{mensaje}...........................\n')
    
    return

def generar_movimiento(player_position, obstaculos, player_crash):
    
    new_position = player_position.copy()

    for p in range(num_pistas):
        movimiento = random.randint(min_movimiento, max_movimiento)

        if player_crash[p]:
            new_position[p] = player_position[p]
            player_crash[p] = False
        else:
            new_position[p] = max(player_position[p] - movimiento, 0)
            if player_position[p] in obstaculos[p]:
                player_crash[p] = True
        
    return new_position, player_crash

def mostrar_ganador(new_player_position):

    indices = [i for i, x in enumerate(new_player_position) if x == 0]
    if len(indices) == 1:
        mensaje = f'Ganador el jugador número {indices[0]}'
    else:
        mensaje = f'Empatados los jugadores números {indices}'

    print('\n.........................................')
    print(f'      {mensaje}') 
    print('.........................................') 


if __name__ == '__main__':
    
    player_position = [long_pista - 1 for _ in range(num_pistas)]
    player_crash = [False for _ in range(num_pistas)]
    obstaculos, id_player = generar_pista()
    dibujar_pista(obstaculos, id_player, player_position)
    
    while True:
        
        new_player_position, player_crash = generar_movimiento(player_position, obstaculos, player_crash)
        player_finished = True if min(new_player_position) == 0 else False
        
        dibujar_pista(obstaculos, id_player, new_player_position)

        if player_finished:
            break
        else:
            player_position = new_player_position
            sleep(1)
        
    mostrar_ganador(new_player_position)
