import random
import os
import time

# Limpiar la pantalla


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Colección de acertijos
acertijos = [
    {
        'pregunta': '¿Qué cosa es la que cuanto más grande, menos se ve?',
        'respuesta': 'La oscuridad',
        'pista': 'Es lo contrario a la luz'
    },
    {
        'pregunta': '¿Qué cosa es la que cuanto más se moja, más se seca?',
        'respuesta': 'La toalla',
        'pista': 'Se usa para secar'
    },
    {
        'pregunta': 'Húmedo por dentro, con pelos por fuera. ¿De qué se trata?',
        'respuesta': 'El coco',
        'pista': 'Comienza por la letra C'
    },
    {
        'pregunta': '¿Qué cosa es la que tiene dientes y no come, tiene cabeza y no es un animal?',
        'respuesta': 'El ajo',
        'pista': 'Se usa para cocinar'
    },
    {
        'pregunta': 'Hay algo que, aunque te pertenezca, la gente siempre lo utiliza más que tú. ¿Qué es?',
        'respuesta': 'Tu nombre',
        'pista': 'Es algo que te identifica'
    },
    {
        'pregunta': '¿Qué cosa es la que tiene ojos y no ve, tiene agua y no es un pez?',
        'respuesta': 'Una papa',
        'pista': 'Se usa para cocinar'
    },
    {
        'pregunta': 'El hombre que lo vendió no lo quería. El hombre que lo compró no lo necesitaba. El hombre que lo usó no lo conocía. ¿Qué es?',
        'respuesta': 'Un ataúd',
        'pista': 'Se usa en un día muy triste'
    },
    {
        'pregunta': 'Tom mide 1,80, es ayudante en una carnicería y lleva zapatos de la talla 45. ¿Qué pesa?',
        'respuesta': 'Carne',
        'pista': 'Lee bien la pregunta'
    },
    {
        'pregunta': '¿Cuál es la mujer que siempre sabe donde está su marido?',
        'respuesta': 'La viuda',
        'pista': 'Es también un tipo de araña'
    },
    {
        'pregunta': '¿De qué color es el caballo blanco de Santiago?',
        'respuesta': 'Blanco',
        'pista': 'Es un caballo blanco'
    },
    {
        'pregunta': 'Si un pastor tiene 15 ovejas y se le mueren todas menos nueve, ¿cuántas le quedan?',
        'respuesta': 'Nueve',
        'pista': 'Lee bien la pregunta'
    }
]


class Acertijo:

    def __init__(self, pregunta, respuesta, pista="", intentos=3):
        self.pregunta = pregunta
        self.respuesta = respuesta
        self.pista = pista
        self.pista_usada = False
        self.intentos = intentos
        self.resuelto = False

    def comprobar(self, respuesta):
        return respuesta == self.respuesta or respuesta == self.respuesta.lower() or respuesta == self.respuesta.upper() or respuesta == self.respuesta.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u') or respuesta == self.respuesta.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').lower() or respuesta == self.respuesta.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').upper() or self.respuesta.replace('El ', '').replace('La ', '').replace('Los ', '').replace('Las ', '') == respuesta or self.respuesta.replace('El ', '').replace('La ', '').replace('Los ', '').replace('Las ', '') == respuesta.lower() or self.respuesta.replace('El ', '').replace('La ', '').replace('Los ', '').replace('Las ', '') == respuesta.upper()

    def usar_pista(self):
        if self.pista_usada:
            print('Ya usaste la pista')
        else:
            print(self.pista)
            self.pista_usada = True

    def resolver(self):
        print('🎩 ACERTIJO 🪄')
        answer = ''
        while (not self.comprobar(answer)) and self.intentos > 0:
            answer = input(self.pregunta + '\n -> ')
            if not self.comprobar(answer):
                self.intentos -= 1
                if self.intentos > 0:
                    print("Respuesta incorrecta 😔, te quedan {} intentos".format(
                        self.intentos))
                    print('Pista: ', self.pista)
        if self.comprobar(answer):
            clear()
            print('%'*50)
            print("🎉 Respuesta correcta 🎉")
            print('%'*50)
            time.sleep(1)
            self.resuelto = True
            return True
        else:
            clear()
            print('%'*50)
            print("💀 Respuesta incorrecta, perdiste una vida 💀")
            print('%'*50)
            time.sleep(1)
            return False


class Habitacion:

    # 4 Tipos de habitaciones: puerta (🚪), normal (🪟)
    # Fantasma (👻) y Dulce (🍭)
    def __init__(self, x, y, type, a1=None, a2=None, jogando=True):
        self.x = x
        self.y = y
        self.type = type
        self.solved = None

    def __str__(self):
        if self.type == 'puerta':
            return '🚪'
        elif self.type == 'normal':
            return '⬜️'
        elif self.type == 'fantasma':
            return '👻'
        elif self.type == 'dulce':
            return '🍭'
        else:
            return '🚫'

    def resolver(self, bool):
        self.solved = bool


