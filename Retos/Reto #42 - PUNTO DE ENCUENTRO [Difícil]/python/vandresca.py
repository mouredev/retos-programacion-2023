"""
/*
 * Crea una función que calcule el punto de encuentro de dos objetos en movimiento
 * en dos dimensiones.
 * - Cada objeto está compuesto por una coordenada xy y una velocidad de desplazamiento
 *   (vector de desplazamiento) por unidad de tiempo (también en formato xy).
 * - La función recibirá las coordenadas de inicio de ambos objetos y sus velocidades.
 * - La función calculará y mostrará el punto en el que se encuentran y el tiempo que tardarn en lograrlo.
 * - La función debe tener en cuenta que los objetos pueden no llegar a encontrarse.   
 */
"""


import numpy as np
import copy

class Point:
    x = None
    y = None

    # Métodos de la clase
    def __init__(self, x, y):
        self.x = y
        self.y = x


def printTable():
    for row in range(SIDE_TABLE):
        print()
        for col in range(SIDE_TABLE):
            print(str(table[row, col])+" ", end="")

def setValues(point1, point2):
    table[point1.x][point1.y] = "(x)"
    table[point2.x][point2.y] = "(x)"

def isOutTable(point1, point2):
    limit = SIDE_TABLE - 1
    if  (point1.x > limit or point2.x > limit 
        or point1.y > limit or point2.y > limit
        or point1.x == -1 or point2.x == -1
        or point1.y == -1 or point2.y == -1):
        return True
    return False


point1 = Point(5, 5)
point2 = Point(9, 1)

vectorSpeed1 = Point(1, 1)
vectorSpeed2 = Point(0, 2)

SIDE_TABLE = 15
modelTable = np.array([[" o "]*SIDE_TABLE]* SIDE_TABLE)
table = copy.copy(modelTable)
setValues(point1, point2)
while(True):
    print()
    print()    
    printTable()
    table = copy.copy(modelTable)
    if(point1.x == point2.x and point1.y == point2.y):
        print(f"Los dos puntos se encuentran en ({point1.x}, {point1.y})")
        break
    else:
        print("Los dos puntos no se encuentran")
    point1.x += vectorSpeed1.x
    point1.y += vectorSpeed1.y
    point2.x += vectorSpeed2.x
    point2.y += vectorSpeed2.y
    if isOutTable(point1, point2):
        break
    setValues(point1, point2)


