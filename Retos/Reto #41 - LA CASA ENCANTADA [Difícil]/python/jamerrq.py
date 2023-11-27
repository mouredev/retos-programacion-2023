import random
import os
import time

# MODO DEBUG
# Si debug es True, entonces se mostrarán todas las habitaciones
DEBUG_MODE = False

# Limpiar la pantalla
def clear(force=False):
    if DEBUG_MODE and not force:
        return
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
        'pregunta': 'Tom mide 1.80, es ayudante en una carnicería y lleva zapatos de la talla 45. ¿Qué pesa?',
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
        'pista': 'Lee bien la pregunta'
    },
    {
        'pregunta': 'Si un pastor tiene 15 ovejas y se le mueren todas menos nueve, ¿cuántas le quedan?',
        'respuesta': 'Nueve',
        'pista': 'Lee bien la pregunta'
    },
    {
        'pregunta': 'Tengo un arco y soy de madera, pero no una flecha. ¿Qué soy?',
        'respuesta': 'Un violín',
        'pista': 'Es un instrumento musical'
    },
    {
        'pregunta': 'Cuando me necesitas, me tiras. Cuando ya no me necesitas, me recoges. ¿Qué soy?',
        'respuesta': 'El ancla',
        'pista': 'Se usa en los barcos'
    },
    {
        'pregunta': 'Círculo redondo al que, si lo golpeas, das un buen brinco del susto. ¿Qué es?',
        'respuesta': 'El tambor',
        'pista': 'Porrumpompom'
    },
    {
        'pregunta': 'Dos abanicos que no paran en todo el día, pero cuando duermes se quedan quietos. ¿Qué son?',
        'respuesta': 'Las pestañas',
        'pista': 'Están en tus ojos'
    },
    {
        'pregunta': 'No tengo cabeza, pero sí cuello.',
        'respuesta': 'La botella',
        'pista': 'Se usa para beber'
    },
    {
        'pregunta': 'Pese a tener 4 patas, no puedo correr ni caminar. ¿Qué soy?',
        'respuesta': 'La silla',
        'pista': 'Se usa para descansar las nalgas 🌚'
    }
]

print('Hay {} acertijos'.format(len(acertijos)))


def preprocess(input):
    # Preprocesar la respuesta
    # 1. Quitar los espacios en blanco
    # output = input.replace(' ', '')
    output = input
    # 2. Quitar los signos de puntuación
    signos = ['.', ',', '¿', '?', '¡', '!',
              '(', ')', '[', ']', '{', '}', ':', ';', '-', '_', '—', '«', '»', '“', '”']
    for signo in signos:
        output = output.replace(signo, '')
    # 3. Quitar los acentos
    output = output.replace('á', 'a').replace('é', 'e').replace(
        'í', 'i').replace('ó', 'o').replace('ú', 'u')
    # 4. Convertir a minúsculas
    output = output.lower()
    # 5. Quitar los artículos (el, la, los, las, un, una, unos, unas)
    output = output.replace('el ', '').replace('la ', '').replace('los ', '').replace(
        'las ', '').replace('una ', '').replace('un ', '').replace('unos ', '').replace('unas ', '')
    return output


