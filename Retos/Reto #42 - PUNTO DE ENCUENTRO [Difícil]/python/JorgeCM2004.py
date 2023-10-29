class Object():
    position: tuple
    speed: tuple

def ask_position(obj: str) -> tuple:
    coorx = int(input(f"Coordenada x del objeto {obj}: "))
    coory = int(input(f"Coordenada y del objeto {obj}: "))
    return (coorx, coory)

def ask_speed(obj: str) -> tuple:
    speedx = int(input(f"Velocidad en el eje x del objeto {obj}: "))
    speedy = int(input(f"Velocidad en el eje y del objeto {obj}: "))
    return (speedx, speedy)

def will_intersect(obj1: Object, obj2: Object) -> bool:
    return obj1.speed != obj2.speed

def same_position(obj1: Object, obj2: Object) -> bool:
    return obj1.position == obj2.position

def calculate_intersection(obj1: Object, obj2: Object) -> tuple:
    m1 = obj1.speed[1] / obj1.speed[0]
    m2 = obj2.speed[1] / obj2.speed[0]
    # Procedimiento seguido (Os lo dejo en codigo, si lo quereis ver Quitad las comillas)
    '''    
    eq1 = f"y = {m1} * (x - {obj1.position[0]}) + {obj1.position[1]}"
    eq2 = f"y = {m2} * (x - {obj2.position[0]}) + {obj2.position[1]}"
    resol1 = f"{m1} * (x - {obj1.position[0]}) + {obj1.position[1]} = {m2} * (x - {obj2.position[0]}) + {obj2.position[1]}"
    resol2 = f"{m1} * x - {m1} * {obj1.position[0]} + {obj1.position[1]} = {m2} * x - {m2} * {obj2.position[0]} + {obj2.position[1]}"
    resol3 = f"{m1} * x - {m2} * x = - {m2} * {obj2.position[0]} + {obj2.position[1]} + {m1} * {obj1.position[0]} - {obj1.position[1]}"
    resol4 = f"x * ({m1} - {m2}) = - {m2} * {obj2.position[0]} + {obj2.position[1]} + {m1} * {obj1.position[0]} - {obj1.position[1]}"
    resol4 = f"x = (- {m2} * {obj2.position[0]} + {obj2.position[1]} + {m1} * {obj1.position[0]} - {obj1.position[1]}) / ({m1} - {m2})"
    print("Estas rectas son las que describen el movimiento tanto para lo que hará como para lo que deberia hacer en tiempos negativos (avanzando en el tiempo tanto hacia delante como hacia detras)")
    print(f"Ecuacion del objeto B: {eq1}\nEcuacion del objeto B: {eq2}\nProcedimiento:\nPaso 1: {resol1}\nPaso 2: {resol2}\nPaso 3: {resol3}\nPaso 4: {resol4}")
    '''
    coor_x = (-m2 * obj2.position[0] + obj2.position[1] + m1 * obj1.position[0] -obj1.position[1]) / (m1 - m2)
    coor_y = m1 * coor_x - obj1.position[0] + obj1.position[1]
    return (coor_x, coor_y)

def main() -> None:
    objectA = Object(position = ask_position("A"), speed = ask_speed("A"))
    objectB = Object(position = ask_position("B"), speed = ask_speed("B"))
    if will_intersect(objectA, objectB):
        pass
    elif same_position(objectA, objectB):
        print("Los objetos A y B tienen tanto la misma direccion como la misma velocidad por lo que colisionaran en todos los puntos por los que pasen.")
    else:
        print(f"Aunque los objetos tengan distinta velocidad comienzan en el mismo punto de partida por lo que colisionarán en el punto ({objectA.position[0]}, {objectA.position[1]}) en el instante t = 0.")
    
if __name__ == "__main__":
    main()