# Crea un programa que simule la competición de dos coches en una pista.
# - Los dos coches estarán representados por 🚙 y 🚗. Y la meta por 🏁.
# - Cada pista tendrá entre 1 y 3 árboles 🌲 colocados de forma aleatoria.
# - Las dos pistas tendrán una longitud configurable de guiones bajos "_".
# - Los coches comenzarán en la parte derecha de las pistas. Ejemplo:
#   🏁____🌲_____🚙
#   🏁_🌲____🌲___🚗
# 
# El juego se desarrolla por turnos de forma automática, y cada segundo
# se realiza una acción sobre los coches (moviéndose a la vez), hasta que
# uno de ellos (o los dos a la vez) llega a la meta.
# - Acciones:
#   - Avanzar entre 1 a 3 posiciones hacia la meta.
#   - Si al avanzar, el coche finaliza en la posición de un árbol,
#     se muestra 💥 y no avanza durante un turno.
#   - Cada turno se imprimen las pistas y sus elementos.
#   - Cuando la carrera finalice, se muestra el coche ganador o el empate.

 
import random
import time


def pista_base(long):
    pista = ["_" for i in range(0,long)]
    return pista

def pista_con_arbol_aleatorio(pista):
    cantidad = random.randint(1,3)
    for i in range(1, cantidad + 1):
        pos = random.randint(0, len(pista)-1)
        pista[pos] = "🌲"
    return pista

class auto:

    def __init__(self, icono, pista : list):
        self.icono = icono
        self.puede_mover = True
        self.ganador = False
        self.pista = pista
        self.pista.insert(0,'🏁')
        self.pista.append(icono)   
        self.mostrar_pista() 
      
    def mostrar_pista(self):
        print(''.join(self.pista))
    
    def mover(self):
        cas = random.randint(2,4)
        indice = - cas
        try:
            if  self.puede_mover and self.pista[indice] == "🌲":
                self.puede_mover = False
                self.pista[indice] = '💥'
                self.pista = self.pista[:indice + 1]
            elif self.puede_mover:
                if self.pista[indice] == '🏁':
                    self.pista[indice] = self.icono
                    self.pista = self.pista[:indice + 1]
                    self.ganador = True
                else:
                    self.pista[indice] = self.icono
                    self.pista = self.pista[:indice + 1]
            else:
                self.puede_mover = True
            self.mostrar_pista()
        except:
            self.ganador = True
            self.pista = [self.icono]
            self.mostrar_pista()
    
    
        
        
def jugar():
    try:
        longitud_pista = int(input("Ingrese la longitud de pista deseada: "))
        print("¡En sus marcas!")
        time.sleep(1)
        print("¿¿¿¡Listos!???")
        auto1 = auto('🚙',pista_con_arbol_aleatorio(pista_base(longitud_pista)))
        auto2 = auto('🚗',pista_con_arbol_aleatorio(pista_base(longitud_pista)))
        time.sleep(1)
        print("¡¡¡YAAAAAAA!!!")
        while not auto1.ganador and not auto2.ganador:
            auto1.mover()
            auto2.mover()
            time.sleep(1)

        if auto1.ganador == auto2.ganador:
            print("Empate")
        elif auto1.ganador:
            print("¡¡VERDE GANADOR!!")
        else:
            print("¡¡ROJO GANADOR!!")
    except:
        print("Debe ingresar un entero")
jugar()
       