class Acertijo:

    def __init__(self, pregunta, respuesta, pista="", intentos=3):
        self.pregunta = pregunta
        self.respuesta = respuesta
        self.pista = pista
        self.pista_usada = False
        self.intentos = intentos
        self.resuelto = False

    def comprobar(self, respuesta):
        # print(preprocess(respuesta), preprocess(self.respuesta))
        return preprocess(respuesta) == preprocess(self.respuesta)

    def usar_pista(self):
        if self.pista_usada:
            print('Ya usaste la pista')
        else:
            print(self.pista)
            self.pista_usada = True

    def resolver(self, no_clear=False, n=0):
        if not n:
            print('🎩 ACERTIJO 🪄')
        else:
            print(f'🎩 ACERTIJO {n} de 2 🪄'.format(n))
        print('🧱'*20)
        answer = ''
        while (not self.comprobar(answer)) and self.intentos > 0:
            answer = input(self.pregunta + '\n ↪ ')
            if not self.comprobar(answer):
                self.intentos -= 1
                if self.intentos > 0:
                    print("Respuesta incorrecta 😔, te quedan {} intentos".format(
                        self.intentos))
                    print('Pista 🐦‍: ', self.pista)
        if self.comprobar(answer):
            if not no_clear:
                clear()
            print('🧱'*20)
            print("🎉 Respuesta correcta 🎉")
            print('🧱'*20)
            time.sleep(1)
            self.resuelto = True
            return True
        else:
            if not no_clear:
                clear()
            print('🧱'*20)
            print("💀 Respuesta incorrecta, perdiste una vida 💀")
            print('🧱'*20)
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
        while dulce_fila is None or self.habitaciones[dulce_fila][dulce_columna].type != 'normal' or not (dulce_fila + dulce_columna):
            dulce_fila = random.randint(0, n-1)
            dulce_columna = random.randint(0, m-1)
        dulce = Habitacion(dulce_fila, dulce_columna, 'dulce')
        # Colocar el dulce en la habitación correspondiente
        print('Dolce en: {}, {}'.format(dulce_fila, dulce_columna))
        self.habitaciones[dulce_fila][dulce_columna] = dulce

    def mostrar(self, x, y, jogando=True):

        def mostrar_habitacion(habitacion):
            # Si el jugador está en la habitación, mostrarlo
            if habitacion.x == x and habitacion.y == y and jogando and habitacion.type != 'dulce':
                # print(x, y)
                str_hab = str(habitacion)
                if habitacion.solved != None:
                    if habitacion.solved:
                        str_hab = '✅'
                    else:
                        str_hab = '❌'
                return '👤' + ' ' + str_hab
            elif habitacion.solved and jogando:
                return '   ✅'
            elif habitacion.solved == False and jogando:
                return '   ❌'
            # Si no se ha terminado el juego y la habitación
            # es de tipo fantasma, entonces mostrar una habitación normal (en
            # caso que no se haya resulto la habitación)
            elif habitacion.type == 'dulce':
                if not jogando or DEBUG_MODE:
                    return '   🍭'
                else:
                    return '   ⬜️'
            elif habitacion.type == 'fantasma':
                if jogando and not DEBUG_MODE:
                    if habitacion.solved == None:
                        return '   ⬜️'
                    elif habitacion.solved:
                        return '   ✅'
                    else:
                        return '   ❌'
                else:
                    return '   👻'
            else:
                return '   ' + str(habitacion)

        # Mostrar cada fila de la matriz
        for fila in self.habitaciones:
            print(' '.join([mostrar_habitacion(h) for h in fila]))


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
        # print()
        print('🧱'*20)
        print('🎩   Puntaje: {0:.2f}'.format(self.get_real_score()))
        print('🍄     Vidas: {}'.format(self.vidas))
        print('🗺️   Estás en: ({}, {})'.format(self.x, self.y))
        print('🥾     Pasos: {}'.format(self.steps))
        print('🔑 Acertijos: {}'.format(len(self.resueltas)))

    def get_real_score(self):
        return (self.score / max(1, self.steps)) + self.vidas

    def mover(self, direccion):
        if direccion == 'N' or direccion == 'n':
            if self.x > 0:
                self.x -= 1
                self.steps += 1
            else:
                clear()
                print('🧱'*20)
                print('🚫 No puedes ir hacia el norte 🚫')
                print('🧱'*20)
                time.sleep(1)

        elif direccion == 'S' or direccion == 's':
            if self.x < self.mansion.n-1:
                self.x += 1
                self.steps += 1
            else:
                clear()
                print('🧱'*20)
                print('🚫 No puedes ir hacia el sur 🚫')
                print('🧱'*20)
                time.sleep(1)

        elif direccion == 'E' or direccion == 'e':
            if self.y < self.mansion.m-1:
                self.steps += 1
                self.y += 1
            else:
                clear()
                print('🧱'*20)
                print('🚫 No puedes ir hacia el este 🚫')
                print('🧱'*20)
                time.sleep(1)

        elif direccion == 'W' or direccion == 'w':
            if self.y > 0:
                self.steps += 1
                self.y -= 1
            else:
                clear()
                print('🧱'*20)
                print('🚫 No puedes ir hacia el oeste 🚫')
                print('🧱'*20)
                time.sleep(1)

        elif direccion == 'X' or direccion == 'x':
            print('🎃 Hasta Luego 👋')
            self.jugando = False
        else:
            print('Dirección no válida')

    def jugar(self):
        clear(force=True)
        while self.jugando:
            clear()
            print('🧱'*20)
            print('🧱'*4 + '🏚️  MANSIÓN ENCANTADA 🏚️' + '🧱'*5)
            print('🧱'*20)
            if(DEBUG_MODE):
                print('🎃 MODO DEBUG 🐛')
                print('🧱'*20)
            self.mostrar()
            print('🧱'*20)
            options = ['N ↑', 'S ↓', 'E →', 'W ←']
            if self.x == 0:
                options.remove('N ↑')
            if self.x == self.mansion.n-1:
                options.remove('S ↓')
            if self.y == 0:
                options.remove('W ←')
            if self.y == self.mansion.m-1:
                options.remove('E →')
            direccion = input(f'🧭 ¿Hacia dónde quieres ir? [{", ".join(options)}]' +
                              '\n' + 'Presiona X para salir.' + '\n ↪ ')
            self.mover(direccion)
            habitacion = self.mansion.habitaciones[self.x][self.y]
            if habitacion.type == 'fantasma':
                if(habitacion.solved != None):
                    continue
                clear()
                print('🧱'*20)
                print('Has entrado en una habitación fantasma 👻')
                print('Debes resolver 2 acertijos para poder salir 🪤')
                print('🧱'*20)
                n = random.randint(0, len(acertijos)-1)
                while n in self.resueltas:
                    n = random.randint(0, len(acertijos)-1)
                acertijo1 = Acertijo(
                    acertijos[n]['pregunta'], acertijos[n]['respuesta'], acertijos[n]['pista'])
                if acertijo1.resolver(no_clear=True, n=1):
                    self.score += 50
                    self.resueltas.add(n)
                    n = random.randint(0, len(acertijos)-1)
                    while n in self.resueltas:
                        n = random.randint(0, len(acertijos)-1)
                    acertijo2 = Acertijo(
                        acertijos[n]['pregunta'], acertijos[n]['respuesta'], acertijos[n]['pista'])
                    if(acertijo2.resolver(no_clear=True, n=2)):
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
                print('🧱'*20)
                print('Ganaste el juego 🎉')
                print('Tu score es: {0:.2f}'.format(
                    self.score / self.steps + self.vidas))
                print('🧱'*20)
                print('TABLERO INICIAL 🏁')
                self.mansion.mostrar(self.x, self.y, False)
                print('🧱'*20)
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
                    continue
                clear()
                print('🧱'*20)
                print('Has entrado en una habitación normal 🛖')
                print('Debes resolver un acertijo para poder salir 🪤')
                print('🧱'*20)
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

