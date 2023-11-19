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


class Vehiculo:
    # Constructor
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    # Métodos
    def mover(self):
        self.x += self.vx
        self.y += self.vy


def puntoEncuentro(vehiculo1 : Vehiculo, vehiculo2 : Vehiculo) -> str:
    tiempo = 0 ##se entrará en un bucle y en cada iteración se aumentará 1
    
    while(vehiculo1.x != vehiculo2.x or vehiculo1.y != vehiculo2.y) and tiempo != 100:
        vehiculo1.mover()
        vehiculo2.mover()
        tiempo += 1
    
    
    if(vehiculo1.x == vehiculo2.x and vehiculo1.y == vehiculo2.y):
        return f"Se encuentran en {vehiculo1.x,vehiculo1.y} en {tiempo} unidades de tiempo"
    else:
        return "No se han encontrado"
    

veh1 = Vehiculo(1,4,1,0)
veh2 = Vehiculo(4,0,0,1)

print(puntoEncuentro(veh1,veh2))