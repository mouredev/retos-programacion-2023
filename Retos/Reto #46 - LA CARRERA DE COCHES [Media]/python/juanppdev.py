import random
import time

def generar_pista(longitud):
    # Genera una pista con árboles aleatorios
    pista = ["_" for _ in range(longitud)]
    num_arboles = random.randint(1, 3)
    for _ in range(num_arboles):
        posicion_arbol = random.randint(0, longitud - 1)
        pista[posicion_arbol] = "🌲"
    return pista

def imprimir_pistas(pista_1, pista_2):
    # Imprime las pistas y sus elementos
    print(" ".join(pista_1) + " 🚙")
    print(" ".join(pista_2) + " 🚗")
    print("🏁" + "____" * len(pista_1))

def carrera():
    # Configuración inicial
    longitud_pista = random.randint(5, 10)
    pista_1 = generar_pista(longitud_pista)
    pista_2 = generar_pista(longitud_pista)
    meta = longitud_pista * 4

    # Inicialización de posiciones de los coches
    posicion_coche_1 = longitud_pista - 1
    posicion_coche_2 = longitud_pista - 1

    while True:
        # Acciones de los coches
        avance_1 = random.randint(1, 3)
        avance_2 = random.randint(1, 3)

        # Actualizar posiciones
        posicion_coche_1 -= avance_1
        posicion_coche_2 -= avance_2

        # Verificar colisión con árboles
        if pista_1[posicion_coche_1] == "🌲":
            print("💥 Coche 1 choca con un árbol!")
            posicion_coche_1 += avance_1  # Retroceder al choque

        if pista_2[posicion_coche_2] == "🌲":
            print("💥 Coche 2 choca con un árbol!")
            posicion_coche_2 += avance_2  # Retroceder al choque

        # Imprimir pistas
        imprimir_pistas(pista_1, pista_2)

        # Verificar llegada a la meta
        if posicion_coche_1 <= 0 and posicion_coche_2 <= 0:
            print("Empate!")
            break
        elif posicion_coche_1 <= 0:
            print("¡Coche 1 gana!")
            break
        elif posicion_coche_2 <= 0:
            print("¡Coche 2 gana!")
            break

        # Esperar un segundo antes del próximo turno
        time.sleep(1)

# Iniciar la carrera
carrera()
