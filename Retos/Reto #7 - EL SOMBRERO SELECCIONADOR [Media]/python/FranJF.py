"""
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
"""
import questionary


class SombreroSeleccionador:
    CASAS: dict = {
        "Gryffindor": {"puntuacion": 0, "respuesta_desempate": "Mi coraje"},
        "Slytherin": {"puntuacion": 0, "respuesta_desempate": "Mi astucia"},
        "Hufflepuff": {"puntuacion": 0, "respuesta_desempate": "Mi empatía"},
        "Ravenclaw": {"puntuacion": 0, "respuesta_desempate": "Mis conocimientos"},
    }
    PREGUNTAS: dict= {
        "¿Qué animal escogerías?": ["Búho", "Gato", "Perro", "Rata"],
        "Todos estos elixires te otorgan un poder, ¿cuál prefieres?": [
            "Fuerza",
            "Invisibilidad",
            "Capacidad de hablar con los animales",
            "Sabiduría",
        ],
        "Como recompensa por tus hazañas te otorgan únicamente un objeto de la Sala de los Menesteres, ¿cuál escoges?": [
            "Gema de la Inmortalidad",
            "La Varita de Saúco",
            "Unas gafas que te permiten leer la mente",
            "El Colgante de la Inteligencia",
        ],
        "¿Qué palabra te define mejor?": [
            "Valentía",
            "Liderazgo",
            "Lealtad",
            "Inteligencia",
        ],
        "¿Qué actividad habrías preferido hacer en tu estancia en la escuela?": [
            "Estar en el equipo de Quidditch",
            "Hacer bromas de los profesores",
            "La clase de herbología",
            "Leer en la biblioteca",
        ],
    }
    PREGUNTA_DESEMPATE: str = "¿Qué es lo que más temes perder?"

    def ceremonia_seleccion(self):
        for pregunta, opciones in self.PREGUNTAS.items():
            respuesta = self.__preguntar(pregunta, opciones)
            index_respuesta: int = self.PREGUNTAS[pregunta].index(respuesta)
            casa_escogida_por_su_index = list(self.CASAS.keys())[index_respuesta]
            self.CASAS[casa_escogida_por_su_index]["puntuacion"] += 1
        return self.__elegir_ganador()

    def __preguntar(self, pregunta: str, opciones: list) -> str:
        return questionary.select(pregunta, opciones).ask()

    def __elegir_ganador(self):
        puntuacion_mas_alta:int = 0
        casas_con_puntuacion_mas_alta: list = []
        for casa in self.CASAS:
            puntuacion:int = self.CASAS[casa]["puntuacion"]

            if puntuacion > puntuacion_mas_alta:
                puntuacion_mas_alta = puntuacion
                if casas_con_puntuacion_mas_alta:
                    casas_con_puntuacion_mas_alta.pop()
                casas_con_puntuacion_mas_alta.append(casa)
            elif puntuacion == puntuacion_mas_alta:
                casas_con_puntuacion_mas_alta.append(casa)

        if len(casas_con_puntuacion_mas_alta) == 1:
            return casas_con_puntuacion_mas_alta[0]
        else:
            return self.__desempatar(casas_con_puntuacion_mas_alta)

    def __desempatar(self, casas_empatadas:list):
        respuestas_desempate: list = []
        for casa_empatada in casas_empatadas:
            respuesta_desempate = self.CASAS[casa_empatada]["respuesta_desempate"]
            respuestas_desempate.append(respuesta_desempate)

        respuesta_desempate_usuario = self.__preguntar(self.PREGUNTA_DESEMPATE, respuestas_desempate)
        for casa in self.CASAS.keys():
            if self.CASAS[casa]["respuesta_desempate"] == respuesta_desempate_usuario:
                casa_ganadora = casa
                return casa_ganadora


print(SombreroSeleccionador().ceremonia_seleccion())
