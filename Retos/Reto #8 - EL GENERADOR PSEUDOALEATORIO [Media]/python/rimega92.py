import time

def generar_numero_pseudoaleatorio():
    seed = int(time.time())  # Obtener el tiempo actual como semilla
    seed = (1103515245 * seed + 12345) % (2**31)  # Algoritmo lineal congruente
    numero_aleatorio = seed % 101  # Escalar el número para estar en el rango de 0 a 100
    return numero_aleatorio

numero_aleatorio = generar_numero_pseudoaleatorio()
print(numero_aleatorio)