import tkinter as tk
import random
from tkinter import simpledialog, messagebox

'''entry = "🚪"
exit = "🍭"
room = "⬜"
ghost = "👻"
player = "🐍"'''


# Define las casillas
CASILLA_PUERTA = '🚪'
CASILLA_HABITACION_OCULTA = '⬜'
CASILLA_HABITACION_DULCES = '🍭'
CASILLA_ILUMINADA = '💡'

# Enigmas y respuestas
ENIGMAS_RESPUESTAS = {
    "¿Qué tiene ojos pero no puede ver?": "plátano",
    "¿Qué tiene llaves pero no abre puertas?": "piano",
    "¿Qué es lo que tiene dientes pero no puede morder?": "peine",
    # Agrega más enigmas y respuestas aquí
}

# Preguntas de los fantasmas y respuestas
PREGUNTAS_FANTASMAS_RESPUESTAS = {
    "Pregunta de fantasma 1": "R1",
    "Pregunta de fantasma 2": "R2",
    # Agrega más preguntas de fantasmas y respuestas aquí
}

class JuegoHalloween:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Juego de Halloween")
        self.jugador = simpledialog.askstring("Bienvenido", "Ingresa tu nombre:")
        self.ruta = [(0, 0)]
        self.intentos_restantes = 4
        self.instrucciones = "Instrucciones:\n\n1. Debes avanzar en la mansión 4x4 hasta encontrar la habitación de los dulces.\n\n2. Cada vez que avanzas hacia una casilla oculta, debes responder a un enigma o preguntas de fantasmas.\n\n3. Tienes 4 intentos para avanzar en la dirección que elijas (arriba, abajo, izquierda o derecha).\n\n4. Si respondes correctamente a un enigma o pregunta de fantasma, la casilla se iluminará.\n\n5. Si encuentras la habitación de los dulces, ¡has ganado, {}! ¡Diviértete!".format(self.jugador)
        self.crear_mansion()
        self.crear_interfaz()
        self.mostrar_instrucciones()

    def crear_mansion(self):
        # Crea la mansión como una matriz 4x4 con casillas ocultas
        self.mansion = [[CASILLA_HABITACION_OCULTA] * 4 for _ in range(4)]
        self.mansion[0][0] = CASILLA_PUERTA

        # Coloca la casilla de los dulces de manera aleatoria
        dulces_fila = random.randint(0, 3)
        dulces_columna = random.randint(0, 3)
        self.mansion[dulces_fila][dulces_columna] = CASILLA_HABITACION_DULCES

    def crear_interfaz(self):
        # Crea la interfaz gráfica con botones para cada habitación
        for fila, habitaciones_fila in enumerate(self.mansion):
            for columna, tipo_habitacion in enumerate(habitaciones_fila):
                boton = tk.Button(self.ventana, text=" ", font=("Arial", 16), command=lambda row=fila, col=columna: self.hacer_movimiento(row, col))
                boton.grid(row=fila, column=columna)

    def mostrar_instrucciones(self):
        respuesta_instrucciones = simpledialog.askstring("Instrucciones", "¿Quieres ver las instrucciones? (Sí/No)")
        if respuesta_instrucciones and respuesta_instrucciones.lower() == "si":
            messagebox.showinfo("Instrucciones", self.instrucciones)
        else:
            messagebox.showinfo("¡Comencemos!", "¡Que comience el juego!")

    def hacer_movimiento(self, fila, columna):
        if self.intentos_restantes == 0:
            return

        if fila < self.ruta[-1][0]:
            direccion = "arriba"
        elif fila > self.ruta[-1][0]:
            direccion = "abajo"
        elif columna < self.ruta[-1][1]:
            direccion = "izquierda"
        elif columna > self.ruta[-1][1]:
            direccion = "derecha"
        else:
            return

        self.intentos_restantes -= 1
        self.ruta.append((fila, columna))
        self.actualizar_interfaz()

        if direccion:
            if self.mansion[fila][columna] == CASILLA_HABITACION_DULCES:
                messagebox.showinfo("¡Felicidades!", "¡Has encontrado la habitación de los dulces, {}! ¡Has ganado!".format(self.jugador))
                self.ventana.quit()
            elif self.mansion[fila][columna] == CASILLA_HABITACION_OCULTA:
                if random.random() < 0.1:
                    # Aparece un fantasma
                    pregunta_fantasma = random.choice(list(PREGUNTAS_FANTASMAS_RESPUESTAS.keys()))
                    respuesta_correcta_fantasma = PREGUNTAS_FANTASMAS_RESPUESTAS[pregunta_fantasma]
                    respuesta_usuario = simpledialog.askstring("Fantasma", pregunta_fantasma)
                    if respuesta_usuario and respuesta_usuario.lower() == respuesta_correcta_fantasma.lower():
                        self.mansion[fila][columna] = CASILLA_ILUMINADA
                        self.actualizar_interfaz()
                        messagebox.showinfo("¡Escapaste del fantasma!", "Respuesta correcta. Puedes continuar.")
                    else:
                        messagebox.showerror("¡Fantasma te ha atrapado!", "Respuesta incorrecta. El fantasma te atrapó.")
                        self.ventana.quit()
                else:
                    # Pregunta de enigma
                    pregunta_enigma = random.choice(list(ENIGMAS_RESPUESTAS.keys()))
                    respuesta_correcta_enigma = ENIGMAS_RESPUESTAS[pregunta_enigma]
                    respuesta_usuario = simpledialog.askstring("Enigma", pregunta_enigma)
                    if respuesta_usuario and respuesta_usuario.lower() == respuesta_correcta_enigma.lower():
                        self.mansion[fila][columna] = CASILLA_ILUMINADA
                        self.actualizar_interfaz()
                    else:
                        messagebox.showerror("Respuesta Incorrecta", "La respuesta es incorrecta. Inténtalo de nuevo en otra habitación.")

        self.intentos_restantes = 4

    def actualizar_interfaz(self):
        for fila, habitaciones_fila in enumerate(self.mansion):
            for columna, tipo_habitacion in enumerate(habitaciones_fila):
                if tipo_habitacion == CASILLA_ILUMINADA:
                    self.ventana.grid_slaves(row=fila, column=columna)[0].config(text=tipo_habitacion)
                elif self.ruta[-1] == (fila, columna):
                    self.ventana.grid_slaves(row=fila, column=columna)[0].config(text="👣")
                else:
                    self.ventana.grid_slaves(row=fila, column=columna)[0].config(text=" ")

if __name__ == "__main__":
    ventana = tk.Tk()
    juego = JuegoHalloween(ventana)
    ventana.mainloop()

