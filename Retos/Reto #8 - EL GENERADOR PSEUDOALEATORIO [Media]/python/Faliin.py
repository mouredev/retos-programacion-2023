# Define una semilla inicial
seed = 0

# Genera 1 números pseudoaleatorios entre 0 y 100
for i in range(1):
    # Actualiza la semilla con un valor diferente en cada iteración
    seed += i + 1

    # Calcula el número pseudoaleatorio
    random_num = abs(hash(str(seed))) % 101

    # hash es el sustituyente de random aunque random es más competente pero Moure no quiere que lo utilicemos ahora.

    # Imprime el resultado
    print(random_num)
