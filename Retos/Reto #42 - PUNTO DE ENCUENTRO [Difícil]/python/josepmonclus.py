'''
Crea una función que calcule el punto de encuentro de dos objetos en movimiento
en dos dimensiones.
- Cada objeto está compuesto por una coordenada xy y una velocidad de desplazamiento
  (vector de desplazamiento) por unidad de tiempo (también en formato xy).
- La función recibirá las coordenadas de inicio de ambos objetos y sus velocidades.
- La función calculará y mostrará el punto en el que se encuentran y el tiempo que tardarán en lograrlo.
- La función debe tener en cuenta que los objetos pueden no llegar a encontrarse.   
'''

class Objeto():    
    def __init__(self, origen, desplazamiento):
        self.origen = origen
        self.desplazamiento = desplazamiento

def check_encuentro(a: Objeto, b: Objeto):
    if a.desplazamiento[0] - b.desplazamiento[0] == 0:
        return "Los ojetos no se encontrarán nunca."
    else:
        tx = (b.origen[0] - a.origen[0]) / (a.desplazamiento[0] - b.desplazamiento[0])
    
    if a.desplazamiento[1] - b.desplazamiento[1] == 0:
        return "Los objetos no se encontrarán nunca."
    else:
        ty = (b.origen[1] - a.origen[1]) / (a.desplazamiento[1] - b.desplazamiento[1])
    
    if tx == ty:
        t = tx
        x = a.origen[0] + a.desplazamiento[0] * t
        y = a.origen[1] + a.desplazamiento[1] * t
    
    return f"Los objetos se encontrarán en la posicion ({x}, {y}) pasados {t}s"

a = Objeto((0, 0), (1, 1))
b = Objeto((1, 2), (0, 1))
print(check_encuentro(a, b))
    
a = Objeto((2, 0), (0, 1))
b = Objeto((0, 2), (1, 0))
print(check_encuentro(a, b))

a = Objeto((0, 0), (10, 5))
b = Objeto((100, 50), (-5, -2.5))
print(check_encuentro(a, b))

a = Objeto((0, 0), (1, 1))
b = Objeto((0, 0), (-1, -1))
print(check_encuentro(a, b))