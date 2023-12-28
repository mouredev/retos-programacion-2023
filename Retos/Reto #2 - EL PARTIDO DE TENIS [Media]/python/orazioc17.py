class Tennis:
    PUNTUACION = {
        0: 'Love',
        1: '15',
        2: '30',
        3: '40'
    }
    
    p1 = 0
    p2 = 0
    hay_ganador = False

    @staticmethod
    def comprobar_input(puntos: str):
        try:
            puntos = puntos.replace(' ', '')
            puntos = puntos.lower()
            lista_puntos = puntos.split(',')  
            
            for punto in lista_puntos:
                if punto != 'p1' and punto != 'p2':
                    raise Exception("Puntaje mal ingresado")

            if len(lista_puntos) < 4:
                raise Exception("Las puntuaciones ingresadas no son las minimas para que algun jugador pueda ganar")
        except Exception as e:
            print(e)
            return False
        
        return True

    def __init__(self, puntos: str):
        puntos = puntos.replace(' ', '')
        puntos = puntos.lower()
        lista_puntos = puntos.split(',') 
        self.lista_puntos = lista_puntos
            

    def sumar_p1(self):
        if self.p1 == 3 and self.p2 == 4:
            self.p2 -= 1
        else:
            self.p1 += 1

    def sumar_p2(self):
        if self.p1 == 4 and self.p2 == 3:
            self.p1 -= 1
        else:
            self.p2 += 1

    def convertir_puntaje(self, puntos: int) -> str:
        return self.PUNTUACION[puntos]

    def __str__(self):
        if self.p1 == 3 and self.p2 == 3:
            return 'Deuce'
        elif self.p1 == 3 and self.p2 == 4:
            return 'Ventaja P2'
        elif self.p1 == 4 and self.p2 == 3:
            return 'Ventaja P1'
        else:
            return f'{self.convertir_puntaje(self.p1)} - {self.convertir_puntaje(self.p2)}'

    def comprobar_terminar(self):
        if (self.p1 == 4 and self.p2 < 3) or self.p1 == 5:
            print('Ha ganado el P1')
            return True

        if (self.p2 == 4 and self.p1 < 3) or self.p2 == 5:
            print('Ha ganado el P2')
            return True

        return False

    def simular(self):
        for punto in self.lista_puntos:
            if punto == 'p1':
                self.sumar_p1()
            else:
                self.sumar_p2()

            if self.comprobar_terminar(): 
                self.hay_ganador = True
                return
            else:
                print(self.__str__())
        
        print('Oh, parece que no hay ganador, se acabaron los puntajes que nos proporcionaste')


def run():
    print("#"*25 + " Partido de Tenis " + "#"*25)
    print("\nPodras saber el resultado de un partido de tenis ingresando los puntos de los jugadores")
    print("Para ello, indica los puntos del jugador 1 con 'P1' y del jugador 2 con 'P2'")

    while True:
        puntos = input(
            "Ingresa la secuencia de puntos separada por coma (ejemplo: P1,P1,P2,P2,P1): ")
    
        if Tennis.comprobar_input(puntos):
            tennis = Tennis(puntos)
            tennis.simular()

            print('\nTermino la simulacion del partido, quieres simular otro partido o terminar el programa?')
            opcion = input('Ingresa 1 para volver a simular un partido o cualquier otro caracter para terminar el programa: ')

            if opcion != '1':
                quit()


if __name__ == '__main__':
    run()
