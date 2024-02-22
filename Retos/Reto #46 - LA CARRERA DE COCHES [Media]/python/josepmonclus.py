'''
Crea un programa que simule la competición de dos coches en una pista.
- Los dos coches estarán representados por 🚙 y 🚗. Y la meta por 🏁.
- Cada pista tendrá entre 1 y 3 árboles 🌲 colocados de forma aleatoria.
- Las dos pistas tendrán una longitud configurable de guiones bajos "_".
- Los coches comenzarán en la parte derecha de las pistas. Ejemplo:
  🏁____🌲_____🚙
  🏁_🌲____🌲___🚗

El juego se desarrolla por turnos de forma automática, y cada segundo
se realiza una acción sobre los coches (moviéndose a la vez), hasta que
uno de ellos (o los dos a la vez) llega a la meta.
- Acciones:
  - Avanzar entre 1 a 3 posiciones hacia la meta.
  - Si al avanzar, el coche finaliza en la posición de un árbol,
    se muestra 💥 y no avanza durante un turno.
  - Cada turno se imprimen las pistas y sus elementos.
  - Cuando la carrera finalice, se muestra el coche ganador o el empate.
'''
import random

longitud_carrera = 10

def print_carrera():
    # print(''.join(map(str, carrera[0])))
    # print(''.join(map(str, carrera[1])))
    if posiciones[0] == len(carrera[0]):
        print(''.join(map(str, carrera[0])) + c1, end='')
    else:
        for i in range(0, len(carrera[0])):
            if i == posiciones[0]:
                if carrera[0][i] == arbol:
                    print(crash, end='')
                else:
                    print(c1, end='')
            else:
                print(carrera[0][i], end='')
    print('')
    if posiciones[1] == len(carrera[1]):
        print(''.join(map(str, carrera[1])) + c2, end='')
    else:
        for i in range(0, len(carrera[1])):
            if i == posiciones[1]:
                if carrera[1][i] == arbol:
                    print(crash, end='')
                else:
                    print(c2, end='')
            else:
                print(carrera[1][i], end='')
    print('\n')
    
def generar_carrera():
    global carrera
    carrera = [[meta], [meta]]
    for i in range(0, longitud_carrera):
        carrera[0].append(road)
        carrera[1].append(road)
        
    #Arboles carrera 1
    for i in range(0, n_arboles_1):
        while True:
            arbol_position = random.randint(1, longitud_carrera)
            if carrera[0][arbol_position] == road:
                carrera[0][arbol_position] = arbol
                break

    #Arboles carrera 2
    for i in range(0, n_arboles_2):
        while True:
            arbol_position = random.randint(1, longitud_carrera)
            if carrera[1][arbol_position] == road:
                carrera[1][arbol_position] = arbol
                break

c1 = '🚙'
c2 = '🚗'
meta = '🏁'
arbol = '🌲'
crash = '💥'
road = '_'

n_arboles_1 = random.randint(1, 3) 
n_arboles_2 = random.randint(1, 3) 

carrera = [[], []]
generar_carrera()

posiciones = [len(carrera[0]), len(carrera[1])]
avance_c1 = 0
avance_c2 = 0

while posiciones[0] > 0 and posiciones[1] > 0:
    print_carrera()
    
    if posiciones[0] < len(carrera[0]) and avance_c1 > 0 and carrera[0][posiciones[0]] == arbol:
        avance_c1 = 0
    else:
        avance_c1 = random.randint(1, 3)
    
    if posiciones[1] < len(carrera[1]) and avance_c2 > 0 and carrera[1][posiciones[1]] == arbol:
        avance_c2 = 0
    else:
        avance_c2 = random.randint(1, 3)
    
    posiciones[0] -= avance_c1 if posiciones[0] - avance_c1 >= 0 else posiciones[0]
    posiciones[1] -= avance_c2 if posiciones[1] - avance_c2 >= 0 else posiciones[1]

print_carrera()

if posiciones[0] == 0 and posiciones[1] == 0:
    print('Resultado final: EMPATE')
elif posiciones[0] == 0:
    print('Resultado final: Gana el coche 1')
else:
    print('Resultado final: Gana el coche 2')