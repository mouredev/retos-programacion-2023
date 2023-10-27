"""/*
 * Crea una función que calcule el punto de encuentro de dos objetos en movimiento
 * en dos dimensiones.
 * - Cada objeto está compuesto por una coordenada xy y una velocidad de desplazamiento
 *   (vector de desplazamiento) por unidad de tiempo (también en formato xy).
 * - La función recibirá las coordenadas de inicio de ambos objetos y sus velocidades.
 * - La función calculará y mostrará el punto en el que se encuentran y el tiempo que tardarn en lograrlo.
 * - La función debe tener en cuenta que los objetos pueden no llegar a encontrarse.   
 */"""

import random

def funciones_lineales(x1, y1, veloc1, x2, y2, veloc2):

    # m1*x1 + n1*y1 = result1
    # m2*x2 + n2*y2 = result2
    # Se estipulan en forma aleatorias las pendientes de las rectas de accion
    m1 = random.randint(-10,10)
    n1 = random.randint(-10,10)
    m2 = random.randint(-10,10)
    n2 = random.randint(-10,10)

    # Obtencion de los datos faltantes para aplicar la regla de Cramer (determinantes)
    result1 = (m1 * x1) + (n1 * y1)
    result2 = (m2 * x2) + (n2 * y2)
    
    determinante = (m1 * n2) - (n1 * m2)
    if determinante == 0:
        print("Las rectas son paralelas, no se seguir calculando.")
        exit()
    else:
        # Calculo coordenadas de cruce
        x_intersect = (((result1 * n2) - (n1 * result2)) / determinante)
        x_intersect = round(x_intersect, 2)
        y_intersect = (((m1 * result2) - (result1 * m2)) / determinante)
        y_intersect = round(y_intersect, 2)
        
        # Calculo de distancias desde origen a punto de cruce con el Teorema de Pitagoras       
        dist1 = (((x_intersect - x1) ** 2) + ((y_intersect - y1) ** 2)) ** .5
        dist1 = round(dist1, 2)
        dist2 = (((x_intersect - x2) ** 2) + ((y_intersect - y2) ** 2)) ** .5
        dist2 = round(dist2, 2)
        
        # Calculo de tiempo hasta el cruce
        tiempo1 = round((dist1 / veloc1), 2)
        tiempo2 = round((dist2 / veloc2), 2)
        
        print("\nLOS RESULTADOS SON:")
        print(f"Ambas rectas se cruzan en el punto ({x_intersect}, {y_intersect})")
        print(f"La distancia recorrida por el primer vector es {dist1} y le tomo {tiempo1} de tiempo." )
        print(f"La distancia recorrida por el segundo vector es {dist2} y le tomo {tiempo2} de tiempo." )

x1 = int(input("Ingrese la coordenada en x del primer punto: "))
y1 = int(input("Ingrese la coordenada en y del primer punto: "))
veloc1 = int(input("Ingrese la velocidad del primer punto: "))
print("\n")
x2 = int(input("Ingrese la coordenada en x del segundo punto: "))
y2 = int(input("Ingrese la coordenada en y del segundo punto: "))
veloc2 = int(input("Ingrese la velocidad del segundo punto: "))

if x1 != x2 and y1 != y2:    
    funciones_lineales(x1, y1, veloc1, x2, y2, veloc2)
else: 
    print("Ambas coordenadas son identicas. Se cruzan antes de iniciar el movimiento.")
    