class Mansion:

    def __init__(self, n=4, m=4, alpha_ghost=0.1):
        # Validar que las dimensiones sean mayores a 0
        if(n <= 0 or m <= 0):
            raise Exception(
                'Las dimensiones de la mansión deben ser mayores a 0')
        self.n = n
        self.m = m
        self.habitaciones = []

        # Jugador
        self.x = 0
        self.y = 0

        # Crear habitaciones

        # La habitación inicial es la (0,0) que corresponde
        # a la puerta de entrada
        puerta = Habitacion(0, 0, 'puerta')

        # Se crea una habitación dulce en una posición aleatoria
        dulce_fila = random.randint(1, n-1)
        dulce_columna = random.randint(1, m-1)
        # print('Dulce en: {}, {}'.format(dulce_fila, dulce_columna))
        dulce = Habitacion(dulce_fila, dulce_columna, 'dulce')

        # TODO: Implementar la creación de las habitaciones fantasmas

        # Crear las habitaciones normales
        primera_fila = [puerta]
        for j in range(1, m):
            prob = random.random()
            if prob <= alpha_ghost:
                primera_fila.append(Habitacion(0, j, 'fantasma'))
            else:
                primera_fila.append(Habitacion(0, j, 'normal'))
        self.habitaciones.append(primera_fila)
        for i in range(1, n):
            fila = []
            for j in range(m):
                prob = random.random()
                if prob <= alpha_ghost:
                    fila.append(Habitacion(i, j, 'fantasma'))
                else:
                    fila.append(Habitacion(i, j, 'normal'))
            self.habitaciones.append(fila)

        dulce_fila = None
        dulce_columna = None
        while dulce_fila is None or self.habitaciones[dulce_fila][dulce_columna].type != 'normal':
            dulce_fila = random.randint(1, n-1)
            dulce_columna = random.randint(1, m-1)
        # Colocar el dulce en la habitación correspondiente
        # dulce_fila = 0
        # dulce_columna = 1
        print('Dolce en: {}, {}'.format(dulce_fila, dulce_columna))
        self.habitaciones[dulce_fila][dulce_columna] = dulce

    def mostrar(self, x, y, jogando=True):

        def mostrar_habitacion(habitacion):
            # Si el jugador está en la habitación, mostrarlo
            if(habitacion.x == x and habitacion.y == y and jogando):
                str_hab = str(habitacion)
                if(habitacion.solved != None):
                    if(habitacion.solved):
                        str_hab = '✅'
                    else:
                        str_hab = '❌'
                return '👤' + ' ' + str_hab
            elif(habitacion.solved and jogando):
                return '   ✅'
            elif(habitacion.solved == False and jogando):
                return '   ❌'
            # Si no se ha terminado el juego y la habitación
            # es de tipo fantasma, entonces mostrar una habitación normal (en
            # caso que no se haya resulto la habitación)
            elif habitacion.type == 'dulce':
                if not jogando:
                    return '   🍭'
                else:
                    return '   ⬜️'
            elif habitacion.type == 'fantasma' and jogando:
                if habitacion.solved == None:
                    return '   ⬜️'
                elif habitacion.solved:
                    return '   ✅'
                else:
                    return '   ❌'
            elif habitacion.x == x and habitacion.y == y:
                return '👤' + ' ' + str(habitacion)
            else:
                return '   ' + str(habitacion)

        # def special_format(habitacion):
        #     if habitacion.type == 'puerta':
        #         return 'LA PUERTA'
        #     elif habitacion.type == 'fantasma':
        #         return 'HABITACIÓN FANTASMA'
        #     elif habitacion.type == 'dulce':
        #         return 'HABITACIÓN DULCE'
        #     else:
        #         return 'HABITACIÓN NORMAL'

        # Mostrar cada fila de la matriz
        for fila in self.habitaciones:
            print(' '.join([mostrar_habitacion(h) for h in fila]))

        # Mostrar la posición del jugador
        # print('Estás en: {}, {} ({})'.format(x, y,
        #       special_format(habitacion=self.habitaciones[x][y])))


