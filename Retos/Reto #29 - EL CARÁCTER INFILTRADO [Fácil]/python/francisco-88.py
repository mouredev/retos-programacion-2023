def busca_caracteres_distintos(s1, s2):
    caracteres_distintos = []  # lista para almacenar los caracteres diferentes

    # Recorrer las cadenas de texto
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            caracteres_distintos.append(c2)

    return caracteres_distintos

# Contador de intentos
intentos = 0

while intentos < 3:
    # Solicitar las cadenas al usuario
    s1 = input("Por favor, ingresa la primera cadena de texto: ")
    s2 = input("Por favor, ingresa la segunda cadena de texto: ")

    # Verificar si las cadenas tienen la misma longitud
    if len(s1) != len(s2):
        print("Las cadenas deben tener la misma longitud. Inténtalo de nuevo.")
        intentos += 1
        continue

    # Calcular y mostrar los caracteres diferentes
    caracteres_distintos = busca_caracteres_distintos(s1, s2)
    print("Los caracteres diferentes en las cadenas de texto son:", caracteres_distintos)
    break  # Salir del bucle si todo salió bien

# En caso de agotar los intentos
if intentos == 3:
    print("Has superado el número máximo de intentos.")