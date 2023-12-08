import matplotlib.pyplot as plt
import time


def calcular_punto_encuentro():
    objeto1 = {
        'x': float(input("Ingrese la coordenada x del primer objeto: ")),
        'y': float(input("Ingrese la coordenada y del primer objeto: ")),
        'velocidadX': float(input("Ingrese la velocidad en la dirección x del primer objeto: ")),
        'velocidadY': float(input("Ingrese la velocidad en la dirección y del primer objeto: ")),
    }

    objeto2 = {
        'x': float(input("Ingrese la coordenada x del segundo objeto: ")),
        'y': float(input("Ingrese la coordenada y del segundo objeto: ")),
        'velocidadX': float(input("Ingrese la velocidad en la dirección x del segundo objeto: ")),
        'velocidadY': float(input("Ingrese la velocidad en la dirección y del segundo objeto: ")),
    }


    dx = objeto2['x'] - objeto1['x']
    dy = objeto2['y'] - objeto1['y']

    dvx = objeto2['velocidadX'] - objeto1['velocidadX']
    dvy = objeto2['velocidadY'] - objeto1['velocidadY']

    t = (dx * dvx + dy * dvy) / (dvx * dvx + dvy * dvy)

    if t >= 0:
        punto_encuentro_x = objeto1['x'] + objeto1['velocidadX'] * t
        punto_encuentro_y = objeto1['y'] + objeto1['velocidadY'] * t

        print(f"Los objetos se encuentran en ({punto_encuentro_x}, {punto_encuentro_y}) en t = {t} unidades de tiempo. \n")

        print("Abriendo dibujo del punto de encuentro entre dos objetos en movimiento")
        time.sleep(2)

        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.scatter(punto_encuentro_x, punto_encuentro_y, color='red', label='Punto de encuentro')
        plt.legend()
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
        plt.title('Punto de Encuentro de Objetos en Movimiento')
        plt.grid(True)
        plt.show()
    else:
        print("Los objetos no se encuentran en ningún punto.")  


calcular_punto_encuentro()
