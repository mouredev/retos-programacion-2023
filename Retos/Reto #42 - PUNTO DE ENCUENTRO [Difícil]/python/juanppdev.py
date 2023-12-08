def punto_encuentro(coord_objeto1, velocidad_objeto1, coord_objeto2, velocidad_objeto2):
    # Calcula las diferencias entre las coordenadas iniciales de los objetos.
    diff_x = coord_objeto2[0] - coord_objeto1[0]
    diff_y = coord_objeto2[1] - coord_objeto1[1]

    # Calcula la diferencia de velocidad entre los dos objetos.
    diff_vel_x = velocidad_objeto2[0] - velocidad_objeto1[0]
    diff_vel_y = velocidad_objeto2[1] - velocidad_objeto1[1]

    # Comprueba si los objetos son paralelos (no se encuentran).
    if diff_vel_x == 0 and diff_vel_y == 0:
        return "Los objetos no se encuentran."

    # Calcula el tiempo en el que se encontrarán.
    tiempo_encuentro = (diff_x / diff_vel_x) if diff_vel_x != 0 else (diff_y / diff_vel_y)

    # Calcula las coordenadas del punto de encuentro.
    punto_x = coord_objeto1[0] + velocidad_objeto1[0] * tiempo_encuentro
    punto_y = coord_objeto1[1] + velocidad_objeto1[1] * tiempo_encuentro

    return f"Los objetos se encuentran en ({punto_x}, {punto_y}) en {tiempo_encuentro} unidades de tiempo."

# Ejemplo de uso:
coord_objeto1 = (0, 0)
velocidad_objeto1 = (1, 2)
coord_objeto2 = (3, 1)
velocidad_objeto2 = (1, 1)

resultado = punto_encuentro(coord_objeto1, velocidad_objeto1, coord_objeto2, velocidad_objeto2)
print(resultado)
