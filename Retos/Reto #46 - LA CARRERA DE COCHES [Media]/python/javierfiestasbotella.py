# Reto #46: La carrera de coches
#### Dificultad: Media | Publicación: 27/11/23 | Corrección: 04/12/23

## Enunciado

'''
/*
 * Crea un programa que simule la competición de dos coches en una pista.
 * - Los dos coches estarán representados por 🚙 y 🚗. Y la meta por 🏁.
 * - Cada pista tendrá entre 1 y 3 árboles 🌲 colocados de forma aleatoria.
 * - Las dos pistas tendrán una longitud configurable de guiones bajos "_".
 * - Los coches comenzarán en la parte derecha de las pistas. Ejemplo:
 *   🏁____🌲_____🚙
 *   🏁_🌲____🌲___🚗
 * 
 * El juego se desarrolla por turnos de forma automática, y cada segundo
 * se realiza una acción sobre los coches (moviéndose a la vez), hasta que
 * uno de ellos (o los dos a la vez) llega a la meta.
 * - Acciones:
 *   - Avanzar entre 1 a 3 posiciones hacia la meta.
 *   - Si al avanzar, el coche finaliza en la posición de un árbol,
 *     se muestra 💥 y no avanza durante un turno.
 *   - Cada turno se imprimen las pistas y sus elementos.
 *   - Cuando la carrera finalice, se muestra el coche ganador o el empate.
 *   
 */'''

import time
import random
import threading

class Fast_Furious:
    player_1 = '🚙'
    player_2 = '🚗'
    crash = '💥'
    meta = '🏁'
    arbol = '🌲'
    carretera = '_'

    def __init__(self):
        self.posiciones = 15
        self.avance = random.randint(1, 3)
        self.pista = [self.carretera, self.arbol, self.carretera, self.carretera, self.carretera]
        self.winner = None  
        self.lock = threading.Lock() 

    def crea_pista_obstaculos(self):
        pista_1 = self.meta
        pista_2 = self.meta
        for i in range(self.posiciones - 1):
            componente_1 = random.choice(self.pista)
            componente_2 = random.choice(self.pista)

            pista_1 += componente_1
            pista_2 += componente_2
        pista_1 += self.player_1
        pista_2 += self.player_2
        return pista_1, pista_2

    def start(self, v, n):
        for i in range(14, 0, -1):
            time.sleep(1)
            if v[i] == self.carretera:
                print(v[:i] + n)
            elif v[i] == self.arbol:
                print(v[:i+1], self.crash + n)
            elif v[i] == self.meta:
                with self.lock:
                    if self.winner is None:
                        self.winner = n
                        break

def ejecutar_carrera(pista, jugador, carrera):
    carrera.start(pista, jugador)

carrera_1 = Fast_Furious()

pista_1, pista_2 = carrera_1.crea_pista_obstaculos()

hilo_1 = threading.Thread(target=ejecutar_carrera, args=(pista_1, carrera_1.player_1, carrera_1))
hilo_2 = threading.Thread(target=ejecutar_carrera, args=(pista_2, carrera_1.player_2, carrera_1))


time.sleep(1)
print('3...2...1...Ya!!!')
hilo_1.start()
hilo_2.start()

hilo_1.join()
hilo_2.join()
time.sleep(1)

with carrera_1.lock:
    if carrera_1.winner is not None:
        print(f'¡{carrera_1.winner} ha ganado!')