def mostrar_mensaje_bienvenida():
    # Mostrar mensaje de bienvenida
    clear(force=True)
    print('🧱'*20)
    print('🎃 Bienvenido a la mansión encantada 🎃')
    print('🧱'*20,end="")
    print("""
🧙🏽 Sinopsis:
🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱
Acabas de entrar en una mansión encantada, la cuál consiste en una serie
de habitaciones. En cada habitación hay un acertijo que debes resolver
para poder pasar a la siguiente. Si resuelves el acertijo, ganas 50 puntos,
pero si no lo resuelves, pierdes una vida. Si pierdes todas las vidas,
pierdes el juego. Si logras encontrar el dulce, ganas el juego.
🧟 ¡Ten cuidado! Hay habitaciones fantasmas, las cuales tienen 2 acertijos
que debes resolver para poder salir. Si no los resuelves, pierdes una vida.
🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱
🎩 Cómo se calcula el puntaje:
🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱
El puntaje se calcula de la siguiente manera:
(puntaje / pasos) + vidas, por lo que es importante resolver los acertijos
en la menor cantidad de pasos posibles y con la mayor cantidad de vidas.
🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱
📝 Controles:
🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱
Para moverte, debes escribir la dirección hacia donde quieres ir:
N → Norte
S → Sur
E → Este
W → Oeste

Para salir del juego, debes escribir X
🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱
🔮 Para tener en cuenta:
🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱
- Si resuelves un acertijo, puedes volver a entrar en la habitación
pero ya no habrá acertijo y te aumentará el número de pasos.
- No debes preocuparte por acentos, signos de puntuación o
mayúsculas/minúsculas en las respuestas, ya que el juego se encarga
de validar eso. Por ejemplo, si la respuesta es "El perro", entonces
puedes escribir "el perro", "El Perro", "perro", etc.
- Si quieres ver el tablero completo, puedes cambiar el valor de la
variable DEBUG_MODE a True.
🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱
🧛 ¡Mucha suerte! Presiona cualquier tecla para comenzar 🪄
🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱
""")
    input(" ↪ ")



def main():
    # Crear la mansión
    mansion = Mansion()
    # Mostrar mensaje de bienvenida
    if not DEBUG_MODE:
        mostrar_mensaje_bienvenida()
    # Crear el juego
    juego = Juego(mansion)
    # Jugar
    juego.jugar()


if __name__ == "__main__":
    main()
