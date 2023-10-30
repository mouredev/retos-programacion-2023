import math
from matplotlib import pyplot as plt
import numpy

def detectar_colision(coor1, coor2, vel1, vel2, plot_graph=False):
    '''
    Determina si dos objetos colisionarán en el plano y muestra un gráfico si se especifica.

    Parámetros:
    coor1 (tuple): Coordenadas iniciales del objeto 1 (x1, y1).
    coor2 (tuple): Coordenadas iniciales del objeto 2 (x2, y2).
    vel1 (tuple): Velocidades del objeto 1 en (vx1, vy1).
    vel2 (tuple): Velocidades del objeto 2 en (vx2, vy2).
    plot_graph (bool, opcional): True si se debe mostrar un gráfico, False por defecto.

    Retorna:
    bool: True si los objetos colisionan, False si no.
    '''
    colision = False
    try:
        # Asigno el valor de las tuplas a variables individuales
        vx1, vy1 = vel1
        vx2, vy2 = vel2

        x1, y1 = coor1
        x2, y2 = coor2

        # Verifico la condición de que no parten del mismo punto
        if (x1 == x2) and (y1 == y2):
            print("Ambos objetos están colisionados antes de iniciar su movimiento.")
            x = x1
            y = y1
            alpha = 0
            colision = True
        else:
            # Verifico que ambas trayectorias no sean coplanares
            if (vx1 * vy2 - vy1 * vx2) != 0:
                # Calculo alpha y beta de sus ecuaciones vectoriales
                beta = (vx1 * (y1 - y2) + vy1 * (x2 - x1)) / (vx1 * vy2 - vy1 * vx2)
                if vy1 != 0:
                    alpha = (y2 - y1 + beta * vy2) / vy1
                elif vx1 != 0:
                    alpha = (x2 - x1 + beta * vx2) / vx1

                x = x2 + beta * vx2
                y = y2 + beta * vy2

                # Si alpha y beta son iguales (tiempo) hay colisión, sino solamente intersección de trayectorias
                if alpha == beta and alpha > 0:
                    print(f"Los objetos colisionan en ({x:.2f}, {y:.2f}) transcurridos {alpha:.2f} segundos.")
                    colision = True
                else:
                    print(f"Si bien las trayectorias se intersectan en ({x:.2f}, {y:.2f}), no hay colisión entre objetos.")
            else:
                # Hago el análisis puntual de trayectorias coplanares
                vect1 = complex(vx1, vy1)
                vect12 = complex(x2-x1, y2-y1)
                vect21 = complex(x1-x2, y1-y2)
                
                ang_vect1 = numpy.angle(vect1)
                ang_vect12 = numpy.angle(vect12)
                ang_vect21 = numpy.angle(vect21)

                # Determino la colinealidad mediante compara el vector entre P1 y P2 y una de las velocidades
                if ang_vect1 == ang_vect12 or ang_vect1 == ang_vect21:
                    alpha = -math.inf
                    beta = -math.inf    
                    # Para ello calculo la constante del vector
                    if vx1 - vx2 != 0:
                        alpha = (x2 - x1) / (vx1 - vx2)
                    if vy1 - vy2 != 0:
                        beta = (y2 - y1) / (vy1 - vy2)
                    # Si la velocidad en ambos ejes son igualesquiere decir que van a la misma velocidad
                    if alpha == -math.inf and beta == -math.inf:
                        print("Los objetos van a la misma velocidad, no habrá colisión.")
                    elif (alpha == -math.inf and beta > 0) or (beta == -math.inf and alpha > 0) or (beta == alpha > 0):
                        if alpha <= 0:
                            alpha = beta
                        x = x1 + alpha * vx1
                        y = y1 + alpha * vy1
                        print(f"Los objetos colisionan en ({x:.2f}, {y:.2f}) transcurridos {alpha:.2f} segundos.")
                        colision = True
                    else:
                        print("Los objetos son colineales pero van separándose, no habrá colisión.")

                else:
                    print("Las trayectorias son paralelas, no habrá colisión.")                       
                
        if colision and plot_graph:
            plt.axhline(0, color='black', linewidth=0.65)
            plt.axvline(0, color='black', linewidth=0.65)
            plt.scatter(x, y, color='red', linewidths=10, label=f'COLISIÓN\nx: {x:.2f} - y: {y:.2f} - t: {alpha:.2f}')
            plt.scatter(x1, y1, color='blue', linewidths=5, label=f'Salida objeto 1\nVx: {vx1} Vy: {vy1}')
            plt.scatter(x2, y2, color='green', linewidths=5, label=f'Salida objeto 2\nVx: {vx2} Vy: {vy2}')
            plt.plot([x1, x], [y1, y], color='blue', ls="-.")
            plt.plot([x2, x], [y2, y], color='green', ls="-.")
            plt.legend()
            plt.xlabel('Eje X')
            plt.ylabel('Eje Y')
            plt.title('Punto de Colisión')
            plt.grid(True)
            plt.show()

        return colision

    except Exception as e:
        print(f"Error: {e}")
        return colision
