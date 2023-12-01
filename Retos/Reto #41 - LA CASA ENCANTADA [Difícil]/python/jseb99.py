import random
import os

class CasaEncantada:
    def __init__(self) -> None:
        self._casa = [["⬜️","⬜️","⬜️","⬜️"],
                     ["⬜️","⬜️","⬜️","⬜️"],
                     ["⬜️","⬜️","⬜️","⬜️"],
                     ["⬜️","⬜️","⬜️","⬜️"]]
        self.pos_fantasmas = []
    @property
    def get_casa(self):
        print("-CASA ENCANTADA-")
        for habitacion in self._casa:
            print(" ".join(habitacion))
        print("-CASA ENCANTADA-")
    
    def crear_objetos(self):
        """
        Retorna la posición inicial del jugador en una lista [fila, columna]
        Crea fantasmas y Puerta
        """
        self.fila_puerta = random.randint(0,3)
        if self.fila_puerta in (1,2):
            self.columna_puerta = random.choice([0,3])
        else:
            self.columna_puerta = random.randint(0,3)
        
        # 🍭 cualquier posición, menos en la pos. puerta
        self.fila_dulce = random.randint(0,3)
        self.columna_dulce = random.randint(0,3)

        while (self.fila_dulce,self.columna_dulce)==(self.fila_puerta,self.columna_puerta):
            self.fila_dulce = random.randint(0,3)
            self.columna_dulce = random.randint(0,3)

        self._casa[self.fila_puerta][self.columna_puerta] = "🚪"
        self._casa[self.fila_dulce][self.columna_dulce] = "🍭" 
        self.fantasma()
        return [self.fila_puerta,self.columna_puerta]
        
    def fantasma(self):
        '''
        Crea posición de los fantasmas
        '''
        num_ghosts = 0
        for i in range(0, 16):
            ghost_rand = random.randint(1, 10)
            if ghost_rand == 1:
                num_ghosts += 1
        
        while num_ghosts > 0:
            while True:
                ghost_pos = random.randint(0, 15)
                if (ghost_pos // 4) != self.fila_puerta and int(ghost_pos % 4) != self.columna_puerta and (ghost_pos // 4) != self.fila_dulce and int(ghost_pos % 4) != self.columna_dulce:
                    break
            if self._casa[ghost_pos // 4][ghost_pos % 4] == "⬜️":
                self.pos_fantasmas.append([ghost_pos // 4,ghost_pos % 4])
            num_ghosts -= 1

class Jugador:
    def __init__(self,posicion: list):
        self.pos_jugador = posicion

    def movimiento(self):
        move = input("¿Hacia dónde quieres ir?: Norte(N), Sur(S), Este(E), Oeste(O): ").upper()
        while (move not in ("N","S","E","O")):
            move = input("¿Hacia dónde quieres ir?: Norte(N), Sur(S), Este(E), Oeste(O): ").upper()

        if move == "N":
            if self.pos_jugador[0]>0:
                self.pos_jugador[0] -= 1
            else:
                self.movimiento()
        elif move == "S":
            if self.pos_jugador[0]<3:
                self.pos_jugador[0] += 1
            else:
                self.movimiento()
        elif move == "E":
            if self.pos_jugador[1]<3:
                self.pos_jugador[1] += 1
            else:
                self.movimiento()
        elif move == "O":
            if self.pos_jugador[1]>0:
                self.pos_jugador[1] -= 1
            else:
                self.movimiento()

        return self.pos_jugador

class Juego(CasaEncantada, Jugador):
    def __init__(self):
        self.casa_encantada = CasaEncantada()  # Crear una instancia de CasaEncantada
        self.jugador = Jugador(self.casa_encantada.crear_objetos())  # Crear una instancia de Jugador
        self.preguntas = [
                {
                    'pregunta': '¿Cuál es la capital de Francia?',
                    'respuestas': {
                        'correcta': 'París',
                        'incorrecta': ['Londres', 'Madrid', 'Berlín']
                    }
                },
                {
                    'pregunta': '¿En qué año se fundó Apple Inc.?',
                    'respuestas': {
                        'correcta': '1976',
                        'incorrecta': ['1984', '1990', '2001']
                    }
                },
                {
                    'pregunta': '¿Cuál es el planeta más grande del sistema solar?',
                    'respuestas': {
                        'correcta': 'Júpiter',
                        'incorrecta': ['Marte', 'Venus', 'Saturno']
                    }
                },
                {
                    'pregunta': '¿Quién escribió la novela "Don Quijote de la Mancha"?',
                    'respuestas': {
                        'correcta': 'Miguel de Cervantes',
                        'incorrecta': ['William Shakespeare', 'Leo Tolstoy', 'Charles Dickens']
                    }
                },
                {
                    'pregunta': '¿Cuál es el río más largo del mundo?',
                    'respuestas': {
                        'correcta': 'Amazonas',
                        'incorrecta': ['Nilo', 'Misisipi', 'Danubio']
                    }
                },
                {
                    'pregunta': '¿En qué año se proclamó la independencia de Estados Unidos?',
                    'respuestas': {
                        'correcta': '1776',
                        'incorrecta': ['1789', '1812', '1900']
                    }
                },
                {
                    'pregunta': '¿Cuál es el metal más abundante en la corteza terrestre?',
                    'respuestas': {
                        'correcta': 'Aluminio',
                        'incorrecta': ['Hierro', 'Cobre', 'Plata']
                    }
                },
                {
                    'pregunta': '¿Cuál es la montaña más alta del mundo?',
                    'respuestas': {
                        'correcta': 'Monte Everest',
                        'incorrecta': ['Monte Kilimanjaro', 'Monte McKinley', 'Monte Fuji']
                    }
                },
                {
                    'pregunta': '¿Cuál es el quinto planeta del sistema solar?',
                    'respuestas': {
                        'correcta': 'Júpiter',
                        'incorrecta': ['Marte', 'Venus', 'Saturno']
                    }
                },
                {
                    'pregunta': '¿Cuál es el gas más abundante en la atmósfera de la Tierra?',
                    'respuestas': {
                        'correcta': 'Nitrógeno',
                        'incorrecta': ['Oxígeno', 'Dióxido de carbono', 'Argón']
                    }
                },
                {
                    'pregunta': '¿Quién pintó la Mona Lisa?',
                    'respuestas': {
                        'correcta': 'Leonardo da Vinci',
                        'incorrecta': ['Pablo Picasso', 'Vincent van Gogh', 'Rembrandt']
                    }
                },
                {
                    'pregunta': '¿Cuál es el océano más grande del mundo?',
                    'respuestas': {
                        'correcta': 'Océano Pacífico',
                        'incorrecta': ['Océano Atlántico', 'Océano Índico', 'Océano Ártico']
                    }
                },
                {
                    'pregunta': '¿Cuál es el proceso de convertir agua en vapor mediante calor?',
                    'respuestas': {
                        'correcta': 'Evaporación',
                        'incorrecta': ['Condensación', 'Sublimación', 'Fusión']
                    }
                },
                {
                    'pregunta': '¿Cuál es el quinto planeta del sistema solar?',
                    'respuestas': {
                        'correcta': 'Júpiter',
                        'incorrecta': ['Marte', 'Venus', 'Saturno']
                    }
                }
            ]

    def mezclar_lista(self, lista_original):

        lista = lista_original[:]
        longitud_lista = len(lista)

        for i in range(longitud_lista):
            indice_aleatorio = random.randint(0, longitud_lista - 1)

            temporal = lista[i]
            lista[i] = lista[indice_aleatorio]
            lista[indice_aleatorio] = temporal

        return lista

    def logica_preguntas(self, twice:bool):
        conteo = 0
        while twice:
            pregunta = random.choice(self.preguntas)
            respuestas = self.mezclar_lista([pregunta['respuestas']['correcta']]+pregunta['respuestas']['incorrecta'])
            print(f"Pregunta-->",self.preguntas.index(pregunta)+1,pregunta['pregunta'],"\n",
                    "1.",respuestas[0],"\n","2.",respuestas[1],"\n","3.",respuestas[2],"\n","4.",respuestas[3])
            respuesta_usuario = int(input("Selecciona 1,2,3 o 4: "))
            while respuesta_usuario not in (1,2,3,4):
                print("No escribas algo distinto, por favor.")
                respuesta_usuario = int(input("Selecciona 1,2,3 o 4: "))
            if (respuestas[respuesta_usuario-1] == pregunta['respuestas']['correcta']) and conteo != 2:
                conteo += 1
            if conteo == 2:
                return
        while not twice:
            pregunta = random.choice(self.preguntas)
            respuestas = self.mezclar_lista([pregunta['respuestas']['correcta']]+pregunta['respuestas']['incorrecta'])
            print(f"❓ Pregunta: ",self.preguntas.index(pregunta)+1,pregunta['pregunta'],"\n",
                    "1.",respuestas[0],"\n","2.",respuestas[1],"\n","3.",respuestas[2],"\n","4.",respuestas[3])
            respuesta_usuario = int(input("Selecciona 1,2,3 o 4: "))
            while respuesta_usuario not in (1,2,3,4):
                print("No escribas algo distinto, por favor.")
                respuesta_usuario = int(input("Selecciona 1,2,3 o 4: "))
            if respuestas[respuesta_usuario-1] == pregunta['respuestas']['correcta']:
                twice = True

    def empezar_juego(self):
        print("👻👻👻 Te encuentras en la entrada 👻👻👻")
        self.casa_encantada.get_casa
        self.jugador.movimiento()
        while self.jugador.pos_jugador[0] != self.casa_encantada.fila_dulce or self.jugador.pos_jugador[1] != self.casa_encantada.columna_dulce:
            self.clearScreen()
            print(f'📌 Te encuentas en la habitación: fila:{self.jugador.pos_jugador[0]}, columna:{self.jugador.pos_jugador[1]}')
            twice = False
            if self.jugador.pos_jugador in self.casa_encantada.pos_fantasmas:
                self.casa_encantada._casa[self.jugador.pos_jugador[0]][self.jugador.pos_jugador[1]] = "👻"
                twice = True
            self.casa_encantada.get_casa
            self.logica_preguntas(twice)
            self.jugador.movimiento()
        self.clearScreen()

        print("🎇🎇🎇FELICITACIONES🎇🎇🎇\n🍭🍭🍬🍬 Obtuviste el dulce 🍭🍭🍬🍬")    
    
    def clearScreen(self):
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    juego = Juego()
    juego.empezar_juego()
