# Reto #41: La casa encantada
#### Dificultad: Difícil | Publicación: 16/10/23 | Corrección: 23/10/23

## Enunciado

#
# Este es un reto especial por Halloween.
# Te encuentras explorando una mansión abandonada llena de habitaciones.
# En cada habitación tendrás que resolver un acertijo para poder avanzar a la siguiente.
# Tu misión es encontrar la habitación de los dulces.
#
# Se trata de implementar un juego interactivo de preguntas y respuestas por terminal.
# (Tienes total libertad para ser creativo con los textos)
#
# - 🏰 Casa: La mansión se corresponde con una estructura cuadrada 4 x 4
#   que deberás modelar. Las habitaciones de puerta y dulces no tienen enigma.
#   (16 habitaciones, siendo una de entrada y otra donde están los dulces)
#   Esta podría ser una representación:
#   🚪⬜️⬜️⬜️
#   ⬜️👻⬜️⬜️
#   ⬜️⬜️⬜️👻
#   ⬜️⬜️🍭⬜️
# - ❓ Enigmas: Cada habitación propone un enigma aleatorio que deberás responder con texto.
#   Si no lo aciertas no podrás desplazarte.
# - 🧭 Movimiento: Si resuelves el enigma se te preguntará a donde quieres desplazarte.
#   (Ejemplo: norte/sur/este/oeste. Sólo deben proporcionarse las opciones posibles)
# - 🍭 Salida: Sales de la casa si encuentras la habitación de los dulces.
# - 👻 (Bonus) Fantasmas: Existe un 10% de que en una habitación aparezca un fantasma y
#   tengas que responder dos preguntas para salir de ella.
#

import random

class Mansion:
    def __init__(self):
        self.dimensiones = 4
        self.mansión = [[Habitacion() for _ in range(self.dimensiones)] for _ in range(self.dimensiones)]
        self.colocar_puerta()
        self.colocar_dulces()
        self.colocar_fantasmas()
        self.revelar_puerta_inicial()

    def __str__(self):
        mansión_str = ""
        for fila in self.mansión:
            for habitacion in fila:
                mansión_str += str(habitacion)
            mansión_str += "\n"
        return mansión_str

    def colocar_puerta(self):
        borde = random.choice(['norte', 'sur', 'este', 'oeste'])
        if borde == 'norte':
            x = random.randint(0, self.dimensiones - 1)
        elif borde == 'sur':
            x = random.randint(0, self.dimensiones - 1)
        elif borde == 'este':
            y = random.randint(0, self.dimensiones - 1)
            x = self.dimensiones - 1
        else:
            y = random.randint(0, self.dimensiones - 1)
            x = 0

        self.mansión[y][x].contiene_puerta = True

    def colocar_dulces(self):
        x = random.randint(0, self.dimensiones - 1)
        y = random.randint(0, self.dimensiones - 1)
        self.mansión[y][x].contiene_dulces = True

    def colocar_fantasmas(self):
        for _ in range(self.dimensiones):
            for _ in range(self.dimensiones):
                if random.random() < 0.1:
                    x = random.randint(0, self.dimensiones - 1)
                    y = random.randint(0, self.dimensiones - 1)
                    self.mansión[y][x].contiene_fantasma = True

    def revelar_puerta_inicial(self):
        for y in range(self.dimensiones):
            for x in range(self.dimensiones):
                if self.mansión[y][x].contiene_puerta:
                    self.mansión[y][x].oculta = False

class Habitacion:
    def __init__(self):
        self.contiene_puerta = False
        self.contiene_dulces = False
        self.contiene_fantasma = False
        self.oculta = True
        self.enigma_resuelto = False

    def __str__(self):
        if not self.oculta:
            if self.contiene_puerta:
                return "🚪 "
            elif self.contiene_dulces:
                return "🍭 "
            elif self.contiene_fantasma:
                return "👻 "
            else:
                return "❓ "
        else:
            return "⬜ "

class Jugador:
    def __init__(self, mansion):
        self.mansion = mansion
        self.x, self.y = self.encontrar_posicion_inicial()
        self.enigmas_resueltos = 0

    def encontrar_posicion_inicial(self):
        for y in range(self.mansion.dimensiones):
            for x in range(self.mansion.dimensiones):
                if self.mansion.mansión[y][x].contiene_puerta:
                    return x, y

    def mover(self):
        direccion = input("¿Hacia dónde quieres moverte? (norte/sur/este/oeste): ").lower()
        x, y = self.x, self.y
        movimiento_valido = True

        if direccion == "norte":
            if y > 0:
                y -= 1
            else:
                movimiento_valido = False
        elif direccion == "sur":
            if y < self.mansion.dimensiones - 1:
                y += 1
            else:
                movimiento_valido = False
        elif direccion == "este":
            if x < self.mansion.dimensiones - 1:
                x += 1
            else:
                movimiento_valido = False
        elif direccion == "oeste":
            if x > 0:
                x -= 1
            else:
                movimiento_valido = False
        else:
            movimiento_valido = False

        if not movimiento_valido:
            print(f"No puedes moverte al {direccion}, estás en el borde {direccion}.")
            return

        habitacion_actual = self.mansion.mansión[y][x]
        habitacion_actual.oculta = False
        self.x, self.y = x, y

        if habitacion_actual.contiene_fantasma and not habitacion_actual.enigma_resuelto:
            print("¡Un 👻 te asusta!")
            self.resolver_enigmas(2)
        elif habitacion_actual.contiene_dulces and not habitacion_actual.enigma_resuelto:
            print("¡Encontraste 🍭! ¡Felicidades, has ganado!")
            habitacion_actual.enigma_resuelto = True
            self.enigmas_resueltos += 1
        elif not habitacion_actual.enigma_resuelto:
            self.resolver_enigmas(1)

    def resolver_enigmas(self, cantidad):
        enigmas = {
            "Enigma 1: Capital de Francia": "paris",
            "Enigma 2: Es redondo, se hincha y si lo pinchas explota, ¿qué es?": "un globo",
            "Enigma 3: Si me nombras, dejas de existir. ¿Qué soy?": "el silencio",
            "Enigma 4: Soy alto cuando joven y bajo cuando viejo, ¿qué soy?": "una vela"
        }

        for _ in range(cantidad):
            enigma = random.choice(list(enigmas.keys()))
            print(enigma)
            respuesta = input("¿Cuál es la respuesta? ").lower()
            if respuesta in enigmas.values():
                print("¡Resolviste el enigma! Puedes seguir adelante.")
            else:
                print("Respuesta incorrecta. No puedes avanzar.")

    def esta_fuera(self):
        if self.x < 0 or self.x >= self.mansion.dimensiones or self.y < 0 or self.y >= self.mansion.dimensiones:
            return True
        return False

if __name__ == "__main__":
    mansion = Mansion()
    jugador = Jugador(mansion)

    print("Bienvenido a la mansión. Debes encontrar el 🍭 para ganar el juego.")

    while not jugador.esta_fuera() and jugador.enigmas_resueltos < 2:
        print(mansion)
        jugador.mover()

    if jugador.enigmas_resueltos >= 2:
        print("¡Has ganado al resolver todos los enigmas! ¡Felicidades!")

    print("¡Gracias por jugar!")