class Juego:

    def __init__(self, mansion, vidas=3):
        self.mansion = mansion
        self.jugando = True
        self.vidas = vidas
        self.score = 0
        self.steps = 0
        self.resueltas = set([])
        # Esto para después, cuando se implemente el jugador
        # Me servirá para crear un sistema de guardado
        # para que el jugador pueda continuar después
        # y registrar su nombre en el ranking
        # self.jogador_name = ''
        self.x = 0
        self.y = 0

    def mostrar(self):
        self.mansion.mostrar(self.x, self.y, self.jugando)
        print('%'*50)
        print('🎩 Score: {}'.format(self.score))
        print('🍄 Vidas: {}'.format(self.vidas))
        print('🗺️  Estás en: {}, {}'.format(self.x, self.y))

    def mover(self, direccion):
        if direccion == 'N' or direccion == 'n':
            if self.x > 0:
                self.x -= 1
                self.steps += 1
            else:
                clear()
                print('%'*50)
                print('🚫 No puedes ir hacia el norte 🚫')
                print('%'*50)
                time.sleep(1)

        elif direccion == 'S' or direccion == 's':
            if self.x < self.mansion.n-1:
                self.x += 1
                self.steps += 1
            else:
                clear()
                print('%'*50)
                print('🚫 No puedes ir hacia el sur 🚫')
                print('%'*50)
                time.sleep(1)

        elif direccion == 'E' or direccion == 'e':
            if self.y < self.mansion.m-1:
                self.steps += 1
                self.y += 1
            else:
                clear()
                print('%'*50)
                print('🚫 No puedes ir hacia el este 🚫')
                print('%'*50)
                time.sleep(1)

        elif direccion == 'O' or direccion == 'o':
            if self.y > 0:
                self.steps += 1
                self.y -= 1
            else:
                clear()
                print('%'*50)
                print('🚫 No puedes ir hacia el oeste 🚫')
                print('%'*50)
                time.sleep(1)

        elif direccion == 'X' or direccion == 'x':
            print('Sayonara 👋')
            self.jugando = False
        else:
            print('Dirección no válida')

    def jugar(self):
        while self.jugando:
            clear()
            print('%'*50)
            self.mostrar()
            print('%'*50)
            direccion = input('¿Hacia dónde quieres ir? (N, S, E, O) ' +
                              '\n' + 'Presiona X para salir.' + '\n -> ')
            self.mover(direccion)
            habitacion = self.mansion.habitaciones[self.x][self.y]
            if habitacion.type == 'fantasma':
                # if(habitacion.solved != None):
                #     print('%'*50)
                #     print('Ya resolviste este acertijo 🪄')
                #     continue
                clear()
                print('Has entrado en una habitación fantasma 👻')
                print('Debes resolver 2 acertijos para poder salir 🪤')
                print('%'*50)
                n = random.randint(0, len(acertijos)-1)
                while n in self.resueltas:
                    n = random.randint(0, len(acertijos)-1)
                acertijo1 = Acertijo(
                    acertijos[n]['pregunta'], acertijos[n]['respuesta'], acertijos[n]['pista'])
                if acertijo1.resolver():
                    self.score += 50
                    self.resueltas.add(n)
                    n = random.randint(0, len(acertijos)-1)
                    while n in self.resueltas:
                        n = random.randint(0, len(acertijos)-1)
                    acertijo2 = Acertijo(
                        acertijos[n]['pregunta'], acertijos[n]['respuesta'], acertijos[n]['pista'])
                    if(acertijo2.resolver()):
                        self.resueltas.add(n)
                        self.score += 50
                        habitacion.resolver(True)
                    else:
                        habitacion.resolver(False)
                        self.vidas -= 1
                        if self.vidas == 0:
                            print(
                                'Has perdido todas las vidas, el juego ha finalizado 😞')
                            self.jugando = False
                else:
                    habitacion.resolver(False)
                    self.vidas -= 1
                    if self.vidas == 0:
                        print('Has perdido todas las vidas')
                        self.jugando = False
            elif habitacion.type == 'dulce':
                print('%'*50)
                print('Ganaste el juego 🎉')
                print('Tu score es: {0:.2f}'.format(
                    self.score / self.steps + self.vidas))
                print('%'*50)
                print('\nTABLERO INICIAL:')
                self.mansion.mostrar(self.x, self.y, False)
                habitacion.resolver(True)
                self.jugando = False
                break
            elif habitacion.type == 'puerta':
                # print('Has entrado en la puerta de la mansión 🚪')
                # habitacion.resolver(True)
                # self.jugando = False
                pass
            else:
                if(habitacion.solved != None):
                    print('%'*50)
                    print('Ya resolviste este acertijo 🪄')
                    continue
                clear()
                print('Has entrado en una habitación normal 🛖')
                print('Debes resolver un acertijo para poder salir 🪤')
                print('%'*50)
                n = random.randint(0, len(acertijos)-1)
                while n in self.resueltas:
                    n = random.randint(0, len(acertijos)-1)
                acertijo = Acertijo(
                    acertijos[n]['pregunta'], acertijos[n]['respuesta'], acertijos[n]['pista'])
                if acertijo.resolver():
                    self.resueltas.add(n)
                    self.score += 50
                    habitacion.resolver(True)
                else:
                    habitacion.resolver(False)
                    self.vidas -= 1
                    if self.vidas == 0:
                        print('Has perdido todas las vidas, el juego ha finalizado 😞')
                        self.jugando = False


def main():
    # Crear la mansión
    mansion = Mansion()
    # mansion.mostrar()
    juego = Juego(mansion)
    juego.jugar()


if __name__ == "__main__":
    main()
