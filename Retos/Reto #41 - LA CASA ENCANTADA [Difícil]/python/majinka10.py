"""
- Hacer un banco de unas 4 preguntas sobre cultura Halloween (peliculas,
libros, etc).
- El dulce aparecerá en cualquier habitación al azar a excepción
de la primera.
- La probabilidad de que aparezca un fantasta en una habitación es del
10%.
"""

import random

class Habitacion:
    def __init__(self):
        self.elemento = '⬜️' # Bloque de la habitación por defecto
        self.activada = False # Para saber si ya se 'entró' en la habitación
        self.superada = False # Para saber si ya se superó la pregunta de la habitación

    def colocar_fantasmas(self):
        # Probabilidad del 10% de un fantasma
        if self.elemento != '🍭': # Si al crear la mansión se asignó este cuadrito como el dulce, entonces no se le asignará otro
            if random.random() <= 0.1:
                self.elemento = '👻'
            else:
                self.elemento = '❓'
    
    def activar(self): # Lógica para activar la habitación
        if not self.activada: # Si la habitación aun no ha sido activada
            self.activada = True # Se establece en activada
            self.colocar_fantasmas() # Se coloca un fantasma o la incognita

    def __str__(self):
        # Si la habitación ya fue activada mostrará su elemento, sino el cuadrito por defecto
        if self.activada:
            return self.elemento
        else:
            return '⬜️'
        
class Pregunta:
    def __init__(self, enunciado, opciones, respuesta_correcta):
        # Cada pregunta tiene un enunciado, opciones y su respectiva respuesta correcta. 
        self.enunciado = enunciado
        self.opciones = opciones
        self.respuesta_correcta = respuesta_correcta

    def combrobar_respuesta(self, seleccion):
        # Para comprobar la respuesta. Se recibe la selección del usuario mediante un input (más adelante)
        # y corresponde con la respuesta correcta de la pregunta retorna True. 
        if seleccion == self.respuesta_correcta:
            return True

# Formato de las preguntas con temática Halloween. Enunciado - Opciones (lista) - Respuesta
halloween_questions = [
    Pregunta('¿Cuál es la película clásica de Halloween dirigida por John Carpenter?', [
        ('a. El Exorcista'),
        ('b. Psicosis'),
        ('c. Halloween'),
        ('d. El Resplandor')
    ], 'c'),
    Pregunta('¿Quién escribió la famosa historia "El extraño caso del Dr. Jekyll y Mr. Hyde"?', [
        ('a. Mary Shelley'),
        ('b. Bram Stoker'),
        ('c. Edgar Allan Poe'),
        ('d. Robert Louis Stevenson')
    ], 'd'),
    Pregunta('¿Cuál es el villano principal en la serie de películas "Pesadilla en Elm Street"?', [
        ('a. Jason Voorhees'),
        ('b. Leatherface'),
        ('c. Freddy Krueger'),
        ('d. Michael Myers')
    ], 'c'),
    Pregunta('¿Qué autor escribió el cuento clásico "La leyenda de Sleepy Hollow"?', [
        ('a. Washington Irving'),
        ('b. H.P. Lovecraft'),
        ('c. Stephen King'),
        ('d. Edgar Allan Poe')
    ], 'a'),
    Pregunta('¿Cuál es el nombre del libro escrito por Mary Shelley que presenta a un monstruo creado por la ciencia?', [
        ('a. Drácula'),
        ('b. Frankenstein'),
        ('c. El retrato de Dorian Gray'),
        ('d. El Hombre Invisible')
    ], 'b')
]

class Mansion:
    def __init__(self):
        # La mansión se inicializa con 16 habitaciones.
        self.habitaciones = [Habitacion() for _ in range(16)]
        # A cada habitación se le coloca un elemento. Especialmente nos interesa el indice de la 
        # habitación de entrada y salida, por eso las retorno.
        self.entrada, self.salida = self.colocar_elementos()

    # Función para colocar los elementos.
    def colocar_elementos(self):
        # La entrada es un numero aleatorio entre 0 y 15.
        entrada = random.randint(0, 15)
        # La salida es un numero aleatorio entre 0 y 15, diferente al de la entrada.
        while True:
            salida = random.randint(0, 15)
            if salida != entrada:
                break

        for i in range(16):
            if i == entrada:
                self.habitaciones[i].elemento = '🚪'
                self.habitaciones[i].activada = True
            elif i == salida:
                self.habitaciones[i].elemento = '🍭'
            else:
                # Si no es estrada ni salida. Se coloca como si no hubiera sido activada.
                self.habitaciones[i].activada = False
        return entrada, salida # Retorno el indice de la entrada y salida para la lógica del juego.

    def imprimir_mansion(self):
        # Se imprime la mansión por filas. Realmente toda la mansión es un array de 15 elementos.
        for i in range(0, 16, 4):
            fila = self.habitaciones[i:i+4]
            print(' '.join(map(str, fila)))
    
    # Lógica para imprimir la ubicación del jugador.
    def imprimir_mansion_con_jugador(self, posicion_jugador):
        for i in range(0, 16, 4):
            fila = self.habitaciones[i:i+4]
            for j, cuadro in enumerate(fila):
                if i + j == posicion_jugador:
                    print(' 🤺 ', end='')  # Marcar la posición del jugador con un emoji de jugador
                else:
                    print(f' {cuadro} ', end='')
            print()


class Juego:
    def __init__(self):
        # El juego se inicializa con una masión. Y la función jugar().
        self.mansion = Mansion()
        self.jugar()

    # Mensaje de bienvenida al juego.
    def bienvenida(self):
        print("Bienvenido a la mansión encantada.")
        print("Para encontrar el tesoro, deberás superar las incógnitas.")

    # Función para moverse por la mansión.
    def mover(self):
        # Dirección en la que se moverá el usuario.
        direccion = input("¿Hacia dónde quieres moverte? (norte/sur/este/oeste): ").lower()

        # Diferentes condicionales para evitar indices no adecuados. Además se manejan los indices de la posición actual
        # considerando que la mansión es un array de 16 elementos (habitaciones).
        if direccion == 'norte' and self.posicion_actual > 3:
            self.posicion_actual -= 4
        elif direccion == 'sur' and self.posicion_actual < 12:
            self.posicion_actual += 4
        elif direccion == 'este' and self.posicion_actual % 4 != 3:
            self.posicion_actual += 1
        elif direccion == 'oeste' and self.posicion_actual % 4 != 0:
            self.posicion_actual -= 1
        else:
            print("Movimiento inválido. Intenta de nuevo.")

        self.mansion.habitaciones[self.posicion_actual].activar()  # Activar la habitación al moverse a ella.
        self.mansion.imprimir_mansion_con_jugador(self.posicion_actual) # Mostrar la mansión con el jugador.
        self.explorar_habitacion()
    
    # Lógica para responder una pregunta en cada habitación.
    def responder_pregunta(self):
        # Primero, no le di muchas vueltas y escojo una pregunta al azar de la lista de preguntas.
        pregunta = random.choice(halloween_questions)
        print(pregunta.enunciado) # Se muestra el enunciado de la pregunta.
        # Se muestran las opciones de la pregunta.
        for opciones in pregunta.opciones:
            print(opciones)
        # Hago una lista con las opciones que se pueden escoger (por si el usuario se pone de chistoso)
        opciones_posibles = ['a', 'b', 'c', 'd']
        
        while True: # Este while se ejecuta mientras el usuario no haya ingresado la respuesta correcta.
            while True: # Este while se ejecuta mientras el usuario no haya ingresado una opción posible.
                seleccion = input('Escribe la letra de la opción correcta\n').lower()
                if seleccion in opciones_posibles:    
                    break
            # Con este if verifico la respuesta correcta (recibiendo la seleccion del usuario). Y hago a la habitación superada.
            if pregunta.combrobar_respuesta(seleccion):
                self.mansion.habitaciones[self.posicion_actual].superada = True
                return print('Correcto!\n')
            else: # Si el usuario falló, se imprime el siguiente mensaje y se reinicia el ciclo.
                print('Esa no era la respuesta correcta 😔. Inténtalo de nuevo!')

    # Lógica al moverse a una habitación determinada.
    def explorar_habitacion(self):
        # Primero se obtiene el objeto (habitación) de la lista de habitaciones de la mansión.
        habitacion_actual = self.mansion.habitaciones[self.posicion_actual]

        # Lógica si el elemento de la habitación es una incónita.
        if habitacion_actual.elemento == '❓':
            # Si la incógnita de la habitación no ha sido superada entonces se le hace la pregunta.
            if not habitacion_actual.superada:
                print("Te encuentras en una habitación con una incógnita ❓. Resuelve el acertijo.")
                self.responder_pregunta() # Lógica para resolver la incógnita (preguntas, etc.)
                self.mansion.imprimir_mansion_con_jugador(self.posicion_actual)

        # Si la habitación actual tiene el dulce entonces finaliza el juego.
        elif habitacion_actual.elemento == '🍭':
            print("¡Felicidades! Has encontrado el tesoro 🍭. ¡Juego completado!")
            return self.mansion.imprimir_mansion()

        # Lógica si el elemento de la habitación es un fantasma.
        elif habitacion_actual.elemento == '👻':
            # Si la incógnita de la habitación no ha sido superada entonces se le hacen dos preguntas.
            if not habitacion_actual.superada:
                print("¡Oh no! Has encontrado un fantasma 👻. Resuelve las preguntas para seguir adelante.")
                # Lógica para enfrentar el fantasma (preguntas adicionales, etc.)
                for _ in range(2):
                    self.responder_pregunta()
                self.mansion.imprimir_mansion_con_jugador(self.posicion_actual)
    
    # Lógica para jugar.
    def jugar(self):
        # Primero declaro la posicion actual con el indice de la entrada (donde está la puerta). Ahí siempre empezará el jugador.
        self.posicion_actual = self.mansion.entrada 
        self.bienvenida() # Se da el mensaje de bienvenida.
        self.mansion.imprimir_mansion() # Se imprime la mansión inicial.
        while self.posicion_actual != self.mansion.salida: # Este while hace que mientras no se haya llegado a la salida, el jugador se podrá seguir moviendo.
            self.mover()

# Crear el juego
juego = Juego()  