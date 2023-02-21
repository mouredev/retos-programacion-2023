class Pregunta:
    def __init__(self, pregunta, opciones, respuestas):
        self.pregunta = pregunta
        self.opciones = opciones
        self.respuestas = respuestas


class Cuestionario:
    def __init__(self, preguntas):
        self.preguntas = preguntas

    def hacer_preguntas(self):
        puntuaciones = {
            "Gryffindor": 0,
            "Hufflepuff": 0,
            "Ravenclaw": 0,
            "Slytherin": 0
        }
        for pregunta in self.preguntas:
            print(f"{pregunta.pregunta}\n")
            for num_opcion, opcion in enumerate(pregunta.opciones):
                print(f"{num_opcion+1}) {opcion}")
            respuesta_idx = None
            while respuesta_idx not in [1, 2, 3, 4]:
                try:
                    respuesta_idx = int(input("Ingresa tu respuesta (1-4): "))
                except ValueError:
                    print("Debes ingresar un número del 1 al 4.")
            respuesta = pregunta.respuestas[respuesta_idx - 1]
            print(f"Seleccionaste: {respuesta}\n")
            if respuesta == 'Gryffindor':
                puntuaciones["Gryffindor"] += 1
            elif respuesta == 'Hufflepuff':
                puntuaciones["Hufflepuff"] += 1
            elif respuesta == 'Ravenclaw':
                puntuaciones["Ravenclaw"] += 1
            elif respuesta == 'Slytherin':
                puntuaciones["Slytherin"] += 1

        casa_ganadora = max(puntuaciones, key=puntuaciones.get)
        return casa_ganadora


preguntas = [
    Pregunta(
        "¿Cuál de estas cualidades te define mejor?",
        ["Astucia", "Lealtad", "Inteligencia", "Coraje"],
        ["Slytherin", "Hufflepuff", "Ravenclaw", "Gryffindor"]
    ),
    Pregunta(
        "¿Qué tipo de animal te gustaría tener como mascota?",
        ["Lechuza", "Sapo", "Gato", "Rata"],
        ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    ),
    Pregunta(
        "¿Cuál de estas acciones valoras más en una persona?",
        ["Honestidad", "Inteligencia", "Valentía", "Lealtad"],
        ["Hufflepuff", "Ravenclaw", "Gryffindor", "Slytherin"]
    ),
    Pregunta(
        "¿Qué asignatura te gustaría estudiar en Hogwarts?",
        ["Adivinación", "Defensa contra las artes oscuras",
            "Pociones", "Cuidado de criaturas mágicas"],
        ["Ravenclaw", "Gryffindor", "Slytherin", "Hufflepuff"]
    ),
    Pregunta(
        "¿Cuál de estas actividades te parece más divertida?",
        ["Jugar al quidditch", "Leer un libro",
            "Hacer bromas", "Explorar lugares nuevos"],
        ["Gryffindor", "Ravenclaw", "Slytherin", "Hufflepuff"]
    )
]
cuestionario = Cuestionario(preguntas)
casa_ganadora = cuestionario.hacer_preguntas()

print(f"¡Felicidades! ¡Eres de la casa {casa_ganadora}!")
