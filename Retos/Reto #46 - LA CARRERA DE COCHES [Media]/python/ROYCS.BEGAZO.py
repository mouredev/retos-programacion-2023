import os
import random
import time

# Función para crear las pistas con árboles y coches
def tracks(length):
    track1 = ['_'] * length
    track2 = ['_'] * length
    track1 = tree(track1)
    track2 = tree(track2)
    track1.insert(0, "🏁")
    track1.append("🚙")
    track2.insert(0, "🏁")
    track2.append("🚗")
    return [track1, track2]

# Función principal de la carrera
def race():
    track1, track2 = tracks(20)
    car1 = '🚙'
    car2 = '🚗'
    status_1 = True
    status_2 = True

    while True:
        os.system('clear')
        print(''.join(track1))
        print(''.join(track2))

        track1, status_1 = movement(track1, car1, status_1)
        track2, status_2 = movement(track2, car2, status_2)
        os.system('clear')
        print(''.join(track1))
        print(''.join(track2))
        #Determinar ganador
        if track1[0] == '🚙' and track2[0] == "🚗":
            print('es un empate!!!!')
            break
        elif track1[0] == "🚙":
            print("🚙 ¡Ganó el coche 1!")
            break
        elif track2[0] == "🚗":
            print("🚗 ¡Ganó el coche 2!")
            break

        time.sleep(0.5)  # Pausa para visualizar el movimiento

# Función para mover un coche en la pista
def movement(track, car, status):
    if status:
        move = random.randint(1, 3)
        idx = track.index(car)
        new_position = max(0, idx - move)  # Evitar posición negativa

        # Colisión con un árbol
        if track[new_position] == '🌲':
            track[new_position], track[idx] = '💥', '_'

            status = False  # El coche queda inactivo
        else:

            track[idx], track[new_position] = track[new_position], track[idx]
        return track, status

    else:
        status = True
        crash = track.index('💥')
        track[crash] = car
        return track, status




# Función para añadir árboles aleatoriamente a la pista
def tree(track):
    def n_trees():
        return random.sample(range(1, len(track) - 1), k=random.randint(1, 3))
    
    for i in n_trees():
        track[i] = '🌲'
    return track

race()
