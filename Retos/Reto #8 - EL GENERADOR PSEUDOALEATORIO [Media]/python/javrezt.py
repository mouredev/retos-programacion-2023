import time

# Obtenemos el tiempo actual en segundos
current_time = int(time.time())

# Usamos el tiempo actual como semilla
seed = current_time % 100  # Limitamos la semilla a 2 dígitos para que sea un número entre 0 y 99

# Definimos la función que genera números aleatorios
def generate_random_number():
    global seed
    a = 987654321
    c = 123456789
    m = 2**16
    seed = (a * seed + c) % m
    return seed % 101  # Limitamos el rango a 0-100

# Generamos un número aleatorio
random_number = generate_random_number()

# Imprimimos el número generado
print(random_number)