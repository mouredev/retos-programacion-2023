"""
 * Este es un reto especial por Halloween.
 * Te encuentras explorando una mansión abandonada llena de habitaciones.
 * En cada habitación tendrás que resolver un acertijo para poder avanzar a la siguiente.
 * Tu misión es encontrar la habitación de los dulces.
 *
 * Se trata de implementar un juego interactivo de preguntas y respuestas por terminal.
 * (Tienes total libertad para ser creativo con los textos)
 *
 * - 🏰 Casa: La mansión se corresponde con una estructura cuadrada 4 x 4
 *   que deberás modelar. Las habitaciones de puerta y dulces no tienen enigma.
 *   (16 habitaciones, siendo una de entrada y otra donde están los dulces)
 *   Esta podría ser una representación:
 *   🚪⬜️⬜️⬜️
 *   ⬜️👻⬜️⬜️
 *   ⬜️⬜️⬜️👻
 *   ⬜️⬜️🍭⬜️
 * - ❓ Enigmas: Cada habitación propone un enigma aleatorio que deberás responder con texto.
 *   Si no lo aciertas no podrás desplazarte.
 * - 🧭 Movimiento: Si resuelves el enigma se te preguntará a donde quieres desplazarte.
 *   (Ejemplo: norte/sur/este/oeste. Sólo deben proporcionarse las opciones posibles)
 * - 🍭 Salida: Sales de la casa si encuentras la habitación de los dulces.
 * - 👻 (Bonus) Fantasmas: Existe un 10% de que en una habitación aparezca un fantasma y
 *   tengas que responder dos preguntas para salir de ella.
 * - ✔
"""
import random
import os


class App:
    def __init__(self):
        self.casa = [["⬜️"] * 4 for _ in range(4)]
        self.salir = False
        self.contador_fantasma = 0

        print("BIENVENIDO A LA CASA ENCANTADA!")
        print("-------------------------------")
        print("Para salir debes encontrar la habitación de los dulces.")
        print("En cada habitación se te planteará una pregunta,")
        print("que tendrás que acertar para pasar a la siguiente habitación.")
        print("pero ten cuidado, si encuentras un fantasma, ")
        print("te hará una pregunta extra y tendrás que acertarla para derrotarlo.\n")

        (self.entrada, self.salida) = self.obtener_entrada_salida()
        self.posicion = self.entrada
        self.actualizar_matriz(1)
        self.pinta()
        self.jugar()


    def obtener_entrada_salida(self):
        entrada = [random.choice([0, 3]), random.randint(0, 3)]

        while True:
            salida = [random.choice([0, 3]), random.randint(0, 3)]
            if salida != entrada:
                return entrada, salida
        

    def actualizar_matriz(self, opcion):
        casa = self.casa
        x, y = self.posicion

        match opcion:
            case 0:
                casa[x][y] = "⬜️"
            case 1:
                casa[x][y] = "🚪"
            case 2:
                casa[x][y] = "❓"
            case 3:
                casa[x][y] = "✅"
            case 4:
                casa[x][y] = "👻"
            case 9:
                casa[x][y] = "🍭"

    def obtener_movimientos(self):
        x, y = self.posicion
        opciones = []

        if x > 0:
            opciones.append("N")
        if x < 3:
            opciones.append("S")
        if y > 0:
            opciones.append("W")
        if y < 3:
            opciones.append("E")

        return opciones

    def pinta(self):
        for _ in self.casa:
            print(" ".join(_))

    def borrar_pantalla(self):
        os.system ("clear") if os.name == "posix" else os.system ("cls")


    def preguntar_desplazamiento(self):
        opciones = self.obtener_movimientos()

        while True:
            print("Puedes moverte hacia: ")
            self.pinta_movimientos(opciones)
            opcion = input(f"Hacia donde quieres ir? ").upper()

            if opcion in opciones:
                return opcion
            
            print("La dirección no es válida.")

    def desplazamiento(self):
        opcion = self.preguntar_desplazamiento()

        x, y = self.posicion
        match opcion:
            case "N":
                x -= 1
            case "S":
                x += 1
            case "E":
                y += 1
            case "W":
                y -= 1

        self.posicion = [x, y]

        if self.posicion == self.salida:
            self.salir = True
            print("Encontraste la salida!!!")

    def pregunta(self):
        respuesta = input("pon OK: ")
        
        return respuesta.upper() == "OK"

    def pinta_movimientos(self, opciones):
        for opcion in opciones:
            match opcion:
                case "N":
                    print("N = Norte")
                case "S":
                    print("S = Sur")
                case "E":
                    print("E = Este")
                case "W":
                    print("W = Oeste")

    def obtener_tipo_habitacion(self):
        x, y = self.posicion

        if self.posicion == self.salida:
            return 9

        if self.casa[x][y] in ("🚪", "✅"):
            print("Por aqui ya has pasado!!!")
            return 1 if self.casa[x][y] == "🚪" else 3
      
        probabilidadFantasma = random.randint(0, 10)

        if self.contador_fantasma < 2 and probabilidadFantasma > 8:
            self.contador_fantasma += 1
            return 4

        return 2

    def jugar(self):
        while not self.salir:
            self.desplazamiento()
            tipo_habitacion = self.obtener_tipo_habitacion()
            self.actualizar_matriz(tipo_habitacion)
            self.borrar_pantalla()
            self.pinta()


            if tipo_habitacion == 2:
                respuesta = self.pregunta()

                if respuesta:
                    self.actualizar_matriz(3)

            elif tipo_habitacion == 4:
                respuesta = self.pregunta()

                if respuesta:
                    respuesta = self.pregunta()
                    
                    if respuesta:
                        self.actualizar_matriz(3) 


if __name__ == "__main__":
    App()
